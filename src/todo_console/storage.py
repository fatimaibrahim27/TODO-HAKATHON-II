"""
In-memory storage for the Todo Console App
Using only Python standard library components
"""
from .models import TodoItem


class TodoList:
    """
    Collection of TodoItem objects with management capabilities
    """

    def __init__(self):
        """
        Initialize an empty TodoList
        """
        self.todos = []
        self.next_id = 1

    def add(self, todo_content):
        """
        Add a new todo and return its ID

        Args:
            todo_content (str): Content of the new todo item

        Returns:
            int: The ID of the newly created todo item
        """
        if not todo_content or not todo_content.strip():
            raise ValueError("Todo content must not be empty")

        # Create a new TodoItem with the next available ID
        new_todo = TodoItem(self.next_id, todo_content, False)
        self.todos.append(new_todo)

        # Remember the ID to return and increment next_id
        todo_id = self.next_id
        self.next_id += 1

        return todo_id

    def get(self, todo_id):
        """
        Retrieve a todo by its ID

        Args:
            todo_id (int): The ID of the todo to retrieve

        Returns:
            TodoItem or None: The todo item if found, None otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            return None

        # Find the todo with the specified ID
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update(self, todo_id, new_content):
        """
        Update a todo's content

        Args:
            todo_id (int): The ID of the todo to update
            new_content (str): The new content for the todo

        Returns:
            bool: True if the update was successful, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            return False

        if not new_content or not new_content.strip():
            return False

        # Find the todo and update its content
        for todo in self.todos:
            if todo.id == todo_id:
                todo.update_content(new_content)
                return True
        return False

    def delete(self, todo_id):
        """
        Remove a todo by its ID

        Args:
            todo_id (int): The ID of the todo to remove

        Returns:
            bool: True if the deletion was successful, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            return False

        # Find the todo and remove it
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                self.todos.pop(i)

                # Update IDs to maintain sequence
                for j in range(i, len(self.todos)):
                    self.todos[j].id = self.next_id - len(self.todos) + j

                # Update next_id to reflect the new last ID
                self.next_id = len(self.todos) + 1 if len(self.todos) > 0 else 1
                return True
        return False

    def mark_complete(self, todo_id):
        """
        Mark a todo as complete

        Args:
            todo_id (int): The ID of the todo to mark complete

        Returns:
            bool: True if the operation was successful, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            return False

        todo = self.get(todo_id)
        if todo is not None:
            todo.mark_complete()
            return True
        return False

    def mark_incomplete(self, todo_id):
        """
        Mark a todo as incomplete

        Args:
            todo_id (int): The ID of the todo to mark incomplete

        Returns:
            bool: True if the operation was successful, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            return False

        todo = self.get(todo_id)
        if todo is not None:
            todo.mark_incomplete()
            return True
        return False

    def list_all(self):
        """
        Return all todos

        Returns:
            list: A list of all TodoItem objects
        """
        return self.todos.copy()

    def list_completed(self):
        """
        Return completed todos

        Returns:
            list: A list of completed TodoItem objects
        """
        return [todo for todo in self.todos if todo.completed]

    def list_incomplete(self):
        """
        Return incomplete todos

        Returns:
            list: A list of incomplete TodoItem objects
        """
        return [todo for todo in self.todos if not todo.completed]