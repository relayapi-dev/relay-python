# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Webhook ID"""

    created_at: datetime
    """Creation timestamp"""

    enabled: bool
    """Whether the webhook is active"""

    events: List[str]
    """Subscribed events"""

    updated_at: datetime
    """Last update timestamp"""

    url: str
    """Endpoint URL"""


class WebhookListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more items exist"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""
