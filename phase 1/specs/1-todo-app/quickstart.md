# Quickstart Guide: Todo App CLI

**Feature**: Todo App CLI (specs/1-todo-app/spec.md)
**Created**: 2026-02-05

## Setup

1. Ensure Python 3.9+ is installed
2. Install dependencies: `pip install click pytest`
3. Run the application: `python -m src.todo_app.cli`

## Basic Commands

### Add a new todo
```bash
todo add "Buy groceries" --priority high --due 2026-02-10
```

### List all todos
```bash
todo list
```

### Update a todo
```bash
todo update 1 "Buy weekly groceries"
```

### Mark a todo as done
```bash
todo done 1
```

### Mark a todo as pending
```bash
todo pending 1
```

### Delete a todo
```bash
todo delete 1
```

## Example Usage Session

```bash
# Add some todos
todo add "Complete project proposal" --priority high --due 2026-02-08
todo add "Schedule team meeting" --priority medium
todo add "Review code changes" --priority low --due 2026-02-07

# List todos
todo list

# Mark first todo as done
todo done 1

# Update second todo
todo update 2 "Schedule project team meeting"

# Delete the third todo
todo delete 3

# List todos again to see changes
todo list
```

## Help

Get help for any command:
```bash
todo --help
todo add --help
todo list --help
```