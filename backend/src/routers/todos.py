from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
import uuid

from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..models.user import User
from ..schemas import TodoRead, TodoCreate as TodoCreateSchema, TodoUpdate as TodoUpdateSchema
from ..database import get_session
from ..auth import get_current_user

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=List[TodoRead])
def read_todos(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get all todos for the current user."""

    statement = select(Todo).where(Todo.user_id == current_user.id).offset(skip).limit(limit)
    todos = session.exec(statement).all()
    return todos


@router.post("/", response_model=TodoRead)
def create_todo(
    todo: TodoCreateSchema,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new todo for the current user."""

    db_todo = Todo.from_orm(todo) if hasattr(Todo, 'from_orm') else Todo.model_validate(todo)
    db_todo.user_id = current_user.id

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get a specific todo by ID."""

    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return db_todo


@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: uuid.UUID,
    todo: TodoUpdateSchema,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update a specific todo by ID."""

    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update fields that are provided
    update_data = todo.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.patch("/{todo_id}/complete", response_model=TodoRead)
def update_todo_completion(
    todo_id: uuid.UUID,
    is_completed: bool,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update the completion status of a specific todo."""

    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_todo.is_completed = is_completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Delete a specific todo by ID."""

    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(db_todo)
    session.commit()
    return {"message": "Todo deleted successfully"}