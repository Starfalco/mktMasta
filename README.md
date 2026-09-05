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
| Airflow UI | http://localhost:8080 | Pipeline orchestration |
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

### Production (Reverse Proxy — Recommended)
```bash
# .env on the server
FRONTEND_BASE_URL=          # Empty — frontend uses relative paths
FASTAPI_ORIGINS=http://your-domain.com,http://your-domain.com:8080
```

With a reverse proxy (Nginx/Apache) routing all requests to the same domain:
```
Nginx:
  /          → Angular static files
  /api/*     → Backend (port 8000)
  /cache/*   → Backend (port 8000)
  /config.json → Backend (port 8000)
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

┌─────────────────────────────────────────────────────┐
│  Production (Reverse Proxy)                         │
│                                                     │
│  Nginx (port 80/443)                                │
│    /          → Angular SPA                         │
│    /api/*     → FastAPI                             │
│    /config.json → FastAPI (serves frontend config)  │
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

## 1st phase
scrap stock market data via yfinance framework

compute peg ratios and other metadata
## 2nd phase
scraping macro economics data from FRED

scraping data from ism (institute for supply management) reports (manufacturing and services)
## 3rd phase
scraping options/derivatives data

compute pricer estimate based on Black-Scholes model (to help selecting stock target price and stop loss)
## 4th phase - can start after 1st phase done
generate an output for stock picking decisions (earnings calendar terms)

output front-end via a dataviz (power bi like or else, to be determinated)

genereate a short list selection based on those quantitatives (top 20 or other guideline)
## 5th phase
scheduling the entire pipeline on monthly or weekly basis (airflow or else)
## 6th phase
integrate a AI token output to sum up kpi's and additional main points from earnings call transcripts (as an input) with ollama apiRest
## 7th phase - in long term
in long term, storaging output and raw data for statistics purposes (regression model tests or else)

in long term ++, train a AI model or RAG (LLM or else if they are more convinient models) based on those output to generate stock picking decisions (in comparison with analysts choices)