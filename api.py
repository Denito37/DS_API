from fastapi import FastAPI

app = FastAPI()

@app.get("/data_structures")
def DS_info():
    return [
        {
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