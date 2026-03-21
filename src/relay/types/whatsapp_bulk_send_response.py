# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WhatsappBulkSendResponse", "Result", "Summary"]


class Result(BaseModel):
    phone: str
    """Recipient phone number"""

    status: Literal["sent", "failed"]
    """Send status"""

    error: Optional[str] = None
    """Error message if failed"""


class Summary(BaseModel):
    failed: float
    """Failed count"""

    sent: float
    """Successfully sent count"""


class WhatsappBulkSendResponse(BaseModel):
    results: List[Result]

    summary: Summary
