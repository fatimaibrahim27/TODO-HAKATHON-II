---
name: backend-skill
description: Implement FastAPI backend for the Todo Full-Stack Web App. Generate routes, handle requests and responses, integrate with database, and enforce authentication and data validation.
---

# Backend Skill

## Instructions

1. **API Routes**
   - Create RESTful endpoints for tasks and users
   - Support GET, POST, PUT, DELETE, PATCH methods
   - Use path parameters and query parameters properly

2. **Request/Response Handling**
   - Validate incoming requests using Pydantic models
   - Structure responses consistently in JSON format
   - Handle errors gracefully with proper HTTP status codes

3. **Database Integration**
   - Connect endpoints to Neon PostgreSQL via SQLModel ORM
   - Perform CRUD operations using DB agent guidance
   - Ensure transactional integrity where needed

4. **Authentication & Security**
   - Verify JWT tokens for protected routes
   - Integrate with Better Auth for session management
   - Enforce user access control and isolation
   - Sanitize and validate all inputs

## Best Practices
- Keep code modular and maintainable
- Use dependency injection for services and DB sessions
- Follow REST conventions for endpoints
- Include logging for errors and important events

## When to Use
- Implementing new backend routes
- Handling requests and responses
- Connecting backend to database
- Securing endpoints with authentication and validation
