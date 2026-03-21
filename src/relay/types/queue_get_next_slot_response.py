# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["QueueGetNextSlotResponse"]


class QueueGetNextSlotResponse(BaseModel):
    next_slot_at: datetime
    """Next available slot (ISO 8601)"""

    queue_id: str
    """Queue schedule ID"""
