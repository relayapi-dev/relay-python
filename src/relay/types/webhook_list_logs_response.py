# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookListLogsResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: datetime

    error: Optional[str] = None

    event: str

    response_time_ms: Optional[float] = None

    status_code: Optional[float] = None

    success: bool

    webhook_id: str


class WebhookListLogsResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
