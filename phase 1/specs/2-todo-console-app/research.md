# Research: Todo Console App Implementation

**Feature**: Todo Console App (specs/2-todo-console-app/spec.md)
**Created**: 2026-02-05

## Decision: Console Input/Output Approach

**Rationale**: Using Python's built-in input() and print() functions for console interaction to comply with the constraint of using only the standard library. This provides a simple, cross-platform solution for user interaction.

**Alternatives considered**:
- readline module (available on Unix-like systems but not Windows by default)
- curses module (more complex than needed for basic console app)
- tkinter (GUI library, not console-based)

## Decision: Storage Approach

**Rationale**: For the console app, in-memory storage using Python lists and data structures is chosen to keep the implementation simple and focused on core functionality. This aligns with the requirement of using only standard library and no persistence across sessions.

**Alternatives considered**:
- File storage (would violate standard library constraint depending on format)
- Database (would require external libraries)
- In-memory dictionary/list (selected approach)

## Decision: Data Modeling

**Rationale**: Using Python classes with basic attributes for the TodoItem model to provide clean, structured code without external dependencies. Using simple data structures from the standard library.

**Alternatives considered**:
- Plain dictionaries (less structured)
- Named tuples (immutable but inflexible)
- dataclasses (requires import but still standard library)

## Decision: Command Parsing

**Rationale**: Using simple string parsing and split operations to interpret commands rather than argparse, which would be more suitable for traditional CLI programs with flags and arguments. The console app expects a different interaction model.

**Alternatives considered**:
- argparse module (better for CLI with flags, not interactive console)
- cmd module (could be used but basic string parsing sufficient for requirements)
- re module for pattern matching (overkill for basic commands)