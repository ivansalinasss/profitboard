from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_reportes():
    return {"message": "Endpoint de reportes"}
