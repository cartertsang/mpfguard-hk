from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
import httpx
from pydantic import BaseModel
from app.core.config import settings

security = HTTPBearer()

class User(BaseModel):
    user_id: str
    email: str = None

async def verify_clerk_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials or credentials.scheme != "Bearer":
        raise HTTPException(status_code=401, detail="Invalid authorization")

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(settings.CLERK_JWKS_URL)
            resp.raise_for_status()
            jwks = resp.json()

        unverified_header = jwt.get_unverified_header(credentials.credentials)
        kid = unverified_header.get("kid")
        key = next((k for k in jwks["keys"] if k["kid"] == kid), None)
        
        if not key:
            raise ValueError("Key not found")

        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

        payload = jwt.decode(
            credentials.credentials,
            public_key,
            algorithms=["RS256"],
            audience=settings.CLERK_ISSUER,
            issuer=settings.CLERK_ISSUER
        )

        return User(user_id=payload.get("sub"), email=payload.get("email"))
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid Clerk token: {str(e)}")

def require_user(user: User = Depends(verify_clerk_token)):
    return user

# Backward compatibility for API key
from fastapi import Header
def get_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

def require_api_key(api_key = Depends(get_api_key)):
    return api_key
