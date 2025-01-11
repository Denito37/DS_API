from fastapi import FastAPI

app = FastAPI()

@app.get("/data_structures/")

def DS():
    return [
        {
            "name": "Array"
        },
        {
            "name": "Vector"
        },
        {
            "name": "Linked List"
        },
        {
            "name": "Stack"
        },
        {
            "name": "Queue"
        },
        {
            "name": "Ordered_set"
        },
        {
            "name": "Ordered_map"
        },
        {
            "name": "Unordered_set"
        },
        {
            "name": "Unordered_map"
        },
    ]