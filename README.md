<<<<<<< HEAD
# ADK Gemini Agent — Render Deployment Guide

## Project Structure
```
my-adk-agent/
├── agent.py          # ADK Agent definition + tools
├── main.py           # FastAPI HTTP server
├── requirements.txt  # Python dependencies
├── render.yaml       # Render service configuration
└── README.md
```

---

## Prerequisites
- [Render](https://render.com) account (free tier works)
- Gemini API key → get one free at https://aistudio.google.com
- Your code pushed to a **GitHub** or **GitLab** repo

---

## Step 1 — Get your Gemini API Key
1. Go to https://aistudio.google.com
2. Click **Get API Key** → **Create API key**
3. Copy the key — you'll need it in Step 3

---

## Step 2 — Push code to GitHub
```bash
git init
git add .
git commit -m "Initial ADK agent"
git remote add origin https://github.com/YOUR_USERNAME/adk-gemini-agent.git
git push -u origin main
```

---

## Step 3 — Deploy on Render
1. Go to https://render.com → **New** → **Web Service**
2. Connect your GitHub repo
3. Render auto-detects `render.yaml` — confirm these settings:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Under **Environment Variables**, add:
   ```
   Key:   GOOGLE_API_KEY
   Value: your_gemini_api_key_here
   ```
5. Click **Create Web Service**

Render will build and deploy. In ~2 minutes you get a live URL like:
```
https://adk-gemini-agent.onrender.com
```
That URL is your **submission link**.

---

## Test your deployed agent
```bash
# Health check
curl https://adk-gemini-agent.onrender.com/

# Run a query
curl -X POST https://adk-gemini-agent.onrender.com/run \
  -H "Content-Type: application/json" \
  -d '{"message": "What is machine learning?"}'

# Summarize
curl -X POST https://adk-gemini-agent.onrender.com/summarize \
  -H "Content-Type: application/json" \
  -d '{"message": "Google ADK is a framework for building AI agents..."}'

# Classify
curl -X POST https://adk-gemini-agent.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"message": "I am very happy with this product!"}'
```

---

## API Endpoints

| Method | Path         | Description              |
|--------|--------------|--------------------------|
| GET    | `/`          | Health check             |
| POST   | `/run`       | General agent query      |
| POST   | `/summarize` | Summarize text           |
| POST   | `/classify`  | Classify text            |

### Request body
```json
{ "message": "your input text here" }
```
### Response
```json
{ "response": "agent reply here", "status": "success" }
```

---

## Submission Checklist
- [ ] Render service URL is live and responding
- [ ] `/run` endpoint returns valid JSON
- [ ] GitHub repo link ready (optional but recommended)

---

## Local Testing (before deploying)
```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your_key_here"
python main.py
# Visit http://localhost:10000
```
=======
# Hack-ai
>>>>>>> fc4eb2d2deddb55b1507052aa86b44113de60d93
