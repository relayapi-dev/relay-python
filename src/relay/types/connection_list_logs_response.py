# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionListLogsResponse", "Data"]


class Data(BaseModel):
    id: str
    """Log entry ID"""

    account_id: Optional[str] = None
    """Social account ID"""

    created_at: datetime
    """Timestamp"""

    event: Literal["connected", "disconnected", "token_refreshed", "error"]
    """Event type"""

    message: Optional[str] = None
    """Event details"""

    platform: str
    """Platform name"""


class ConnectionListLogsResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
