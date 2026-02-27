from typing import Optional
import os

from fastapi import Header, HTTPException


def get_api_token(authorization: Optional[str] = Header(None)):
    """Simple token check. If `UNIVERSO_API_TOKEN` is set, require `Authorization: Bearer <token>`.
    If env var is empty, allow all requests (useful for local/dev/testing).
    """
    expected = os.getenv("UNIVERSO_API_TOKEN", "")
    if not expected:
        return True
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer" or parts[1] != expected:
        raise HTTPException(status_code=401, detail="Invalid token")
    return True
