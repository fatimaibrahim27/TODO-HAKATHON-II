# Quickstart Guide: Todo CLI App

**Feature**: Todo CLI App (specs/3-todo-cli-app/spec.md)
**Created**: 2026-02-05

## Setup

1. Ensure Python 3.13+ is installed
2. Run the application: `python -m src.todo_cli_app.main`

## Basic Commands

### Add a new task
```
add Buy groceries
```

### View all tasks
```
view
```

### Update a task
```
update 1 Buy weekly groceries
```

### Delete a task
```
delete 1
```

### Mark a task as complete
```
complete 1
```

### Mark a task as incomplete
```
incomplete 1
```

## Example Usage Session

```
Welcome to the Todo CLI App!
Enter commands (type 'help' for options, 'exit' to quit):

> add Complete project proposal
Added task #1: Complete project proposal

> add Schedule team meeting
Added task #2: Schedule team meeting

> view
Tasks:
1. [ ] Complete project proposal
2. [ ] Schedule team meeting

> complete 1
Marked task #1 as complete

> view
Tasks:
1. [x] Complete project proposal
2. [ ] Schedule team meeting

> update 2 Schedule project team meeting
Updated task #2

> delete 2
Deleted task #2

> view
Tasks:
1. [x] Complete project proposal

> exit
Goodbye!
```

## Help

Type `help` at any time to see available commands.