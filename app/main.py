from fastapi import FastAPI
from app.routers import user,payment,hostel,test



app = FastAPI(title="Stay Manager API")

# 2. Plug the router into the main app!
app.include_router(user.router)
app.include_router(payment.router)
app.include_router(hostel.router)
app.include_router(test.router)


@app.get("/")
def root():
    return {"message": "Hello World! from windows"}

