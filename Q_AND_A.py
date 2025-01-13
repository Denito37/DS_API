from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Union, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Question_structure(BaseModel):
    id:int
    Question:str
    Answers:Dict[str,str]
    Correct_Answer:str

@app.post("/Questions")
def add_Question(Question: Question_structure):
    return Question
