CI/CD and Testing Notes

This file documents how CI and deployment are configured for the StudyBuddy MVP.

Run tests locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

GitHub Actions

- The `.github/workflows/ci.yml` workflow now runs a `build` job that installs dependencies, performs a syntax check, runs `pytest`, and builds a Docker image.
- There is a `deploy` job that runs when the `build` job completes for the `main` branch. The deploy job logs into GCP, builds and pushes a Docker image to `gcr.io/<GCP_PROJECT>/studybuddy:mvp`, and deploys to Cloud Run.

Repository secrets required for automated deployment

- `GCP_SA_KEY` — JSON service account key with required Cloud Run and storage permissions.
- `GCP_PROJECT` — GCP project ID.
- `GCP_REGION` — deployment region (e.g. `us-central1`).
- `CLOUD_RUN_SERVICE` — name of the Cloud Run service to deploy (e.g. `studybuddy-mvp`).

Notes

- I cannot perform the deployment step without those secrets. After you add them to your GitHub repository settings, pushing to `main` will trigger the deploy job.
