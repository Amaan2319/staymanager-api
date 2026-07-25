from fastapi import APIRouter
from app.schemas.hostel import HostelType,Hostel

router = APIRouter(prefix="/hostel")

@router.get("/all")
def get_all_hostels():
    return "No hostels as of now"

@router.post("/add")
def add_hostel(hostel: Hostel):
    return {"message": f"Hostel added {hostel}"}