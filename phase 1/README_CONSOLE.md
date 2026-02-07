# Todo Console App

A simple console-based todo application built with Python standard library only. This application allows you to manage your tasks directly from the command line with an interactive console interface.

## Features

- Add new todo items
- View all todos with completion status
- Update existing todo content
- Delete todos by ID
- Mark todos as complete/incomplete
- Interactive console interface

## Usage

### Running the Application

```bash
python -m src.todo_console.app
```

### Available Commands

- `add <content>` - Add a new todo
- `view` or `list` - View all todos
- `update <id> <content>` - Update a todo's content
- `delete <id>` - Delete a todo
- `complete <id>` or `done <id>` - Mark a todo as complete
- `incomplete <id>` or `undone <id>` - Mark a todo as incomplete
- `help` - Show available commands
- `exit` or `quit` - Exit the application

### Example Session

```
Welcome to the Todo Console App!
Type 'help' for available commands, or 'exit' to quit.

> add Buy groceries
Added todo #1: Buy groceries

> add Complete project proposal
Added todo #2: Complete project proposal

> view
Your todos:
[ ] 1. Buy groceries
[ ] 2. Complete project proposal

> complete 1
Marked todo #1 as complete

> view
Your todos:
[x] 1. Buy groceries
[ ] 2. Complete project proposal

> exit
Goodbye!
```

## Project Structure

```
src/
└── todo_console/
    ├── __init__.py
    ├── app.py          # Main application entry point
    ├── models.py       # TodoItem data model
    ├── storage.py      # In-memory storage implementation
    └── commands.py     # Command processing logic
```

## Development

This project strictly uses only Python standard library components as specified in the requirements.