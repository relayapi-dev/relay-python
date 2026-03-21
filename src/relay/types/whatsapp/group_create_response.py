# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["GroupCreateResponse"]


class GroupCreateResponse(BaseModel):
    id: str
    """Group ID"""

    contact_count: float
    """Number of contacts"""

    created_at: datetime
    """Created timestamp"""

    name: str
    """Group name"""

    description: Optional[str] = None
