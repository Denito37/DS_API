from fastapi import FastAPI

app = FastAPI()

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
@app.get("/data_structure/")
def read_dsA():
    return ds_info

@app.get("/data_stuctures/{id}")
def read_ds(id : int | None = None):
    if id:
        return ds_info[id]
    return ds_info