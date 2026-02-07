"""
Controller layer for the Todo CLI App
Interprets commands, updates tasks, and orchestrates operations
"""
from .storage import TaskList
from .utils import format_task_list, parse_command


class Controller:
    """
    Controller for the Todo CLI App
    Interprets commands and coordinates operations between CLI and Storage layers
    """

    def __init__(self):
        """
        Initialize the controller with a TaskList
        """
        self.task_list = TaskList()

    def process_command(self, command_line):
        """
        Process a single command line from the user

        Args:
            command_line (str): The command line entered by the user

        Returns:
            tuple: (success: bool, response: str) Result of command execution
        """
        if not command_line or not command_line.strip():
            return False, "Please enter a command. Type 'help' for available commands."

        command, args = parse_command(command_line)

        if command == "add":
            return self._handle_add(args)
        elif command == "view":
            return self._handle_view(args)
        elif command == "list":
            return self._handle_view(args)  # alias for view
        elif command == "update":
            return self._handle_update(args)
        elif command == "delete":
            return self._handle_delete(args)
        elif command == "complete":
            return self._handle_complete(args)
        elif command == "incomplete":
            return self._handle_incomplete(args)
        elif command == "done":
            return self._handle_complete(args)  # alias for complete
        elif command == "undone":
            return self._handle_incomplete(args)  # alias for incomplete
        elif command == "help":
            return self._handle_help()
        elif command == "exit" or command == "quit":
            return True, "exit"
        else:
            return False, f"Unknown command: {command}. Type 'help' for available commands."

    def _handle_add(self, args):
        """
        Handle the 'add' command

        Args:
            args (list): Arguments to the add command

        Returns:
            tuple: (success: bool, response: str)
        """
        if not args:
            return False, "Usage: add <task content>"

        content = ' '.join(args)
        try:
            task_id = self.task_list.add_task(content)
            return True, f"Added task #{task_id}: {content}"
        except ValueError as e:
            return False, f"Error: {e}"

    def _handle_view(self, args):
        """
        Handle the 'view' command

        Args:
            args (list): Arguments to the view command

        Returns:
            tuple: (success: bool, response: str)
        """
        if len(args) > 0:
            return False, "Usage: view (shows all tasks)"

        tasks = self.task_list.list_all_tasks()

        if not tasks:
            return True, "No tasks found."

        response = format_task_list(tasks)
        return True, response

    def _handle_update(self, args):
        """
        Handle the 'update' command

        Args:
            args (list): Arguments to the update command

        Returns:
            tuple: (success: bool, response: str)
        """
        if len(args) < 2:
            return False, "Usage: update <id> <new content>"

        try:
            task_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        new_content = ' '.join(args[1:])

        if self.task_list.update_task(task_id, new_content):
            return True, f"Updated task #{task_id}"
        else:
            return False, f"Task with ID #{task_id} not found."

    def _handle_delete(self, args):
        """
        Handle the 'delete' command

        Args:
            args (list): Arguments to the delete command

        Returns:
            tuple: (success: bool, response: str)
        """
        if len(args) != 1:
            return False, "Usage: delete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        if self.task_list.delete_task(task_id):
            return True, f"Deleted task #{task_id}"
        else:
            return False, f"Task with ID #{task_id} not found."

    def _handle_complete(self, args):
        """
        Handle the 'complete' command

        Args:
            args (list): Arguments to the complete command

        Returns:
            tuple: (success: bool, response: str)
        """
        if len(args) != 1:
            return False, "Usage: complete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        if self.task_list.mark_complete(task_id):
            return True, f"Marked task #{task_id} as complete"
        else:
            return False, f"Task with ID #{task_id} not found."

    def _handle_incomplete(self, args):
        """
        Handle the 'incomplete' command

        Args:
            args (list): Arguments to the incomplete command

        Returns:
            tuple: (success: bool, response: str)
        """
        if len(args) != 1:
            return False, "Usage: incomplete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        if self.task_list.mark_incomplete(task_id):
            return True, f"Marked task #{task_id} as incomplete"
        else:
            return False, f"Task with ID #{task_id} not found."

    def _handle_help(self):
        """
        Handle the 'help' command

        Returns:
            tuple: (success: bool, response: str)
        """
        help_text = """
Available commands:
  add <content>         - Add a new task
  view                  - View all tasks
  list                  - Alias for view
  update <id> <content> - Update a task's content
  delete <id>           - Delete a task
  complete <id>         - Mark a task as complete
  incomplete <id>       - Mark a task as incomplete
  done <id>             - Alias for complete
  undone <id>           - Alias for incomplete
  help                  - Show this help message
  exit or quit          - Exit the application
        """.strip()
        return True, help_text