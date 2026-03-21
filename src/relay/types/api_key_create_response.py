# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseModel):
    id: str
    """API key ID"""

    created_at: datetime
    """Creation timestamp"""

    expires_at: Optional[datetime] = None
    """Expiration timestamp"""

    key: str
    """Full API key (shown once, store securely)"""

    name: Optional[str] = None
    """API key name"""

    prefix: str
    """Key prefix"""
