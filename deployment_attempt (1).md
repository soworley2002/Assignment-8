Deployment attempt notes (Google Cloud)

This file documents a manual attempt to deploy the StudyBuddy MVP to Google Cloud (Cloud Run or GKE). The deployment may be broken — include this file in the repo as evidence of the attempt.

Steps (Cloud Run, example):

1. Build the Docker image locally:

```bash
docker build -t gcr.io/PROJECT_ID/studybuddy:mvp .
```

2. (Optional) Test locally:

```bash
docker run -p 8080:8080 gcr.io/PROJECT_ID/studybuddy:mvp
# open http://localhost:8080
```

3. Push to Google Container Registry (GCR) or Artifact Registry:

```bash
# Configure gcloud
gcloud auth configure-docker
docker tag gcr.io/PROJECT_ID/studybuddy:mvp gcr.io/PROJECT_ID/studybuddy:mvp
docker push gcr.io/PROJECT_ID/studybuddy:mvp
```

4. Deploy to Cloud Run (example):

```bash
gcloud run deploy studybuddy-mvp \
  --image gcr.io/PROJECT_ID/studybuddy:mvp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

Deployed URL (placeholder):

https://(paste-your-cloud-run-url-here)

Notes:
- Replace `PROJECT_ID` with your GCP project.
- This repo contains `Dockerfile` and instructions; CI is not configured to push images to GCR.
