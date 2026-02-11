---
name: database-skill
description: Manage Neon Serverless PostgreSQL operations for the Todo Full-Stack Web App, including schema design, table creation, migrations, and CRUD operations.
---

# Database Skill

## Instructions

1. **Schema Design**
   - Design tables for users and tasks
   - Include indexes for performance (e.g., tasks.user_id, tasks.completed)
   - Use foreign keys for relationships (e.g., tasks.user_id → users.id)

2. **Operations**
   - Create, read, update, delete tasks and users
   - Implement migrations for schema changes
   - Use SQLModel ORM for all database interactions
   - Ensure data integrity and consistency

3. **Security**
   - Sanitize all database inputs to prevent SQL injection
   - Use environment variables for database credentials
   - Ensure proper access control per user

4. **Performance**
   - Optimize queries for speed and efficiency
   - Avoid unnecessary joins or heavy queries
   - Use indexes and filtering for fast lookups

## Best Practices
- Always use parameterized queries
- Keep database schema normalized but practical
- Test all CRUD operations after migrations
- Use version control for schema changes

## When to Use
- Creating or updating tables
- Implementing migrations
- Performing CRUD operations for tasks and users
- Optimizing database performance
