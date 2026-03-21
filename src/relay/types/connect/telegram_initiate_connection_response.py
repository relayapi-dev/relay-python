# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TelegramInitiateConnectionResponse"]


class TelegramInitiateConnectionResponse(BaseModel):
    bot_username: str
    """Telegram bot username to message"""

    code: str
    """6-character access code"""

    expires_at: datetime
    """ISO 8601 expiry timestamp"""

    expires_in: int
    """Seconds until code expires"""

    instructions: List[str]
    """Step-by-step instructions for the user"""
