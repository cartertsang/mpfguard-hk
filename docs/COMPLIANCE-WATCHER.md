# MPFGuard HK - COMPLIANCE-WATCHER.md
法規監控機制 (自動更新 + 客戶通知)

## Monitoring Pipeline (Celery Cron)
1. **Sources**:
   - MPFA Gazette RSS
   - IRD Updates (https://www.ird.gov.hk/eng/tax/mpf.htm)
   - HK Gazette (https://www.gld.gov.hk/egazette/)
2. **AI Diff**: Grok API compare new rules vs current engine
3. **Update**: Patch rules engine (versioned Pydantic models)
4. **Notify**: Email/Telegram all users '法規更新: RI max 升 $40k'

## Implementation
- scripts/compliance_watcher.py (hourly cron)
- Uses web_search + xAI for 'MPFA 2026 updates'
- Threshold: score >8 publish update

## Audit Trail
- Every update logged, user opt-in apply

*PDPO Compliant: No PII in watcher*
