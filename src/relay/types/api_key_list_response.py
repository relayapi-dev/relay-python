# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKeyListResponse", "Data"]


class Data(BaseModel):
    id: str
    """API key ID"""

    created_at: datetime
    """Creation timestamp"""

    enabled: bool
    """Whether the key is active"""

    expires_at: Optional[datetime] = None
    """Expiration timestamp"""

    name: Optional[str] = None
    """API key name"""

    prefix: Optional[str] = None
    """Key prefix (e.g. rlay*live*)"""

    start: str
    """First 8 characters of the key (preview)"""


class APIKeyListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more items exist"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""
