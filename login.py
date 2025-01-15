from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Union, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
