# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MediaRetrieveResponse"]


class MediaRetrieveResponse(BaseModel):
    id: str
    """Media ID"""

    created_at: datetime
    """Upload timestamp"""

    filename: str
    """Original filename"""

    mime_type: str
    """MIME type"""

    size: int
    """File size in bytes"""

    url: Optional[str] = None
    """Public URL"""

    duration: Optional[int] = None
    """Duration in seconds (video/audio)"""

    height: Optional[int] = None
    """Height in pixels"""

    width: Optional[int] = None
    """Width in pixels"""
