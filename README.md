# MKTmasta

Stock Market Analysis Platform — Angular frontend, FastAPI backend, Airflow pipelines.

## Quick Start (Local Development)

```bash
# 1. Install Docker (Docker Desktop for Windows/Mac)

# 2. Set up environment variables (optional — defaults work for local dev)
cp .env.example .env

# 3. Build and run all services
#    (or follow the commands in the .bash file)
docker compose up --build -d
```

**Services:**
| Service | URL | Description |
|---------|-----|-------------|
| Frontend (Angular) | http://localhost:4200 | Dev server with hot reload + API proxy |
| Backend (FastAPI) | http://localhost:8000 | REST API + OpenAPI docs at /docs |
| Airflow UI | http://localhost:1080 | Pipeline orchestration |
| PgAdmin | http://localhost:8888 | Database admin |

The Angular dev server proxies all `/api/*` and `/cache/*` requests to the FastAPI backend automatically via `proxy.conf.json`.

## Environment Configuration

This project uses **runtime config discovery** — the frontend fetches its configuration from the backend at startup. This means:

- **No hardcoded URLs** in the frontend code
- **Build once, deploy anywhere** — no rebuild needed when changing servers
- **Master branch stays clean** — no environment-specific config files

### Local Development
```bash
# .env (or just use defaults)
FRONTEND_BASE_URL=          # Empty = relative paths (works with dev proxy)
FASTAPI_ORIGINS=http://localhost:4200,http://localhost:8000
```

### Production (Direct Deployment)
```bash
# .env on the server
FRONTEND_BASE_URL=http://your-server-ip:8000
FASTAPI_ORIGINS=http://your-server-ip:4200,http://your-server-ip:8080,http://your-server-ip:8000
```

The frontend will fetch `/config.json` from the backend and use the `baseUrl` to construct API URLs.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  Docker Compose (Local Dev)                         │
│                                                     │
│  Angular (ng serve + proxy)  ←→  FastAPI (port 8000)│
│  Port 4200                    Port 8000             │
│  Proxies /api, /cache       CORS configured         │
└─────────────────────────────────────────────────────┘
```

## Tech Stack

- **Frontend:** Angular (TypeScript)
- **Backend:** FastAPI (Python)
- **Pipeline:** Apache Airflow
- **Data:** yfinance, FRED, ISM reports
- **Deployment:** Docker / Docker Compose

## Project Phases

### 1st phase ✅
- Scrap stock market data via yfinance framework
- Compute PEG ratios and other metadata

### 2nd phase ✅
- Scraping macro economics data from FRED
- Scraping data from ISM (Institute for Supply Management) reports

### 3rd phase ⏳
- Scraping options/derivatives data
- Compute pricer estimate based on Black-Scholes model

### 4th phase ⏳
- Generate stock picking decisions (earnings calendar terms)
- Output front-end via data visualization
- Generate short list selection based on quantitative metrics

### 5th phase ⏳
- Schedule the entire pipeline on monthly or weekly basis (Airflow)

### 6th phase ⏳
- Integrate AI token output for earnings call transcript analysis (Ollama API)

### 7th phase — Long term 🔮
- Store output and raw data for statistics (regression models)
- Train AI model or RAG based on outputs for stock picking decisions
