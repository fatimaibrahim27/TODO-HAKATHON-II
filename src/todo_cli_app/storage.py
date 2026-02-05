"""
Storage layer for the Todo CLI App
Manages in-memory task storage and retrieval
"""
from .utils import TodoTask


class TaskList:
    """
    Collection of TodoTask objects managed in memory
    """

    def __init__(self):
        """
        Initialize an empty TaskList
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, content):
        """
        Add a new task and return its ID

        Args:
            content (str): Content of the new task

        Returns:
            int: The ID of the newly created task
        """
        if not content or not content.strip():
            raise ValueError("Task content must not be empty")

        # Create a new TodoTask with the next available ID
        new_task = TodoTask(self.next_id, content, False)
        self.tasks.append(new_task)

        # Remember the ID to return and increment next_id
        task_id = self.next_id
        self.next_id += 1

        return task_id

    def get_task(self, task_id):
        """
        Retrieve a task by its ID

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            TodoTask or None: The task if found, None otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return None

        # Find the task with the specified ID
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, new_content):
        """
        Update a task's content

        Args:
            task_id (int): The ID of the task to update
            new_content (str): The new content for the task

        Returns:
            bool: True if the update was successful, False otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        if not new_content or not new_content.strip():
            return False

        # Find the task and update its content
        for task in self.tasks:
            if task.id == task_id:
                task.update_content(new_content)
                return True
        return False

    def delete_task(self, task_id):
        """
        Remove a task by its ID

        Args:
            task_id (int): The ID of the task to remove

        Returns:
            bool: True if the deletion was successful, False otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        # Find the task and remove it
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)

                # Update IDs to maintain sequence
                for j in range(i, len(self.tasks)):
                    self.tasks[j].id = self.next_id - len(self.tasks) + j

                # Update next_id to reflect the new last ID
                self.next_id = len(self.tasks) + 1 if len(self.tasks) > 0 else 1
                return True
        return False

    def mark_complete(self, task_id):
        """
        Mark a task as complete

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            bool: True if the operation was successful, False otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        task = self.get_task(task_id)
        if task is not None:
            task.mark_complete()
            return True
        return False

    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete

        Args:
            task_id (int): The ID of the task to mark incomplete

        Returns:
            bool: True if the operation was successful, False otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        task = self.get_task(task_id)
        if task is not None:
            task.mark_incomplete()
            return True
        return False

    def list_all_tasks(self):
        """
        Return all tasks

        Returns:
            list: A list of all TodoTask objects
        """
        return self.tasks.copy()

    def get_next_id(self):
        """
        Get the next available ID

        Returns:
            int: The next available task ID
        """
        return self.next_id