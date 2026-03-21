# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MessageArchiveResponse"]


class MessageArchiveResponse(BaseModel):
    success: bool
    """Whether the action succeeded"""

    message_id: Optional[str] = None
    """Message ID"""
