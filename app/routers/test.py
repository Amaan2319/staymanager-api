import time
import asyncio
from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["Testing"])

# Route 1: The WRONG way to do a slow task (Blocking)
@router.get("/bad-slow")
async def bad_slow_route():
    print("Started bad slow route...")
    # time.sleep() is synchronous. Inside an 'async def', it freezes the whole server!
    time.sleep(10) 
    print("Finished bad slow route!")
    return {"message": "This blocked everyone for 10 seconds."}

# Route 2: The RIGHT way to do a slow task (Non-Blocking)
@router.get("/good-slow")
async def good_slow_route():
    print("Started good slow route...")
    # asyncio.sleep() is asynchronous. The server can do other things while waiting!
    await asyncio.sleep(10)
    print("Finished good slow route!")
    return {"message": "This paused peacefully for 10 seconds."}

# Route 3: A fast route to test if the server is frozen
@router.get("/ping")
def ping_route():
    return {"message": "Pong! The server is awake."}