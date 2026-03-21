# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LocationListResponse", "Location"]


class Location(BaseModel):
    id: str
    """Google Business location ID"""

    name: str
    """Business name"""

    address: Optional[str] = None
    """Business address"""

    phone: Optional[str] = None
    """Business phone number"""


class LocationListResponse(BaseModel):
    locations: List[Location]
