## Minimal Flask MVP (added)

A small Flask app has been added for the Unit 12 MVP. It demonstrates a minimal web UI and a health endpoint.

- App entry: `app.py`
- Run locally: see commands below

### Run locally (virtualenv)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Run with Docker

Build the image:

```bash
docker build -t studybuddy:mvp .
docker run -p 8080:8080 studybuddy:mvp
```

### CI

A lightweight GitHub Actions workflow was added at `.github/workflows/ci.yml` that checks Python syntax and builds a local Docker image (no push configured).

### Deployment

See `deployment_attempt.md` for the documented attempt to deploy to Google Cloud (Cloud Run) and the placeholder deployed URL.

### AI Tools Used

- GitHub Copilot: code and Dockerfile suggestions
- ChatGPT: writing documentation fragments and commit message examples
- Notes: document where AI was used in `confluence_mvp.md`

### Submission Checklist (placeholders)

- GitHub repo: (paste your repo URL here)
- Google Cloud deployed URL: (paste Cloud Run or GKE URL here)
- Jira project URL: (paste public Jira URL here)
- Confluence space URL: (paste public Confluence URL here)
