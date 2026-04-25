# MPFGuard HK - AGENTS.md
香港強積金 (MPF) + 報稅自動化 SaaS 核心知識庫 (2026 年 4 月最新)

## 核心業務邏輯 & 法規規則 (Compliance-First)

### MPF 計算規則 (Relevant Income 2026)
- **最低相關入息 (Minimum Relevant Income)**: $7,100 / 月 (僱主 5%, 僱員 0%)
- **標準範圍**: $7,100 - $30,000 (雙方各 5%)
- **最高相關入息 (Max Relevant Income)**: $30,000 / 月 (雙方各上限 $1,500)
- **即將更新 (MPFA review 中)**: 準備升至最低 $10,500, 最高 $40,000 – 系統自動適配 via Compliance Watcher
- **Edge Cases 完整支援** (解決變動多痛點):
  - 加班/佣金/獎金: 計入 Relevant Income (扣除無薪假後)
  - 無薪假/扣薪: 按實際工作日比例調整 (60-day rule for casual employees)
  - Back pay / 補薪: 分攤至相關月份重新計算
  - Cessation of employment: 最終月 proration + offset 機制
  - LSP/SP 過渡 (2025/5/1 新舊制度): 自動偵測並切換計算

### eMPF 格式 (官方 XML/CSV Bulk Upload)
- **CSV Schema**: Employer ID, Employee ID, RI (Relevant Income), EE Contrib, ER Contrib, Month/Year
- **XML Schema**: MPFA 官方 XSD (sandbox API 準備)
- **自動生成**: 每月 10 號前提醒 + one-click export

### 報稅規則 (IRD 2026)
- **IR56B (僱員)**: MPF 供款證明, 薪金總額, 扣稅優化建議
- **IR56E/F/G**: 多僱主 / 自僱 / 佣金處理
- **iXBRL Profits Tax**: SME 利得稅自動填充
- **扣稅優化**: 強制性 (全扣稅) vs 自願性 (限 $18,000 / 年), 自動建議但需 user approval

### 痛點對應功能 (SME 真實需求)
1. **資料零散**: Smart Data Aggregator (OCR PDF/Excel/銀行 statement → 結構化 PayrollRecord)
2. **變動多**: Variable Pay Calculator (自動 prorate 加班/無薪假)
3. **時限緊**: Deadline Engine (每月 10 號 MPF, 4 月稅季 countdown + Telegram push)
4. **法規更新**: Compliance Watcher (RSS Gazette/MPFA/IRD + AI diff + user notify)
5. **扣稅混淆**: Tax Optimizer (interactive wizard + disclaimer: '建議僅供參考, 請咨詢專業人士')
6. **罰款風險**: Full Audit Trail (immutable log, every calc/export 記錄 versioned)

## PDPO 6 大原則實作 (數據私隱條例)
1. **目的限制**: 僅用於 MPF/報稅, user consent on upload
2. **資料準確性**: OCR + manual correction + validation (Zod/SQLAlchemy)
3. **保留期限**: Auto-delete after 7 年 (IRD/MPFA 要求)
4. **資料安全**: Row Level Security (RLS), column encryption (pgcrypto), Clerk auth
5. **資料存取權**: User dashboard export personal data
6. **不遵守後果**: Non-compliance alert + auto-pause account

## Calculation Formulas (精準 Python impl)
```
relevant_income = min(max(0, gross_salary - unpaid_leave_adjust), 30000)
ee_contrib = 0 if relevant_income &lt; 7100 else min(relevant_income * 0.05, 1500)
er_contrib = min(relevant_income * 0.05, 1500)
```
- Full code in services/mpf_calculator.py

*Disclaimer: 本系統基於公開法規, 非法律意見. 錯漏責任自負. 建議咨詢註冊會計師.*
