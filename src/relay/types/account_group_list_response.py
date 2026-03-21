# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["AccountGroupListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Group ID"""

    account_ids: List[str]
    """Account IDs in the group"""

    created_at: datetime
    """Creation timestamp"""

    name: str
    """Group name"""

    updated_at: datetime
    """Last updated timestamp"""


class AccountGroupListResponse(BaseModel):
    data: List[Data]
