# Data Model: Todo Console App

**Feature**: Todo Console App (specs/2-todo-console-app/spec.md)
**Created**: 2026-02-05

## TodoItem Entity

**Description**: Represents a single task with content and completion status

**Attributes**:
- `id` (int): Unique identifier for the todo item
- `content` (str): The actual todo text/content
- `completed` (bool): Current status - either False (incomplete) or True (complete)

**Validation Rules**:
- Content must not be empty or whitespace only
- ID must be a positive integer
- Completed must be a boolean value

## TodoList Entity

**Description**: Collection of TodoItem objects with management capabilities

**Attributes**:
- `todos` (list): Internal list of todo items
- `next_id` (int): Counter for generating unique IDs

**Operations**:
- `add(todo_content: str) -> int`: Adds a new todo and returns its ID
- `get(todo_id: int) -> TodoItem or None`: Retrieves a todo by its ID
- `update(todo_id: int, new_content: str) -> bool`: Updates a todo's content
- `delete(todo_id: int) -> bool`: Removes a todo by its ID
- `mark_complete(todo_id: int) -> bool`: Marks a todo as complete
- `mark_incomplete(todo_id: int) -> bool`: Marks a todo as incomplete
- `list_all() -> list`: Returns all todos
- `list_completed() -> list`: Returns completed todos
- `list_incomplete() -> list`: Returns incomplete todos