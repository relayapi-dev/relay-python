# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WhatsappListPhoneNumbersResponse", "Data"]


class Data(BaseModel):
    id: str
    """Phone number ID"""

    phone_number: str
    """Phone number"""

    status: Literal["active", "inactive", "pending"]
    """Registration status"""

    display_name: Optional[str] = None
    """Display name"""


class WhatsappListPhoneNumbersResponse(BaseModel):
    data: List[Data]
