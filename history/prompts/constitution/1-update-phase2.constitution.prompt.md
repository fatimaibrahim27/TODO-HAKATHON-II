---
id: 1
title: Update Phase2
stage: constitution
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, phase2, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

/sp.constitution

Project: Phase-2 Full-Stack Todo Application (Next.js + FastAPI + Neon)

Core principles:
- Security-first development (auth, data, APIs)
- Clear separation of concerns (frontend, backend, database, auth)
- Spec-driven & agentic workflow (no ad-hoc coding)
- Maintainability and clean architecture
- Performance without changing features

Key standards:
- All backend APIs must be validated (request/response schemas)
- Authentication must follow industry best practices
- Passwords must NEVER be stored in plain text
- JWT or session tokens must be stored in HttpOnly secure cookies
- All database operations must be safe, parameterized, and traceable
- Environment variables must be used for secrets and API keys
- Consistent naming and folder structure across the project

Architecture constraints:
- Frontend: Next.js App Router
- Backend: FastAPI REST APIs only
- Database: Neon serverless PostgreSQL
- Auth: JWT or Better Auth integration
- No direct frontend-to-database access
- Backend is the sing

## Response snapshot

Updated the constitution file to reflect the requirements for Phase 2 of the Todo Hackathon project. The key changes include:

- Overhauled the core principles to focus on security-first development, clear separation of concerns, spec-driven workflow, maintainability, and performance
- Added detailed key standards covering API validation, authentication best practices, database operations, secrets management, and code quality
- Defined specific architecture constraints for the tech stack (Next.js App Router, FastAPI, Neon PostgreSQL, JWT/Better Auth)
- Created a sync impact report documenting the changes
- Updated the version from 1.0.0 to 1.1.0 to reflect the significant changes

## Outcome

- ✅ Impact: Major overhaul of constitution to support Phase 2 full-stack web application requirements
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with new security-focused principles and architecture guidelines
- 🔁 Next prompts: Will likely need to update other templates to align with new constitution
- 🧠 Reflection: Successfully transformed constitution from CLI-focused to full-stack web application focused with strong security emphasis

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): Update other templates to align with new constitution