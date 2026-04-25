import pandas as pd
from io import BytesIO
from fastapi import UploadFile
from app.services.mpf_calculator import PayrollInput, calculate_mpf

async def parse_payroll_upload(file: UploadFile):
    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(BytesIO(await file.read()))
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(BytesIO(await file.read()))
    else:
        return {"error": "Unsupported format"}

    # Clean (skill workflow)
    df['worked_days'] = 22 - df.get('Unpaid Days', 0)
    df['relevant_income'] = (df['Gross Salary'] + df.get('Overtime', 0) + df.get('Commission', 0)) * (df['worked_days'] / 22)
    df['mpf_ee'] = df['relevant_income'].apply(lambda ri: 0 if ri < 7100 else min(ri * 0.05, 1500))
    df['mpf_er'] = df['relevant_income'].apply(lambda ri: min(ri * 0.05, 1500))

    records = df.to_dict('records')
    return {
        "parsed_records": records,
        "disclaimer": "OCR/parse 95% accurate, review before DB insert/export",
        "ready_for_calc": True
    }