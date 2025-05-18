from fastapi import FastAPI
from routers import reports
import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

app = FastAPI(title="Sistema de Reportes Financieros")

# Incluir el router de reportes
app.include_router(reports.router, prefix="/reportes", tags=["Reportes"])

@app.get("/")
def root():
    return {"message": "API de Reportes Financieros - FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
