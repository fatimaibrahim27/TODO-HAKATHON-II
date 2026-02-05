# Quickstart Guide: Todo Console App

**Feature**: Todo Console App (specs/2-todo-console-app/spec.md)
**Created**: 2026-02-05

## Setup

1. Ensure Python 3.13+ is installed
2. Run the application: `python -m src.todo_console.app`

## Basic Commands

### Add a new todo
```
add Buy groceries
```

### View all todos
```
view
```

### Update a todo
```
update 1 Buy weekly groceries
```

### Mark a todo as complete
```
complete 1
```

### Mark a todo as incomplete
```
incomplete 1
```

### Delete a todo
```
delete 1
```

## Example Usage Session

```
Welcome to the Todo Console App!

> add Complete project proposal
Added todo #1: Complete project proposal

> add Schedule team meeting
Added todo #2: Schedule team meeting

> view
1. [ ] Complete project proposal
2. [ ] Schedule team meeting

> complete 1
Marked todo #1 as complete

> view
1. [x] Complete project proposal
2. [ ] Schedule team meeting

> update 2 Schedule project team meeting
Updated todo #2

> delete 2
Deleted todo #2

> view
1. [x] Complete project proposal

> exit
Goodbye!
```

## Help

Type `help` at any time to see available commands.