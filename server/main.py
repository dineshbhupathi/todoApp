from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.database import engine, SessionLocal
from app import crud, model, schemes, database
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles


model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/build/static", StaticFiles(directory="build/static"), name="static")



def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return FileResponse('build/index.html')


@app.get("/api/todo")
async def get_todo(db: Session = Depends(get_db)):
    todo = db.query(model.Todo).all()
    return todo


@app.post("/api/todo/")
async def post_todo(title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
    todo = schemes.Todo(
        title=title,
        description=description
    )
    return crud.create_todo(db=db, todo=todo)


@app.delete("/api/todo/{id}")
async def delete_todo(id: int):
    with Session(engine) as session:
        todo = session.get(model.Todo, id)
        if not todo:
            raise HTTPException(status_code=404, detail="todo not found")

        session.delete(todo)
        session.commit()
        return {"ok": True}
