# Tasks: Todo App CLI

**Feature**: Todo App CLI
**Branch**: 1-todo-app
**Generated**: 2026-02-05
**Based on**: specs/1-todo-app/spec.md

## Dependencies

**Story Completion Order**: All stories can be developed independently as they share the same foundational components.

**Parallel Opportunities**:
- Models and CLI foundation can be developed in parallel [P]
- Individual CLI commands can be implemented in parallel [P]

## Implementation Strategy

**MVP Scope**: Implement User Story 1 (Add and List Todos) as the minimum viable product, ensuring core functionality works before adding advanced features.

**Approach**: Bottom-up development starting with data models, then storage, then CLI interface, then individual commands.

---

## Phase 1: Setup

- [ ] T001 Create project directory structure per implementation plan
- [ ] T002 Initialize Python project with setup files
- [ ] T003 Install required dependencies (click, pytest)

## Phase 2: Foundation

- [ ] T004 [P] Create TodoItem data model in src/todo_app/models.py
- [ ] T005 [P] Create in-memory storage implementation in src/todo_app/storage.py
- [ ] T006 [P] Create CLI main module in src/todo_app/cli.py
- [ ] T007 Create utility functions in src/todo_app/utils.py

## Phase 3: User Story 1 - Add and List Todos

**Goal**: Enable users to add new todo items via CLI command and view them in a list format.

**Independent Test Criteria**: Users can successfully add a todo item using the CLI and then list all todos to verify it was stored.

- [ ] T008 [P] [US1] Implement todo add command in cli.py
- [ ] T009 [P] [US1] Implement todo list command in cli.py
- [ ] T010 [US1] Create basic tests for add/list functionality in tests/test_cli.py
- [ ] T011 [US1] Test storage of new todos in tests/test_storage.py
- [ ] T012 [US1] Test retrieval of todos in tests/test_storage.py

## Phase 4: User Story 2 - Update and Delete Todos

**Goal**: Allow users to modify or remove existing todo items.

**Independent Test Criteria**: Users can successfully update the content of a todo or delete it entirely.

- [ ] T013 [P] [US2] Implement todo update command in cli.py
- [ ] T014 [P] [US2] Implement todo delete command in cli.py
- [ ] T015 [US2] Create tests for update/delete functionality in tests/test_cli.py
- [ ] T016 [US2] Test updating todos in tests/test_storage.py
- [ ] T017 [US2] Test deleting todos in tests/test_storage.py

## Phase 5: User Story 3 - Mark Todos as Done/Pending

**Goal**: Enable users to track the completion status of their todos by marking them as done or pending.

**Independent Test Criteria**: Users can successfully mark a todo as done or pending and see the status change reflected.

- [ ] T018 [P] [US3] Implement todo done command in cli.py
- [ ] T019 [P] [US3] Implement todo pending command in cli.py
- [ ] T020 [US3] Create tests for done/pending functionality in tests/test_cli.py
- [ ] T021 [US3] Test status updates in tests/test_storage.py

## Phase 6: User Story 4 - Set Due Dates and Priority

**Goal**: Allow users to assign due dates and priority levels to their todos for better organization.

**Independent Test Criteria**: Users can successfully add todos with due dates and priority levels and see them displayed correctly.

- [ ] T022 [P] [US4] Enhance TodoItem model to support due dates and priority in models.py
- [ ] T023 [P] [US4] Update storage to handle due dates and priority in storage.py
- [ ] T024 [P] [US4] Enhance add command to accept due date and priority options in cli.py
- [ ] T025 [US4] Update list command to display due dates and priority in cli.py
- [ ] T026 [US4] Create tests for due dates and priority functionality in tests/test_cli.py

## Phase 7: Polish & Cross-Cutting Concerns

- [ ] T027 Add error handling for invalid indices and operations
- [ ] T028 Add input validation for due date format and priority values
- [ ] T029 Implement help text and usage instructions for all commands
- [ ] T030 Create README with usage instructions
- [ ] T031 Add comprehensive tests covering edge cases
- [ ] T032 Final integration testing of all features