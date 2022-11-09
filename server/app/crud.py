from sqlalchemy.orm import Session
from .model import Todo


def create_todo(db: Session, todo: Todo):
    db_todo = Todo(
        title=todo.title,
        description=todo.description

    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
