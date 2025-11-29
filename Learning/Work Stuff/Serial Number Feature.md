- - - 
```table-of-contents
```
### **Architectural Plan: Referential Task Serial Numbers**

**Document Version:** 1.0
**Author:** Gemini Architect
**Status:** Approved for Implementation

### 1. Executive Summary

This document outlines the architecture and implementation plan for a new **Task Serial Number** feature. The goal is to generate a unique, human-readable, and stable identifier for every task in the system (e.g., `GD-101`).

This identifier will serve as a reliable reference point for project managers, clients, and internal teams, simplifying communication, tracking, and reporting.

The implementation will be phased:
*   **Phase 1 (Current Scope):** Generate prefixes based on the task's **`TaskCategory`**. This provides immediate value for internal operational efficiency.
*   **Phase 2 (Future):** Enhance the system to allow for optional, client-specific prefixes for key accounts. The architecture will be designed from day one to support this extensibility.

### 2. Core Architectural Decisions & Rationale

Several key decisions have been made to ensure the system is robust, scalable, and secure.

#### Decision 1: Prefix Source will be `TaskCategory`
*   **What:** The prefix for a serial number (e.g., the `GD` in `GD-101`) will be derived from the task's associated category (e.g., "Graphic Design").
*   **Why:**
    *   **Internal Operational Efficiency:** This provides the most immediate value to internal teams and project managers. A designer can instantly identify a task by its prefix, and team leads can easily filter and manage workloads for their department.
    *   **Universality & Consistency:** This model handles all tasks, both internal and client-facing, with a single, consistent logic. The meaning of a prefix (`WD` for "Web Development") is the same across the entire system.
    *   **Manageability:** The number of task categories is finite and controlled, leading to a small, stable, and easy-to-learn set of prefixes.

#### Decision 2: Number Generation Must Be an Atomic Operation
*   **What:** The process of reading the last number for a prefix, incrementing it, and saving it back must be performed as a single, indivisible database transaction.
*   **Why:** This is critical to prevent **race conditions**. Without an atomic operation, two users creating a task at the same millisecond could fetch the same last number (`100`), both attempt to create a task with the number `101`, and cause a unique constraint violation and a failed request. A database transaction with row-level locking guarantees that each new task gets a unique, sequential number, even under high load.

#### Decision 3: A Hybrid Strategy for Prefix Uniqueness
*   **What:** The system will use automated suggestions for prefixes, but administrators will have the final say, and the database will provide the ultimate guarantee of uniqueness.
*   **Why:** A purely automated system can't handle nuanced cases (e.g., "Acm Inc" and "Acm Ltd" both suggesting `ACM`). A purely manual system is tedious. The hybrid approach provides the best of both worlds:
    1.  **Suggest:** The system suggests a prefix.
    2.  **Check & Fallback:** It checks for duplicates and suggests an alternative if needed (e.g., `ACM1`).
    3.  **Manual Override:** The user can always enter their own custom prefix.
    4.  **Database Guarantee:** A `UNIQUE` constraint on the `prefix` column makes it impossible to create duplicates, acting as the final safety net.

### 3. Detailed Implementation Plan

#### 3.1. Database Schema (`prisma/schema.prisma`)

We will introduce a new table, `TaskSequence`, to manage the counters and update the `Task` table.

**Example Schema:**
```prisma
// New model to manage the sequence for each prefix atomically.
model TaskSequence {
  id            String       @id @default(uuid())
  
  // The unique prefix code, e.g., "GD", "WD", "ACME".
  // This has a unique constraint to be our ultimate safety net.
  prefix        String       @unique
  
  // The last number used for this prefix.
  // BigInt is used for effectively infinite scalability. A standard Int would
  // also suffice for millions of years, but BigInt is best practice.
  currentNumber BigInt       @default(0)

  // --- Link to the source of the prefix ---
  // This design makes our system extensible for the future hybrid model.
  // For Phase 1, only taskCategoryId will be used.
  taskCategoryId String?      @unique
  taskCategory   TaskCategory? @relation(fields: [taskCategoryId], references: [id])

  // This field is for the Phase 2 enhancement (client-specific prefixes).
  // clientId       String?      @unique
  // client         Client?      @relation(fields: [clientId], references: [id])

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Task {
  // ... all existing fields
  id           String @id @default(uuid())
  title        String
  // etc.

  // The new serial number field.
  // It is optional (?) initially to allow us to backfill existing tasks
  // without causing validation errors. It can be made required after backfilling.
  serialNumber String? @unique

  // An index on this column will ensure that looking up tasks by their
  // serial number is extremely fast.
  @@index([serialNumber])
}
```

#### 3.2. Backend Service: `TaskSerialNumberService`

*   **Purpose:** To centralize the logic for generating serial numbers.
*   **Location:** `apps/backend/api/services/taskSerialNumber.service.ts`
*   **Core Method:** `generateFor(prefix: string): Promise<string>`
*   **Critical Requirement:** This method **must** use Prisma's interactive transactions (`prisma.$transaction(...)`) to implement the atomic operation described in **Decision 2**.

    **Conceptual Flow (not literal code):**
    ```typescript
    // Inside the service...
    prisma.$transaction(async (tx) => {
      // 1. Find the sequence for the prefix and lock the row for update.
      // Prisma handles the underlying 'SELECT ... FOR UPDATE' query.
      const sequence = await tx.taskSequence.findUnique({ where: { prefix } });

      // 2. Increment the number.
      const newNumber = sequence.currentNumber + 1;

      // 3. Update the sequence with the new number.
      await tx.taskSequence.update({
        where: { prefix },
        data: { currentNumber: newNumber },
      });

      // 4. Return the formatted serial number.
      return `${prefix}-${newNumber}`;
    });
    ```

#### 3.3. API and Logic Integration

1.  **Task Creation:** The primary task creation logic must be modified to call `TaskSerialNumberService.generateFor()` before it creates the task. The returned serial number will be included in the `prisma.task.create()` call.
2.  **New Lookup Endpoint:** A new endpoint, `GET /api/tasks/by-serial/:serialNumber`, must be created.
    *   **Security:** This endpoint is a potential vector for Insecure Direct Object Reference (IDOR) attacks. It **must** be protected by the exact same authorization logic that protects `GET /api/tasks/:id`. The system must always verify that the authenticated user has permission to view the requested task.

#### 3.4. Rollout and Data Migration

1.  **Deployment:** Deploy the code changes for the new models, services, and endpoints. At this point, new tasks will get serial numbers, and old tasks will have `null`.
2.  **Backfilling Script:** Create and run a one-time script to populate serial numbers for all existing tasks. The script should:
    *   Iterate through all tasks where `serialNumber` is `null`, ordered by `createdAt`.
    *   For each task, determine its category prefix and generate a serial number using the new service.
    *   Update the task record.
3.  **Finalize Schema:** Once the backfill is complete and verified, the `serialNumber` field in `schema.prisma` can be changed from `String?` to `String` to make it a required field.

### 4. Frontend UI Design & User Experience

This section outlines how the Task Serial Number feature will be integrated into the user interface, ensuring a seamless and intuitive experience for task creation, viewing, and interaction.

#### 4.1. Task Creation UI (`InputForm` Component)

**Decision:** Introduce a dedicated input field for the serial number during task creation, leveraging automated suggestions and providing clear validation feedback.

*   **New Input Field:** A new, clearly labeled input field (e.g., "Task ID" or "Serial Number") will be added to the task creation form. This field will be distinct from the task title.
*   **Automated Prefix Suggestion:**
    *   When the user selects a `TaskCategory` (or if a default category is pre-selected), the frontend will trigger an API call to the backend (e.g., `GET /api/task-sequences/suggest-prefix?category_id=<id>`).
    *   The suggested prefix (e.g., `GD` for Graphic Design) will automatically populate the prefix part of the "Task ID" input field.
    *   **Benefit:** Reduces manual effort, ensures consistency, and guides users towards valid prefixes.
*   **Editable Input with Real-time Validation:**
    *   The user can edit the suggested prefix or type their own.
    *   As the user types (with a debounce to prevent excessive API calls), the frontend will make an API call (e.g., `GET /api/task-sequences/check-prefix-uniqueness?prefix=<user_input_prefix>`) to check if the entered prefix is unique.
    *   **Benefit:** Provides immediate feedback, preventing submission errors and improving user experience.
*   **Warning for Prefix Collisions:**
    *   **Scenario:** User types `ACM` for "Acm Ltd", but `ACM` is already used by "Acm Inc".
    *   **UI Action:** The UI will display a **warning message** (e.g., "Prefix 'ACM' is already in use. Consider using 'ACML' or another unique identifier.") directly below the input field. The user can still proceed, but they are informed of the potential issue.
    *   **Benefit:** Informs the user without blocking them, allowing for manual override if they have a specific reason.
*   **Error on Duplicate Serial Number (Backend Rejection):**
    *   **Scenario:** User submits the form, and the backend (due to a race condition or user ignoring a warning) detects that the generated serial number (e.g., `ACM-101`) is already taken.
    *   **UI Action:** The form submission will fail, and a prominent **error message** (e.g., "The serial number 'ACM-101' is already taken. Please try again or choose a different prefix.") will be displayed, prompting the user to correct the input.
    *   **Benefit:** Ensures data integrity by preventing duplicate serial numbers from being created.

#### 4.2. Display in Task Tables and Detail Views

**Decision:** Prominently display the serial number in all task listings and detail views, making it easily accessible and copyable.

*   **New Column in Task Tables:** A new column titled "Task ID" or "Serial Number" will be added to all relevant task listing tables (e.g., dashboard, client-specific task lists, search results).
    *   **Placement:** This column should be prominently placed, ideally as the first or second column (after any selection checkboxes or before the task title).
    *   **Benefit:** Allows users to quickly scan and identify tasks by their unique ID.
*   **Task Detail View:** The serial number will be displayed clearly at the top of the task detail page, near the task title.
*   **Copy Functionality:** A small, clickable icon (e.g., a copy icon) will be placed next to the serial number in both table and detail views, allowing users to easily copy the ID to their clipboard.
    *   **Benefit:** Facilitates quick sharing and referencing of tasks.

#### 4.3. Search Functionality

**Decision:** Enhance existing search capabilities to allow users to find tasks using their serial numbers.

*   **Enhanced Search Bar:** The global search bar and any task-specific search filters will be updated to include the `serialNumber` field in their search scope.
*   **Partial Search Support:** Users should be able to search by:
    *   Full serial number (e.g., `GD-101`).
    *   Prefix only (e.g., `GD` to find all Graphic Design tasks).
    *   Number only (e.g., `101` to find any task with that number, though this might yield many results).
*   **Benefit:** Provides a powerful new way for users to quickly locate specific tasks or groups of tasks.

#### 4.4. Referencing in Comments and Descriptions

**Decision:** Implement auto-linking and rich display for serial numbers mentioned within task comments and descriptions.

*   **Auto-linking/Highlighting:** When a user types a recognized serial number pattern (e.g., `GD-123`, `WNP-456`) in any rich text editor for comments or task descriptions, the UI will automatically:
    *   Highlight the serial number (e.g., change its color, make it bold).
    *   Convert it into a clickable link.
*   **Hover/Click Functionality:**
    *   **Hover:** Hovering over an auto-linked serial number will display a tooltip with essential task information (e.g., task title, current status, assignee).
    *   **Click:** Clicking on the linked serial number will navigate the user directly to that task's detail page.
*   **Backend Interaction:** The frontend will handle the parsing and display of these links. The backend will store the raw comment text, but the frontend will be responsible for rendering the interactive elements.
    *   **Benefit:** Greatly improves cross-referencing and navigation within the application, making conversations and documentation more efficient.

#### 4.5. Task Editing and Deletion

*   **Task Editing:** The serial number field will be displayed as **read-only** in the task editing interface. Once assigned, a serial number is immutable.
    *   **Benefit:** Maintains the integrity and stability of the task identifier.
*   **Task Deletion:** No direct UI interaction with the serial number during deletion, but the serial number will be part of the task record that is archived or removed.


### Prompt
here is our plan to implement Serial Numbers feature in whatsnetplease-monolith 
- lets start with what files do you need to start working on it 
- No need to assume any content ask when you need it Only provide code that is needed to be added or replaced unless its a new file 
- clarify anything you do not understand instead of assuming