from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
items = [{1: "Item 1"}]

class Item(BaseModel):
    name: int
    price: int
    is_available: bool

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/items")
def get_items():
    return {"items": items}

@app.get("/item/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"message": {item_id: q}}

@app.put("/items/{item_id}")
def give_item(item_id:int, item: Item):
    return {"message": {"id": item_id, "name": item.name, "availability": item.is_available, "price": item.price}}