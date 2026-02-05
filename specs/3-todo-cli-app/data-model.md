# Data Model: Todo CLI App

**Feature**: Todo CLI App (specs/3-todo-cli-app/spec.md)
**Created**: 2026-02-05

## TodoTask Entity

**Description**: Represents a single task with ID, content, and completion status

**Attributes**:
- `id` (int): Unique identifier for the task
- `content` (str): The task description/content
- `completed` (bool): Status indicator - False (incomplete) or True (complete)

**Validation Rules**:
- Content must not be empty or whitespace only
- ID must be a positive integer
- Completed must be a boolean value

## TaskList Entity

**Description**: Collection of TodoTask objects managed in memory

**Attributes**:
- `tasks` (list/dict): Internal storage of task objects
- `next_id` (int): Counter for generating unique IDs

**Operations**:
- `add_task(content: str) -> int`: Adds a new task and returns its ID
- `get_task(task_id: int) -> TodoTask or None`: Retrieves a task by ID
- `update_task(task_id: int, new_content: str) -> bool`: Updates task content
- `delete_task(task_id: int) -> bool`: Removes a task by ID
- `mark_complete(task_id: int) -> bool`: Marks a task as complete
- `mark_incomplete(task_id: int) -> bool`: Marks a task as incomplete
- `list_all_tasks() -> list`: Returns all tasks
- `get_next_id() -> int`: Returns the next available ID