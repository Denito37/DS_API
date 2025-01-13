from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class data_struct(BaseModel):
    id: int
    name: str
    Linear: str
    data_structure: str
    Operation_complexity: List[str]

#*data
ds_info = [
        {
            "id": 0,
            "name": "Array",
            "Linear": "yes",
            "Data_structure":"array",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"constant",
                "search":"linear",
            },
        },
        {
            "id": 1,
            "name": "Vector",
            "Linear": "yes",
            "Data_structure":"dynamic array",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"constant",
                "search":"linear",
            },
        },
        {
            "id": 2,
            "name": "List",
            "Linear": "yes",
            "Data_structure":"doubly linked list",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"linear",
                "search":"linear",
            },
        },
        {
            "id": 3,
            "name": "Stack",
            "Linear": "yes",
            "Data_structure":"stack",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"constant",
                "search":"N/A",
            },
        },
        {
            "id": 4,
            "name": "Queue",
            "Linear": "yes",
            "Data_structure":"queue",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"constant",
                "search":"N/A",
            },
        },
        {
            "id": 5,
            "name": "set",
            "Linear": "no",
            "Data_structure":"binary search tree",
            "Operation_complexity":{
                "insert":"logarithmic",
                "delete":"logarithmic",
                "access":"logarithmic",
                "search":"logarithmic",
            },

        },
        {
            "id": 6,
            "name": "map",
            "Linear": "no",
            "Data_structure":"binary search tree",
            "Operation_complexity":{
                "insert":"logarithmic",
                "delete":"logarithmic",
                "access":"logarithmic",
                "search":"logarithmic",
            },
        },
        {
            "id": 7,
            "name": "Unordered_set",
            "Linear": "no",
            "Data_structure":"hash table",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"constant",
                "search":"constant",
            },
        },
        {
            "id": 8,
            "name": "Unordered_map",
            "Linear": "no",
            "Data_structure":"hash table",
            "Operation_complexity":{
                "insert":"constant",
                "delete":"constant",
                "access":"constant",
                "search":"constant",
            },
        },
    ]

#* query parameter function
@app.get("/data_structure/", response_model=data_struct)
def read_dsA():
    return ds_info

@app.get("/data_structure/{id}", response_model=data_struct)
def read_ds(id : int):
    return ds_info[id]

if __name__ == "__api__":
    uvicorn.run(app,host="0.0.0.0",port=8000)