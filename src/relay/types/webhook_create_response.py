# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    id: str
    """Webhook ID"""

    created_at: datetime
    """Creation timestamp"""

    enabled: bool
    """Whether the webhook is active"""

    events: List[str]
    """Subscribed events"""

    secret: str
    """Webhook signing secret (shown only once)"""

    url: str
    """Endpoint URL"""
