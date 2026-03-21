# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookSendTestResponse"]


class WebhookSendTestResponse(BaseModel):
    response_time_ms: Optional[int] = None
    """Response time in milliseconds"""

    status_code: Optional[int] = None
    """HTTP status code from the test delivery"""

    success: bool
    """Whether the test delivery succeeded"""
