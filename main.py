from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time

app = FastAPI()
items = [{1: "Item 1"}]

class Item(BaseModel):
    name: int
    price: int
    is_available: bool

class Dog(BaseModel):
    name: str
    breed: str
    age: int

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

@app.get("/dogs")
def get_dogs():
    request_start = time.time()
    print(f"first request {request_start}")
    result = requests.get('https://dogapi.dog/api/v1/facts?number=2').json()

    print(f"Dogs: {result}")

    return {'message': result}

@app.get("/dogs/breeds")
def get_breeds():
    second_request = timme.time()
    print(f"second request {second_request}")
    breeds = requests.get('https://dogapi.dog/api/v2/breeds?page[size]=10').json()

    return {"message": breeds}