# Data Model: Full-Stack Todo Web Application

## Entity: User
- **Fields**:
  - id (UUID/Integer): Primary key, unique identifier for the user
  - email (String): Unique, required, validated email address
  - name (String): Optional, user's display name
  - hashed_password (String): Required, securely hashed password (bcrypt)
  - created_at (DateTime): Timestamp of account creation
  - updated_at (DateTime): Timestamp of last account update
  - is_active (Boolean): Flag indicating if account is active
- **Relationships**:
  - One-to-many with TodoItem (via user_id foreign key)
- **Validation rules**:
  - Email must be a valid email format
  - Password must be hashed before storage (never store plaintext)
  - Email must be unique across all users
- **State transitions**:
  - Account created (is_active = true) → Account deactivated (is_active = false)

## Entity: TodoItem
- **Fields**:
  - id (UUID/Integer): Primary key, unique identifier for the todo item
  - user_id (UUID/Integer): Foreign key linking to User entity
  - title (String): Required, title of the todo item
  - description (Text): Optional, detailed description of the todo item
  - completed (Boolean): Flag indicating completion status (default: false)
  - priority (String/Enum): Priority level (e.g., 'low', 'medium', 'high')
  - created_at (DateTime): Timestamp of todo creation
  - updated_at (DateTime): Timestamp of last update
  - due_date (DateTime): Optional, deadline for completing the task
- **Relationships**:
  - Many-to-one with User (via user_id foreign key)
- **Validation rules**:
  - User_id must reference an existing user
  - Title must not be empty
  - Priority must be one of the allowed values ('low', 'medium', 'high')
  - User can only access todo items associated with their user_id
- **State transitions**:
  - Todo created (completed = false) → Todo completed (completed = true) → Todo reopened (completed = false)

## Database Schema Relationships
- User (1) ←→ (Many) TodoItem
- User.id ↔ TodoItem.user_id (foreign key constraint)
- TodoItem.user_id is indexed for efficient querying by user

## Security Considerations
- No user should be able to access another user's TodoItems
- Authentication and authorization must be enforced at both API and database levels
- Proper foreign key constraints to maintain data integrity
- Index on user_id in TodoItem table for efficient filtering by user

## Access Patterns
- Retrieve all TodoItems for a specific User
- Create a new TodoItem associated with a specific User
- Update a TodoItem owned by a specific User
- Delete a TodoItem owned by a specific User
- Toggle completion status of a TodoItem owned by a specific User