from fastapi import FastAPI, Depends, HTTPException
import sqlalchemy.orm
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware
from json import dump

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

class Question(Base):
    __tablename__="Questions"
    id = Column(Integer, primary_key=True, index=True)
    Question = Column(String)
    Correct_Answer = Column(String)
    answers = relationship('Answers', backref='Questions')

class Answers(Base):
    __tablename__='Answers'
    id = Column(Integer, primary_key=True, index=True)
    choice_A = Column(String)
    choice_B = Column(String)
    choice_C = Column(String)
    choice_D = Column(String)
    question_id = Column(Integer, ForeignKey('Questions.id'))

Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Question_create(BaseModel):
    Question:str
    Correct_Answer:str

class Question_response(BaseModel):
    id:int
    Question:str
    Correct_Answer:str

class Answer_create(BaseModel):
    choice_A:str
    choice_B:str
    choice_C:str
    choice_D:str

class Answer_response(BaseModel):
    id:int
    choice_A:str
    choice_B:str
    choice_C:str
    choice_D:str

@app.post("/Questions",response_model= Question_response)
async def add_Question(question: Question_create, db : Session =Depends(get_db)):
    db_item = Question(**question.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.post("/Answers", response_model=Answer_response)
async def add_Answers(answer: Answer_create, db : Session = Depends(get_db)):
    db_item = Answers(**answer.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/Questions")
async def get_Question(db : Session =Depends(get_db)):
    db_item = db.query(Question, Answers).all()
    return db_item


if __name__ == "__QA__":
    uvicorn.run(app, host="127.0.0.1", port=8000)