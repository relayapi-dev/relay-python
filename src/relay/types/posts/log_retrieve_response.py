# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LogRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str
    """Log entry ID (post target ID)"""

    error: Optional[str] = None
    """Error message if failed"""

    platform: str
    """Platform name"""

    platform_post_id: Optional[str] = None
    """Platform post ID"""

    platform_url: Optional[str] = None
    """Published URL"""

    post_id: str
    """Post ID"""

    published_at: Optional[datetime] = None
    """Published timestamp"""

    social_account_id: str
    """Social account ID"""

    status: str
    """Target status"""

    updated_at: datetime
    """Last updated"""


class LogRetrieveResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
