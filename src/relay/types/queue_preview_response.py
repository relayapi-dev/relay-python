# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["QueuePreviewResponse"]


class QueuePreviewResponse(BaseModel):
    slots: List[datetime]
    """Upcoming slot timestamps (ISO 8601)"""
