# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BusinessProfileRetrieveResponse"]


class BusinessProfileRetrieveResponse(BaseModel):
    about: Optional[str] = None
    """About text"""

    address: Optional[str] = None
    """Business address"""

    description: Optional[str] = None
    """Description"""

    email: Optional[str] = None
    """Business email"""

    profile_picture_url: Optional[str] = None
    """Profile picture URL"""

    websites: Optional[List[str]] = None
    """Website URLs"""
