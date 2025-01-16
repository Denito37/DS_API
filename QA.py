from fastapi import FastAPI, Depends, HTTPException
import sqlalchemy.orm
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

class Question(Base):
    __tablename__="Questions"
    id = Column(Integer, primary_key=True, index=True)
    Question = Column(String, index=True)
    #answers = Column(Dict[str,str])
    Correct_Answer = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Question_create(BaseModel):
    Question:str
    #Answers:Dict[str,str]
    Correct_Answer:str

class Question_structure(BaseModel):
    id:int
    Question:str
    #Answers:Dict[str,str]
    Correct_Answer:str

@app.post("/Questions",response_model= Question_structure)
async def add_Question(question: Question_create, db : Session =Depends(get_db)):
    db_item = Question(**question.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/Questions",response_model= List[Question_structure])
async def get_Question(db : Session =Depends(get_db)):
    db_item = db.query(Question).all()
    return db_item


if __name__ == "__QA__":
    uvicorn.run(app, host="127.0.0.1", port=8000)