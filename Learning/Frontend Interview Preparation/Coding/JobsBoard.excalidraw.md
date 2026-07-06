---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useState, useEffect } from "react";
const IDS_URL = "https://hacker-news.firebaseio.com/v0/jobstories.json";
export default function App() {
  const [jobsList, setJobsList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [ids, setIds] = useState([]);
  const [error, setError] = useState("");
  const fetchIds = async () => {
    try {
      const response = await fetch(IDS_URL);
      const idsList = await response.json();
      /// fetch job details for 6 ids
      setIds(idsList);
    } catch (e) {
      setError(e.message);
    }
  };
  useEffect(() => {
    fetchIds();
  }, []);

  useEffect(() => {
    let cancelled = false;

    const fetchInitialJobs = async () => {
      if (ids.length > 0) {
        try {
          const idsBatch = ids.slice(0, 6);
          const result = await Promise.all(
            idsBatch.map((id) =>
              fetch(
                `https://hacker-news.firebaseio.com/v0/item/${id}.json`,
              ).then((res) => res.json()),
            ),
          );
          if (!cancelled) {
            accumulateJobsListing(result);
            setLoading(false);
          }
        } catch (e) {
          if (!cancelled) {
            setError(e.message);
            setLoading(false);
          }
        }
      }
    };

    fetchInitialJobs();

    return () => {
      cancelled = true;
    };
  }, [ids]);
  const accumulateJobsListing = (newJobsList) => {
    setJobsList((prevJobsList) => [...prevJobsList, ...newJobsList]);
  };

  const retryHandler = () => {
    setLoading(true);
    setError("");
    if (ids.length === 0) {
      fetchIds();
    } else {
      fetchJobsByIndex(jobsList.length, jobsList.length + 6);
    }
  };
  const fetchJobsByIndex = async (start, end) => {
    try {
      if (ids.length > 0) {
        const idsBatch = ids.slice(start, end);
        const result = await Promise.all(
          idsBatch.map((id) =>
            fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`).then(
              (res) => res.json(),
            ),
          ),
        );
        accumulateJobsListing(result);
      }
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };
  const loadMoreHanlder = () => {
    setLoading(true);
    fetchJobsByIndex(jobsList.length, jobsList.length + 6);
  };
  return (
    <div>
      <h2 className="title">Hacker News Job Board</h2>
      {error && jobsList.length > 0 ? (
        <>
          <div>
            {jobsList.map((job) => (
              <JobTile key={job.id} job={job} />
            ))}
          </div>
          {jobsList.length > 0 && ids.length !== jobsList.length && (
            <button className="btn" onClick={loadMoreHanlder}>
              {loading ? "Loading..." : "Load more jobs"}
            </button>
          )}
          <div className="error">
            {error}
            <button onClick={retryHandler}>Retry</button>
          </div>
        </>
      ) : error && jobsList.length === 0 ? (
        <div className="error">
          {error}
          <button onClick={retryHandler}>Retry</button>
        </div>
      ) : loading && jobsList.length === 0 ? (
        <p>Loading.....</p>
      ) : (
        <>
          <div>
            {jobsList.map((job) => (
              <JobTile key={job.id} job={job} />
            ))}
          </div>
          {jobsList.length > 0 && ids.length !== jobsList.length && (
            <button className="btn" onClick={loadMoreHanlder}>
              {loading ? "Loading..." : "Load more jobs"}
            </button>
          )}
        </>
      )}
    </div>
  );
}

const JobTile = ({ job }) => {
  const date = new Date(job.time * 1000);
  return (
    <div style={{ display: "flex", flexDirection: "column", padding: "10px" }}>
      {job.url ? (
        <a href={job.url} target="_blank" className="link">
          {" "}
          {job.title}{" "}
        </a>
      ) : (
        <h4 style={{ margin: 0 }}>{job.title} </h4>
      )}
      <div className="row">
        <p>BY {job.by}</p>.<p> {date.toLocaleString()} </p>
      </div>
    </div>
  );
};
 ^0bLyuQES

Style.css ^4T1qVu3x

App.js ^eY0cPTLn

body {
  font-family: sans-serif;
}
.error {
  color: red;
  background: rgb(226, 172, 172);
  font-size: 14px;
  padding: 1rem;
  border: 1px solid red;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
}

.btn {
  background-color: rgb(233, 83, 24);
  color: white;
  padding: 0.5rem 0.5rem;
  border-radius: 4px;
  border: none;
}

.btn:hover {
  cursor: pointer;
  background-color: orangered;
}

.title {
  color: orangered;
}

.row {
  display: flex;
  flex-direction: row;
  font-size: 10px;
  color: gray;
  gap: 2px;
  align-items: center;
}

.link {
  color: black;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
}
 ^vXHzPVsw

## Embedded Files
72a3ff0f03c786044f73b64e052938247de70b0d: [[Screenshot 2026-07-06 at 10.46.32 PM.png]]

%%
## Drawing
```compressed-json
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

NkBCA66uADGKnIJOhOgwAMoHfgQAA===
```
%%