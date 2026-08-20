# Case Study: Multi-File Upload System — HCC Chat App

A production-grade file attachment system supporting multiple files per message, built on presigned S3 uploads with async backend processing, real-time status sync, and resilient per-file failure handling.

---

## Overview

**Problem:** Chat messages needed to support attaching multiple files at once (images, documents, video) — uploaded directly from the browser without proxying large files through the app server, with clear feedback per file, and without one failed file blocking the rest of the batch.

**Stack:** S3 presigned URLs, client-side image compression + thumbnailing, Socket.IO for real-time status push, React Query for attachment metadata, a custom `useFileUpload` hook as the state machine.

---

## Architecture

### 1. Presigned Upload Flow (per file)
Rather than routing file bytes through the application server, the browser uploads directly to S3:

1. **Validate** — size, MIME type, and extension checked client-side against `FILE_CONSTRAINTS` before any network call
2. **Client-side thumbnail generation** — for supported image types, a thumbnail is generated in-browser
3. **Client-side compression** — image files are compressed before upload to reduce bandwidth and storage cost
4. **Request presigned URL(s)** — backend issues a presigned S3 PUT URL for the main file, and a second one for the thumbnail if applicable
5. **Direct-to-S3 upload** — browser PUTs the file straight to S3, with progress callbacks (90% weight reserved for the main file, 10% for the thumbnail)
6. **Complete** — `POST /attachments/complete` tells the backend the upload finished (filename, type, size, CDN URL, S3 bucket/key, ETag), creating the DB record

This keeps large file transfer entirely off the application server — it only ever handles small JSON payloads (URL requests, completion confirmations), not file bytes.

### 2. Async Processing Pipeline (backend)
On completion, an attachment starts in `processing` status, not immediately `ready`. A Lambda function (evidenced by integration test comments: *"awaiting Lambda processing"*) handles server-side work — thumbnail generation for files without a client-side thumbnail, video processing, etc. — then calls back to update status via S3 key lookup (`updateStatus(s3Key, "ready", metadata)`).

### 3. Real-Time Status Sync
Rather than polling, the frontend subscribes to per-attachment status over Socket.IO:
```typescript
socket.emit("subscribe_attachment_updates", {
  attachmentIds: memoizedAttachmentIds,
  requestCurrentStatus: true,
});
socket.on("attachment_status_update", handleStatusUpdate);
socket.on("attachment_processing_complete", handleProcessingComplete);
```
Subscriptions are id-list-diffed (sorted + compared) to avoid re-subscribing on every render — only fires when the actual set of tracked attachment IDs changes.

### 4. Batch Upload State Machine (`useFileUpload` hook)
A single hook centralizes the entire batch's lifecycle:
- **State:** `pendingFiles` (local, not-yet-uploaded), `uploadedAttachments` (confirmed), `isUploading`
- **Per-file status:** `pending → uploading → completed | failed`, tracked independently per file in the batch
- **Sequential upload**, not parallel — deliberate choice to avoid overwhelming the connection/server with N simultaneous large uploads
- **Failure isolation:** a failed file is caught, marked `failed` with its error message, and the loop **continues** to the next file rather than aborting the whole batch
- **Granular retry:** `retryFailedUploads` (all failed) and `retrySpecificFile` (one at a time) — a user doesn't have to re-select and re-upload an entire successful batch because one file failed
- **Send-blocking logic:** `hasOnlyFailedFiles` distinctly tracks "every file in this batch failed" to block message send, separate from "some failed, some succeeded" which allows sending with the successful subset

---

## Design Decisions Worth Highlighting

### Batch validation before any upload starts
`validateFiles()` checks total file count against `maxFilesPerMessage` **and** combined size against `maxTotalSize` up front — a user seeing "too many files" or "total size exceeded" immediately, rather than watching 8 of 10 files upload successfully before hitting a limit on file 9.

### Direct-to-S3 over server-proxied uploads
The presigned URL pattern means the app server's request-handling capacity isn't consumed by large file transfers — it only issues short-lived signed URLs and confirms completion. This is the standard pattern for scaling file upload without scaling the app server alongside it.

### Sequential over parallel batch uploads
A tradeoff explicitly made for server/connection stability over raw upload speed. For a chat context (a handful of attachments per message, not bulk data import), the UX cost of sequential upload is low and the reliability gain is real.

### Async processing simplified to synchronous, later
Code comments (`// ✅ UPDATED: Since files are now immediately ready`) show the system originally treated `ready` as a delayed, Lambda-driven state the frontend had to wait and listen for — and was later simplified so files become ready essentially immediately after upload completes. This is a good "recognized when an async architecture was solving a problem that no longer existed, and simplified it" story, though the exact trigger for that change isn't captured in what's available here.

---

## Testing Rigor (worth mentioning directly — this isn't just "it works")

- **Unit tests** on the repository layer (status transitions, `findByStatus`, `findReadyAttachments`, per-user storage quota calculation via `getTotalSizeByUser`)
- **Service-layer tests** covering authorization (`ForbiddenError` when a different user tries to download), state validation (`BadRequestError` on downloading a non-`ready` attachment), and cleanup resilience (deletion continues even if thumbnail delete fails)
- **Integration tests against real S3** — full upload → complete → verify-object-exists → simulate-processing-callback flow, not mocked
- **Performance tests with explicit budgets** — e.g. upload-URL generation asserted under 500ms, 10 concurrent upload-URL requests averaging under 2000ms, thumbnail URL generation under 700ms — these are real, numeric performance assertions in the test suite, not just functional checks
- **Storage quota enforcement test** — confirms a 25MB file is correctly rejected with a clear error message

This combination (unit + integration + performance testing on a file upload feature) is a strong, concrete answer if asked "how do you know your system works under load" — most candidates can describe an upload flow; fewer can point to a performance test asserting concurrent-request latency budgets.

---

## Honest Gaps (for interview credibility — say these if asked "what would you improve")

### Match-by-name-and-size reconciliation risk
When removing completed files from `pendingFiles` after a successful batch upload, the code matches attachments back to their pending-file entries by `file.name === attachment.name && file.size === attachment.size`:
```typescript
const pendingFile = filesToUpload.find(
  (f) => f.file.name === attachment.name && f.file.size === attachment.size,
);
```
Two different files in the same batch with identical name **and** identical size (plausible — e.g. two screenshots both named `image.png` at the same resolution) could collide during this reconciliation step. Each `pendingFile` already carries a unique `id` — using that as the correlation key throughout instead of name+size would remove this edge case entirely. Worth naming as a known, low-probability but real gap.

### Cleanup on delete tolerates partial failure by design
`deleteAttachment` deletes the main S3 file, then attempts thumbnail deletion in a separate try/catch that only logs on failure rather than throwing — a deliberate choice so a thumbnail-delete failure doesn't block the overall delete. This is defensible (better to have an orphaned thumbnail than a stuck "can't delete" attachment) but does mean orphaned thumbnail files can accumulate in S3 with no automatic sweep.
