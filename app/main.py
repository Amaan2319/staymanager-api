from fastapi import FastAPI
from app.routers import user,payment

# 1. Import your user router
from app.routers import user

app = FastAPI(title="Stay Manager API")

# 2. Plug the router into the main app!
app.include_router(user.router)
app.include_router(payment.router)


@app.get("/")
def root():
    return {"message": "Hello World!"}

