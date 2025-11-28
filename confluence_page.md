Confluence - Project Overview (copy into Confluence page)

Title: StudyBuddy — Project Overview

Summary:
StudyBuddy unifies scheduling, collaboration, and progress tracking for college students. It helps reduce fragmentation between tools and promotes accountability through shared study sessions and progress visualizations.

Proposal:
See the attached `proposal.md` file for the full 150–200 word proposal.

Technology Decisions & Reasoning:
- Frontend: React — widely used, component-driven, good ecosystem for charts and realtime UI.
- Backend: Node.js + Express — fast prototyping and strong NPM ecosystem for auth, WebSocket, and API tooling.
- Database: MongoDB — flexible document model for schedules, messages, and user preferences.
- Deployment: Docker on Google Cloud — container-based deployments replicate local dev environment and scale easily.
- CI/CD: GitHub Actions — integrates with GitHub repo for automated tests and deploys.

Project Plan & Links:
- Jira project: (paste your public Jira URL here)
- Confluence: (paste this Confluence page URL here once published)
- GitHub repo: (paste your repo URL here)

Development Workflow:
- Feature branches named `feat/<ticket-number>-short-desc`.
- Pull requests must reference Jira ticket and include screenshots or test details.

Documentation Strategy:
- Keep `README.md` as the repo landing page; expand Confluence for design decisions and meeting notes.

Acceptance Criteria & MVP:
- Document each user story acceptance criteria in Jira. MVP includes schedule creation, basic chat, and progress dashboard.
