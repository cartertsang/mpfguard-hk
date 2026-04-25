# MVP Hardcoded Settings (no deps, prod use pydantic-settings + .env)
class Settings:
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"
    ENCRYPT_KEY = b'mpfguard_demo_key_very_secure_32_bytes_plus_padding_for_fernet_1234567890abcdef=='
    XAI_API_KEY = "demo"
    XAI_MODEL = "grok-4-1-fast-reasoning"
    MPF_MIN_RI = 7100.0
    MPF_MAX_RI = 30000.0
    MPF_RATE = 0.05
    MPF_CAP = 1500.0
    FRONTEND_URL = "http://localhost:3001"
    SUPABASE_URL = None
    SUPABASE_KEY = None

settings = Settings()