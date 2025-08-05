from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your first ML API!"}


@app.get("/new")
def just():
    return {"Newone": "Hello from your second ML API!"}

@app.get("/about")
def about():
    return {"info": "Learning MLOps"}
