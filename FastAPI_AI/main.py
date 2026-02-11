from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
	return {"message":"Hello FastAPI"}


@app.get("/items/{item_id}/")
def read_item(item_id: int, q: str = "Just a query"):
	return {"item_id": item_id, "q": q}


@app.get("/search/")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
