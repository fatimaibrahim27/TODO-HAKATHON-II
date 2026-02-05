import click
from datetime import datetime
from .storage import TodoStorage
from .models import TodoItem
import sys


# Global storage instance for the CLI session
storage = TodoStorage()


@click.group()
def cli():
    """Simple CLI tool for managing todos."""
    pass


@cli.command()
@click.argument('content', nargs=-1)
@click.option('--priority', default='medium', type=click.Choice(['low', 'medium', 'high']),
              help='Priority level (low, medium, high)')
@click.option('--due', type=click.STRING, help='Due date in YYYY-MM-DD format')
def add(content, priority, due):
    """Add a new todo item."""
    content_str = ' '.join(content).strip()

    if not content_str:
        click.echo("Error: Todo content cannot be empty.")
        return

    # Parse due date if provided
    due_date = None
    if due:
        try:
            due_date = datetime.strptime(due, '%Y-%m-%d').date()
        except ValueError:
            click.echo(f"Error: Invalid date format. Please use YYYY-MM-DD format.")
            return

    # Create and add the todo
    try:
        todo = TodoItem(
            id=0,  # Will be set by storage
            content=content_str,
            priority=priority,
            due_date=due_date
        )
        todo_id = storage.add(todo)
        click.echo(f"Added todo #{todo_id}: {content_str}")
    except ValueError as e:
        click.echo(f"Error: {e}")


@cli.command()
def list():
    """List all todo items."""
    todos = storage.list_all()

    if not todos:
        click.echo("No todos found.")
        return

    click.echo("Your todos:")
    for i, todo in enumerate(todos, 1):
        status_symbol = "✓" if todo.status == "done" else "○"
        priority_symbol = {"low": "L", "medium": "M", "high": "H"}[todo.priority]

        # Format due date if present
        due_str = f" (due: {todo.due_date})" if todo.due_date else ""

        click.echo(f"{i}. [{status_symbol}] [{priority_symbol}] {todo.content}{due_str}")


@cli.command()
@click.argument('index', type=int)
@click.argument('content', nargs=-1)
def update(index, content):
    """Update a todo item by index."""
    content_str = ' '.join(content).strip()

    if not content_str:
        click.echo("Error: Todo content cannot be empty.")
        return

    # Adjust for 1-based indexing from user perspective
    index -= 1

    if storage.update(index, content=content_str):
        click.echo(f"Updated todo #{index + 1}")
    else:
        click.echo(f"Error: Todo at index {index + 1} does not exist.")


@cli.command()
@click.argument('index', type=int)
def delete(index):
    """Delete a todo item by index."""
    # Adjust for 1-based indexing from user perspective
    index -= 1

    if storage.delete(index):
        click.echo(f"Deleted todo #{index + 1}")
    else:
        click.echo(f"Error: Todo at index {index + 1} does not exist.")


@cli.command()
@click.argument('index', type=int)
def done(index):
    """Mark a todo as done by index."""
    # Adjust for 1-based indexing from user perspective
    index -= 1

    if storage.mark_done(index):
        click.echo(f"Marked todo #{index + 1} as done")
    else:
        click.echo(f"Error: Todo at index {index + 1} does not exist.")


@cli.command()
@click.argument('index', type=int)
def pending(index):
    """Mark a todo as pending by index."""
    # Adjust for 1-based indexing from user perspective
    index -= 1

    if storage.mark_pending(index):
        click.echo(f"Marked todo #{index + 1} as pending")
    else:
        click.echo(f"Error: Todo at index {index + 1} does not exist.")


if __name__ == '__main__':
    cli()