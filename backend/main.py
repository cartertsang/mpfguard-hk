from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.services.mpf_calculator import calculate_mpf, PayrollInput
from fastapi.middleware.cors import CORSMiddleware
from app.core.security import require_user

app = FastAPI(title="MPFGuard HK MVP")

# 簡單 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Test only, 之後要改
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/mpf/calculate")
async def api_calc_mpf(payroll: PayrollInput):
    result = calculate_mpf(payroll)
    return result

@app.get("/health")
async def health():
    return {"status": "ok", "service": "MPFGuard HK Backend"}

@app.get("/")
async def root():
    return {"message": "MPFGuard HK Backend is running!"}

print("🚀 MPFGuard HK Backend started successfully!")
