# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["GroupListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Group ID"""

    contact_count: float
    """Number of contacts"""

    created_at: datetime
    """Created timestamp"""

    name: str
    """Group name"""

    description: Optional[str] = None


class GroupListResponse(BaseModel):
    data: List[Data]
