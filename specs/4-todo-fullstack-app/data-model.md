# Data Model: Todo Full-Stack App

**Feature**: Todo Full-Stack App (specs/4-todo-fullstack-app/spec.md)
**Created**: 2026-02-06

## User Entity

**Description**: Represents an authenticated user with credentials and authentication data

**Database Fields**:
- `id` (UUID): Unique identifier for the user
- `email` (String): User's email address (unique, indexed)
- `hashed_password` (String): BCrypt hashed password (not stored in plaintext)
- `created_at` (DateTime): Timestamp when user was created
- `updated_at` (DateTime): Timestamp when user was last updated
- `is_active` (Boolean): Whether the user account is active (default: True)

**Relationships**:
- One-to-Many: User has many Todos

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Password must meet security requirements (min length, complexity)

## Todo Entity

**Description**: Represents a user's todo item with content, status, and metadata

**Database Fields**:
- `id` (UUID): Unique identifier for the todo
- `title` (String): Title/content of the todo item
- `description` (Text, optional): Detailed description of the todo
- `is_completed` (Boolean): Completion status (default: False)
- `created_at` (DateTime): Timestamp when todo was created
- `updated_at` (DateTime): Timestamp when todo was last updated
- `user_id` (UUID): Foreign key linking to the owning user
- `due_date` (DateTime, optional): Optional deadline for the todo

**Relationships**:
- Many-to-One: Todo belongs to one User

**Validation Rules**:
- Title must not be empty
- User_id must reference an existing, active user
- Due date must be in the future (if provided)

## Token Entity (for session management)

**Description**: Stores authentication tokens for user sessions

**Database Fields**:
- `id` (UUID): Unique identifier for the token
- `token` (String): JWT token value (indexed for lookup)
- `user_id` (UUID): Foreign key linking to the user
- `expires_at` (DateTime): Expiration timestamp
- `is_revoked` (Boolean): Whether the token has been revoked
- `created_at` (DateTime): Timestamp when token was created

**Relationships**:
- Many-to-One: Token belongs to one User

**Validation Rules**:
- Token must be unique
- Expires_at must be in the future
- User must be active when token is created