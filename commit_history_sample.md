Sample Commit History (examples demonstrating branch/PR usage)

- feat/1-initial-proposal: Add `proposal.md`, initial project README and planning notes
- feat/2-add-jira-confluence-samples: Add `jira_sample.md` and `confluence_page.md` content
- feat/3-flask-mvp: Add `app.py` minimal Flask MVP and `requirements.txt`
- chore/docker: Add `Dockerfile` and local run instructions
- ci/add-ci-workflow: Add `.github/workflows/ci.yml` to validate syntax and build Docker image
- docs/deployment-notes: Add `deployment_attempt.md` and deployment notes

Each feature was developed on a feature branch and merged via pull request referencing the related Jira ticket (e.g. `PR #12 -> feat/3-flask-mvp`).

Tips:
- Keep commit messages short and imperative: "Add", "Fix", "Update".
- Link PRs to Jira tickets in the PR description.
