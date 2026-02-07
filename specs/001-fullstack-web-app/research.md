# Research Document: Full-Stack Todo Web Application

## Decision: Tech Stack Selection
**Rationale**: Based on the constitution and feature requirements, the tech stack is specified as Next.js (App Router) for frontend, FastAPI for backend, and Neon PostgreSQL with SQLModel for database. This provides clean separation of concerns and meets all architectural constraints.

**Alternatives considered**:
- Django/Flask for backend: Rejected as FastAPI offers better async support and automatic API documentation
- Express.js for backend: Rejected as FastAPI with Pydantic models provides better type safety
- Traditional PostgreSQL vs Neon PostgreSQL: Neon offers serverless scalability which aligns with modern deployment needs

## Decision: Authentication Method
**Rationale**: JWT tokens with Better Auth integration will be used for authentication, meeting constitutional requirements for industry best practices. JWT tokens will be stored securely using HttpOnly cookies to prevent XSS attacks.

**Alternatives considered**:
- Session-based authentication: Rejected as JWT provides stateless authentication suitable for microservices
- OAuth only: Rejected as the requirement includes username/password registration
- Plain JWT in localStorage: Rejected due to XSS vulnerability; HttpOnly cookies are more secure

## Decision: Database ORM
**Rationale**: SQLModel will be used as the ORM to interface with Neon PostgreSQL, meeting constitutional requirements for safe database operations and preventing SQL injection through parameterized queries.

**Alternatives considered**:
- SQLAlchemy Core: Rejected as SQLModel provides better integration with FastAPI and Pydantic
- Tortoise ORM: Rejected as SQLModel has better PostgreSQL support
- Raw SQL queries: Rejected as it violates constitutional requirement for safe, parameterized operations

## Decision: Frontend Framework
**Rationale**: Next.js with App Router will be used to provide server-side rendering, static generation capabilities, and built-in routing, meeting constitutional requirements for responsive UI and performance.

**Alternatives considered**:
- React with Create React App: Rejected as Next.js provides better performance through SSR
- Remix: Rejected as Next.js has broader ecosystem and community support
- Vue/Nuxt: Rejected as constitution specifies Next.js

## Decision: Password Hashing Algorithm
**Rationale**: bcrypt will be used for password hashing, meeting constitutional requirements for authentication best practices and preventing plaintext password storage.

**Alternatives considered**:
- scrypt: Rejected as bcrypt is more widely adopted and proven secure
- Argon2: Rejected as bcrypt is sufficient for this use case and has broader support
- SHA-256 with salt: Rejected as bcrypt is purpose-built for password hashing

## Decision: API Design Pattern
**Rationale**: RESTful API design will be implemented using FastAPI with proper validation through Pydantic models, meeting constitutional requirements for backend API validation.

**Alternatives considered**:
- GraphQL: Rejected as REST is simpler to implement for basic CRUD operations
- gRPC: Rejected as REST over HTTP is more appropriate for web application
- RPC-style endpoints: Rejected as REST provides better standardization

## Decision: CORS Configuration
**Rationale**: CORS will be configured to only allow requests from the frontend domain, meeting security requirements while enabling frontend-backend communication.

**Alternatives considered**:
- Wildcard (*) CORS: Rejected as it poses security risks
- No CORS: Rejected as it would prevent frontend-backend communication

## Decision: Environment Variables Management
**Rationale**: Environment variables will be used for all secrets and configuration values, meeting constitutional requirements for secrets management.

**Alternatives considered**:
- Hardcoded values: Rejected as it violates constitutional requirements
- Configuration files: Rejected as environment variables are more secure and flexible