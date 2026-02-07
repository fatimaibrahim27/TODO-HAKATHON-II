# Data Model: Todo App CLI

**Feature**: Todo App CLI (specs/1-todo-app/spec.md)
**Created**: 2026-02-05

## TodoItem Entity

**Description**: Represents a single task with content, status, priority, and optional due date

**Fields**:
- `id` (int): Unique identifier for the todo item
- `content` (str): The actual todo text/content
- `status` (str): Current status - either "pending" or "done"
- `priority` (str): Priority level - "low", "medium", or "high"
- `due_date` (datetime.date, optional): Date when the todo is due (can be None)
- `created_at` (datetime.datetime): Timestamp when the todo was created

**Validation Rules**:
- Content must not be empty or whitespace only
- Status must be either "pending" or "done"
- Priority must be one of "low", "medium", "high"
- Due date must be a valid date in the future (optional validation rule)

## TodoList Entity

**Description**: Collection of TodoItem objects with management capabilities

**Fields**:
- `todos` (list[TodoItem]): Internal list of todo items
- `next_id` (int): Counter for generating unique IDs

**Operations**:
- `add(todo_item: TodoItem) -> int`: Adds a new todo and returns its ID
- `get(index: int) -> TodoItem`: Retrieves a todo by its index
- `update(index: int, **kwargs) -> bool`: Updates a todo's properties
- `delete(index: int) -> bool`: Removes a todo by its index
- `mark_done(index: int) -> bool`: Marks a todo as done
- `mark_pending(index: int) -> bool`: Marks a todo as pending
- `list_all() -> list[TodoItem]`: Returns all todos