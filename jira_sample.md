Jira Project - Sample Epics, User Stories & Subtasks

Epics:
1) User Management
   - US1: As a registered user, I want to sign up and log in so that I can access my personal study space.
     - Subtasks: Design auth API, Implement signup endpoint, Implement login + JWT, Add frontend forms, Write tests
     - Acceptance Criteria: Users can register and receive a confirmation; login returns a valid JWT.
   - US2: As a user, I want to edit my profile so that I can update availability and preferences.
     - Subtasks: Profile schema, API endpoint, Frontend profile page, Unit tests

2) Core Features
   - US3: As a student, I want to create shared study sessions so that I can coordinate with peers.
     - Subtasks: Session model, CRUD API, Invite link generation, Frontend session UI, Tests
   - US4: As a group member, I want a real-time chat so that we can communicate during sessions.
     - Subtasks: Integrate WebSocket/Socket.io, Chat DB model, Frontend chat component, Tests
   - US5: As a student, I want a progress dashboard so I can see completed tasks and goals.
     - Subtasks: Dashboard API, Visual components (charts), Backend aggregation, Tests

3) AI Integration
   - US6: As a user, I want automated study-plan suggestions so that I can quickly create an effective schedule.
     - Subtasks: Design prompt format, Integrate AI API, Endpoint + caching, Frontend suggestions panel, Tests
   - US7: As a user, I want chat summarization so that I can quickly review discussion highlights.
     - Subtasks: Summarization endpoint, Hook into chat events, Frontend summary UI, Tests

Sprint Planning (suggested):
- Sprint 1 (MVP): US1, US3, US4 (basic chat), US5 minimal dashboard
- Sprint 2 (complete app): remaining features including AI integration, UX polish, notifications

Notes: For each Jira user story, add 3–6 subtasks representing UI, API, DB, tests, and docs. Attach acceptance criteria to each story before moving it to Done.
