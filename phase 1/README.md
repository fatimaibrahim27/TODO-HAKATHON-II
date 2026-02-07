# Todo App CLI

A simple command-line interface for managing todo items. This application allows you to add, list, update, delete, and track the completion status of your todos, with support for priorities and due dates.

## Features

- Add new todo items with optional priority and due date
- List all todos with status, priority, and due date indicators
- Update existing todo content
- Delete todos by index
- Mark todos as done or pending
- Priority levels: low, medium, high
- Due date tracking

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package (optional, for global command access):
   ```bash
   pip install -e .
   ```

## Usage

### Basic Commands

#### Add a new todo
```bash
python -m src.todo_app.cli add "Buy groceries"
```

#### Add a todo with priority and due date
```bash
python -m src.todo_app.cli add "Complete project proposal" --priority high --due 2026-02-10
```

#### List all todos
```bash
python -m src.todo_app.cli list
```

#### Update a todo
```bash
python -m src.todo_app.cli update 1 "Buy weekly groceries"
```

#### Mark a todo as done
```bash
python -m src.todo_app.cli done 1
```

#### Mark a todo as pending
```bash
python -m src.todo_app.cli pending 1
```

#### Delete a todo
```bash
python -m src.todo_app.cli delete 1
```

### If installed globally:
```bash
todo add "My new task"
todo list
todo done 1
```

## Examples

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

## Development

### Running Tests

```bash
pytest tests/
```

### Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── cli.py          # Main CLI entry point
│   ├── models.py       # TodoItem data model
│   ├── storage.py      # In-memory storage implementation
│   └── utils.py        # Utility functions
└── tests/
    ├── conftest.py
    ├── test_models.py
    ├── test_storage.py
    └── test_cli.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run tests to ensure everything works
6. Submit a pull request