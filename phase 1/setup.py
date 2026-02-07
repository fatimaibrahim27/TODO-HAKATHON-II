from setuptools import setup, find_packages

setup(
    name="todo-app-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "todo=src.todo_app.cli:cli",
        ],
    },
    author="Todo App Developer",
    description="A simple CLI tool for managing todo items",
    python_requires=">=3.7",
)