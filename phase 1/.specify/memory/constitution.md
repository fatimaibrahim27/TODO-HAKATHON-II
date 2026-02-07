# 📝 Todo App Constitution

**Project:** Evolution of Todo App with AI & Cloud

**Core Principles:**
- **Spec-Driven Development:** Claude Code generates code; no manual coding.
- **Incremental Phases:** CLI → Web → AI → Local K8s → Cloud K8s.
- **AI-Powered Interaction:** Natural language Todo management (Phase III–V).
- **Reliability:** Testable, scalable, reproducible.

**Constraints:**
- No manual coding; refine specs until Claude Code succeeds.
- Latency <1s for AI commands.
- Full-stack: Next.js + FastAPI + SQLModel + Neon DB.
- Deployments: Docker, Helm, Minikube, DOKS.

**Success Criteria:**
- CRUD operations work correctly in all phases.
- AI chatbot correctly interprets natural language.
- Local and cloud deployments run reliably.

---

## Phase-wise Specs

### Phase I – In-Memory CLI
- Todo CRUD (`add`, `list`, `update`, `delete`)
- Mark Done/Pending
- Due dates & priority
- Input: CLI commands → Output: in-memory list

### Phase II – Web UI
- Same functionality as Phase I
- React/Next.js frontend
- REST API backend

### Phase III – AI Integration
- Natural language processing for todo commands
- Voice input/output capability
- Intent recognition for todo actions

### Phase IV – Local Kubernetes
- Containerized deployment
- Helm charts for deployment
- Minikube for local testing

### Phase V – Cloud Deployment
- Production-ready deployment
- Auto-scaling capabilities
- Monitoring and observability

## Core Principles

### I. Spec-First Development
Specifications must be written and validated before implementation begins. Every feature follows the spec → plan → tasks → implementation workflow.

### II. CLI Interface
Every functionality starts with a CLI interface for easy testing and debugging. Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced.

### IV. Incremental Delivery
Features delivered in small, testable increments following the phase progression from CLI to Cloud.

### V. Observability
Structured logging required; All operations must be traceable and monitorable.

### VI. Simplicity
Start simple, follow YAGNI principles; Complexity must be justified.

## Additional Constraints

Technology Stack:
- Frontend: Next.js
- Backend: FastAPI
- Database: SQLModel with Neon DB
- Deployment: Docker, Helm, Kubernetes

Performance Standards:
- API response time < 1s
- CLI operations < 100ms
- AI processing < 1s

## Development Workflow

1. Create feature specification using `/sp.specify`
2. Generate implementation plan using `/sp.plan`
3. Break down into tasks using `/sp.tasks`
4. Implement using `/sp.implement`
5. Test and validate
6. Create PHR record for each major change

## Governance

This constitution supersedes all other practices. All implementations must comply with these principles. Amendments require documentation and approval.

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05
