from typing import List, Optional
from .models import TodoItem


class TodoStorage:
    """
    In-memory storage implementation for todo items
    """

    def __init__(self):
        self.todos: List[TodoItem] = []
        self.next_id = 1

    def add(self, todo_item: TodoItem) -> int:
        """
        Adds a new todo and returns its ID
        """
        todo_item.id = self.next_id
        self.todos.append(todo_item)
        todo_id = self.next_id
        self.next_id += 1
        return todo_id

    def get(self, index: int) -> Optional[TodoItem]:
        """
        Retrieves a todo by its index (0-based)
        """
        if 0 <= index < len(self.todos):
            return self.todos[index]
        return None

    def update(self, index: int, **kwargs) -> bool:
        """
        Updates a todo's properties by index
        Returns True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            todo = self.todos[index]

            # Update allowed fields
            if 'content' in kwargs:
                todo.content = kwargs['content']
            if 'status' in kwargs:
                todo.status = kwargs['status']
            if 'priority' in kwargs:
                todo.priority = kwargs['priority']
            if 'due_date' in kwargs:
                todo.due_date = kwargs['due_date']

            return True
        return False

    def delete(self, index: int) -> bool:
        """
        Removes a todo by its index
        Returns True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            self.todos.pop(index)
            # Adjust IDs after deletion to maintain sequence
            for i, todo in enumerate(self.todos):
                todo.id = i + 1
            self.next_id = len(self.todos) + 1
            return True
        return False

    def mark_done(self, index: int) -> bool:
        """
        Marks a todo as done by index
        Returns True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            self.todos[index].status = "done"
            return True
        return False

    def mark_pending(self, index: int) -> bool:
        """
        Marks a todo as pending by index
        Returns True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            self.todos[index].status = "pending"
            return True
        return False

    def list_all(self) -> List[TodoItem]:
        """
        Returns all todos
        """
        return self.todos.copy()

    def get_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """
        Retrieves a todo by its ID
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None