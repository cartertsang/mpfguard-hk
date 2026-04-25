from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Sync for Alembic/migrations
sync_engine = create_async_engine(settings.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql://"), echo=True)
SyncSessionLocal = sessionmaker(sync_engine)

# Async for runtime
engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session