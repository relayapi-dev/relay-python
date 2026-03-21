# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ContactRetrieveResponse"]


class ContactRetrieveResponse(BaseModel):
    id: str
    """Contact ID"""

    created_at: datetime
    """Created timestamp"""

    opted_in: bool
    """Whether contact has opted in"""

    phone: str
    """Phone number"""

    email: Optional[str] = None
    """Email address"""

    groups: Optional[List[str]] = None
    """Group IDs"""

    name: Optional[str] = None
    """Contact name"""

    tags: Optional[List[str]] = None
    """Tags"""
