from pydantic import BaseModel
from app.core.config import settings

class PayrollInput(BaseModel):
    gross_salary: float = 0.0
    overtime: float = 0.0
    commission: float = 0.0
    unpaid_days: float = 0.0
    worked_days: float = 22.0

def calculate_mpf(payroll: PayrollInput) -> dict:
    ri_adjust = payroll.gross_salary + payroll.overtime + payroll.commission
    ri_adjust *= (payroll.worked_days / 22.0)
    relevant_income = min(max(0, ri_adjust), settings.MPF_MAX_RI)
    er_contrib = min(relevant_income * settings.MPF_RATE, settings.MPF_CAP)
    ee_contrib = 0 if relevant_income < settings.MPF_MIN_RI else min(relevant_income * settings.MPF_RATE, settings.MPF_CAP)
    return {
        "relevant_income": round(relevant_income, 2),
        "ee_contrib": round(ee_contrib, 2),
        "er_contrib": round(er_contrib, 2),
        "disclaimer": "僅供參考 / For reference only"
    }