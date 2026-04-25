# MPFGuard HK - MEMORY.md
2026 MPF 參數 + 常見痛點解決方案

## 2026 MPF Parameters
| Param | Value | Notes |
|-------|-------|-------|
| Min RI | $7,100 | Employee 0% |
| Max RI | $30,000 | $1,500 cap |
| Upcoming | $10,500/$40,000 | Auto-update ready |
| MPF Deadline | Monthly 10th | + Penalty 5% |
| Tax Season | May 2 (IR56B) | e-filing |

## eMPF Official Formats
- CSV: 'EmployerID,EmployeeID,YearMonth,RI,EEContrib,ERContrib'
- XML: MPFA XSD v2.3 (sandbox: https://empf.mpfa.org.hk)

## IRD Taxonomy (iXBRL)
- Profits Tax: HKFRS aligned
- IR56B: Box 10.1 MPF contrib proof

## 痛點 & 解決方案
1. **零散資料**: OCR (Grok Vision/Unstructured) + pandas clean → PayrollRecord
2. **變動計算**: Prorate formula: RI = gross * (worked_days / total_days)
3. **稅季 Chaos**: Celery cron reminders, Telegram webhook
4. **法規跟唔切**: RSS watcher + Grok diff rules engine
5. **一人公司**: Suggest voluntary $18k for max deduction
