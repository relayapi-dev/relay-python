# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BroadcastSendResponse"]


class BroadcastSendResponse(BaseModel):
    id: str
    """Broadcast ID"""

    created_at: datetime
    """Created timestamp"""

    name: str
    """Broadcast name"""

    recipient_count: float
    """Total recipients"""

    status: Literal["draft", "scheduled", "sending", "sent", "failed"]
    """Broadcast status"""

    template: str
    """Template name"""

    failed: Optional[float] = None
    """Failed sends"""

    scheduled_at: Optional[datetime] = None
    """Scheduled time"""

    sent: Optional[float] = None
    """Successfully sent"""
