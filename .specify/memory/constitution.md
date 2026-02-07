<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: Complete overhaul to focus on security-first development and full-stack web application
- Added sections: Core principles, Key standards, Architecture constraints specific to Phase 2
- Removed sections: Previous phase specs (I-V), old constraints
- Templates requiring updates: ✅ Updated based on new security-focused requirements
- Follow-up TODOs: None
-->
# 📝 Todo App Constitution

**Project:** Phase-2 Full-Stack Todo Application (Next.js + FastAPI + Neon)

## Core Principles

### I. Security-First Development
All development must prioritize security considerations from the outset. Authentication, data protection, and API security are foundational requirements, not afterthoughts. All user data must be encrypted in transit and at rest. Authentication must follow industry best practices with secure session management.

### II. Clear Separation of Concerns
Frontend, backend, database, and authentication layers must be cleanly separated with well-defined interfaces. Each layer should have distinct responsibilities and minimal coupling. This enables independent development, testing, and maintenance of each component.

### III. Spec-Driven & Agentic Workflow
Development follows a spec-driven approach with automated agents handling implementation. No ad-hoc coding is allowed - all changes must originate from validated specifications. Use the spec → plan → tasks → implementation workflow consistently.

### IV. Maintainability and Clean Architecture
Code must be written with long-term maintainability in mind. Follow clean architecture principles with consistent patterns, proper documentation, and well-organized code structure. Naming conventions and folder structures must be consistent across the project.

### V. Performance without Changing Features
Optimizations and performance improvements should enhance speed and efficiency without altering existing functionality. Performance standards must be met while preserving all existing features and user experience.

## Key Standards

### Backend API Validation
All backend APIs must have validated request/response schemas using Pydantic models. Input validation and sanitization are mandatory for all endpoints. Proper HTTP status codes must be returned for all responses.

### Authentication Best Practices
Authentication must follow industry best practices. Passwords must NEVER be stored in plain text. Use bcrypt or similar for password hashing. JWT or session tokens must be stored in HttpOnly secure cookies to prevent XSS attacks.

### Database Operations
All database operations must be safe, parameterized, and traceable. Use prepared statements or ORM methods to prevent SQL injection. Database connections must be properly managed with appropriate connection pooling and error handling.

### Secrets Management
Environment variables must be used for secrets and API keys. No hardcoded credentials in source code. Secrets must be stored securely and accessed through configuration management.

### Code Quality and Consistency
Maintain consistent naming conventions and folder structure across the project. Code must follow established style guides for each technology stack. Proper error handling and logging must be implemented throughout.

## Architecture Constraints

### Frontend: Next.js App Router
- Use Next.js App Router for routing and layout management
- Implement proper error boundaries and loading states
- Follow Next.js best practices for performance optimization
- Use TypeScript for type safety

### Backend: FastAPI REST APIs only
- Build RESTful APIs using FastAPI with proper validation
- Implement authentication middleware for protected endpoints
- Use Pydantic models for request/response validation
- Include comprehensive API documentation

### Database: Neon Serverless PostgreSQL
- Leverage Neon's serverless PostgreSQL for scalability
- Use SQLModel for database modeling and ORM operations
- Implement proper migration strategies
- Optimize queries for performance

### Authentication: JWT or Better Auth integration
- Implement secure authentication using JWT tokens or Better Auth
- Use secure storage for tokens (HttpOnly cookies)
- Implement proper token expiration and refresh mechanisms
- Enforce role-based access control where applicable

### Security: No Direct Frontend-to-Database Access
- All database access must go through backend APIs
- Backend serves as the single source of truth
- Implement proper authorization checks on all endpoints
- Protect against common web vulnerabilities (XSS, CSRF, etc.)

### Backend as Single Source of Truth
- Backend manages all business logic and data validation
- Frontend is responsible for presentation and user interaction
- APIs serve as the contract between frontend and backend
- Maintain consistent data formats and validation rules

## Development Workflow

1. Create feature specification using `/sp.specify`
2. Generate implementation plan using `/sp.plan`
3. Break down into tasks using `/sp.tasks`
4. Implement using `/sp.implement`
5. Test and validate
6. Create PHR record for each major change

## Governance

This constitution supersedes all other practices. All implementations must comply with these principles. Amendments require documentation and approval.

**Version**: 1.1.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-06
