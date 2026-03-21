# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["PageListResponse", "Page"]


class Page(BaseModel):
    id: str
    """Facebook page ID"""

    name: str
    """Page name"""

    category: Optional[str] = None
    """Page category"""

    picture_url: Optional[str] = None
    """Page profile picture URL"""


class PageListResponse(BaseModel):
    pages: List[Page]
