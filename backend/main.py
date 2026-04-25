from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.services.mpf_calculator import calculate_mpf, PayrollInput
from fastapi.middleware.cors import CORSMiddleware
from app.core.security import require_api_key

app = FastAPI(title="MPFGuard HK MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Test only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/mpf/calculate", dependencies=[Depends(require_api_key)])
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