# Todo CLI App

A command-line interface application for managing todo tasks built with a clean 4-layer architecture. This application provides a simple way to manage your tasks directly from the terminal.

## Features

- Add new tasks
- View all tasks with their completion status
- Update existing task content
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Clean, intuitive command-line interface

## Architecture

The application follows a 4-layer architecture:
- **CLI Layer** (`main.py`): Handles user input/output and presents information
- **Controller Layer** (`controller.py`): Interprets commands, orchestrates operations
- **Storage Layer** (`storage.py`): Manages in-memory task storage and retrieval
- **Utils Layer** (`utils.py`): Provides validation and helper functions

## Usage

### Running the Application

```bash
python -m src.todo_cli_app.main
```

### Available Commands

- `add <content>` - Add a new task
- `view` or `list` - View all tasks
- `update <id> <content>` - Update a task's content
- `delete <id>` - Delete a task
- `complete <id>` or `done <id>` - Mark a task as complete
- `incomplete <id>` or `undone <id>` - Mark a task as incomplete
- `help` - Show available commands
- `exit` or `quit` - Exit the application

### Example Session

```
Welcome to the Todo CLI App!
Enter commands (type 'help' for options, 'exit' to quit).

> add Complete project proposal
Added task #1: Complete project proposal

> add Schedule team meeting
Added task #2: Schedule team meeting

> view
Tasks:
[ ] 1. Complete project proposal
[ ] 2. Schedule team meeting

> complete 1
Marked task #1 as complete

> view
Tasks:
[x] 1. Complete project proposal
[ ] 2. Schedule team meeting

> update 2 Schedule project team meeting
Updated task #2

> delete 2
Deleted task #2

> view
Tasks:
[x] 1. Complete project proposal

> exit
Goodbye!
```

## Project Structure

```
src/
└── todo_cli_app/
    ├── __init__.py
    ├── main.py          # CLI Layer (handles user input/output)
    ├── controller.py    # Controller Layer (interprets commands, orchestrates operations)
    ├── storage.py       # Storage Layer (manages in-memory task storage)
    └── utils.py         # Utils Layer (validation and helper functions)
```

## Development

This project uses only Python standard library components as specified in the requirements, following the clean 4-layer architecture pattern for separation of concerns.