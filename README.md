# Hospital Management MVP

Minimal patient registration and listing app with a **Python (FastAPI)** backend and **React (Vite)** frontend, using **MongoDB**.

## Structure

- `backend/` — FastAPI API (`POST/GET /api/patients`)
- `frontend/` — React SPA (Dashboard, Patients, Register Patient)

## Prerequisites

- Python 3.10+
- Node.js 18+
- MongoDB (optional for local demo): if MongoDB is not running, the API automatically uses in-memory storage (`mongomock`) so the UI still works; data is lost on restart. Set `MONGODB_URI` for a real database, or `USE_MONGOMOCK=1` to force in-memory mode.

## Run backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 7777
```

API: http://127.0.0.1:7777

**Windows `WinError 10013` or “address already in use”:** Another process is using port 7777. Stop it or pick a different port and update `frontend/vite.config.js` proxy `target` to match.

To find what is using a port: `netstat -ano | findstr :7777` then `tasklist /FI "PID eq <pid>"`.

## Run frontend

```bash
cd frontend
npm install
npm run dev
```

UI: http://localhost:1697 (proxies `/api` to http://127.0.0.1:7777)

## Tests

```bash
cd backend
pytest
```

Uses `mongomock` — no live MongoDB required for tests.
