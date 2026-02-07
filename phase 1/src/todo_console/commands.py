"""
Command processing for the Todo Console App
Handles all user commands using only Python standard library
"""
from .storage import TodoList


class CommandProcessor:
    """
    Processes user commands for the Todo Console App
    """

    def __init__(self):
        """
        Initialize the command processor with a TodoList
        """
        self.todo_list = TodoList()

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

        parts = command_line.strip().split()
        command = parts[0].lower()
        args = parts[1:]

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
            return False, "Usage: add <todo content>"

        content = ' '.join(args)
        try:
            todo_id = self.todo_list.add(content)
            return True, f"Added todo #{todo_id}: {content}"
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
            return False, "Usage: view (shows all todos)"

        todos = self.todo_list.list_all()

        if not todos:
            return True, "No todos found."

        response_lines = ["Your todos:"]
        for todo in todos:
            response_lines.append(str(todo))
        return True, '\n'.join(response_lines)

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
            todo_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        new_content = ' '.join(args[1:])

        if self.todo_list.update(todo_id, new_content):
            return True, f"Updated todo #{todo_id}"
        else:
            return False, f"Todo with ID #{todo_id} not found."

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
            todo_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        if self.todo_list.delete(todo_id):
            return True, f"Deleted todo #{todo_id}"
        else:
            return False, f"Todo with ID #{todo_id} not found."

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
            todo_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        if self.todo_list.mark_complete(todo_id):
            return True, f"Marked todo #{todo_id} as complete"
        else:
            return False, f"Todo with ID #{todo_id} not found."

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
            todo_id = int(args[0])
        except ValueError:
            return False, f"Invalid ID: {args[0]}. ID must be a number."

        if self.todo_list.mark_incomplete(todo_id):
            return True, f"Marked todo #{todo_id} as incomplete"
        else:
            return False, f"Todo with ID #{todo_id} not found."

    def _handle_help(self):
        """
        Handle the 'help' command

        Returns:
            tuple: (success: bool, response: str)
        """
        help_text = """
Available commands:
  add <content>         - Add a new todo
  view                  - View all todos
  list                  - Alias for view
  update <id> <content> - Update a todo's content
  delete <id>           - Delete a todo
  complete <id>         - Mark a todo as complete
  incomplete <id>       - Mark a todo as incomplete
  done <id>             - Alias for complete
  undone <id>           - Alias for incomplete
  help                  - Show this help message
  exit or quit          - Exit the application
        """.strip()
        return True, help_text