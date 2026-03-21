# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SlotUpdateResponse", "Slot"]


class Slot(BaseModel):
    day_of_week: int
    """Day of week (0=Sunday, 6=Saturday)"""

    time: str
    """Time in HH:MM format"""

    timezone: str
    """IANA timezone (e.g. America/New_York)"""


class SlotUpdateResponse(BaseModel):
    id: str
    """Queue schedule ID"""

    created_at: datetime
    """Created timestamp"""

    is_default: bool
    """Whether this is the default schedule"""

    slots: List[Slot]
    """Time slots"""

    updated_at: datetime
    """Updated timestamp"""

    name: Optional[str] = None
    """Schedule name"""
