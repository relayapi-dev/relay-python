# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["HideDeleteResponse"]


class HideDeleteResponse(BaseModel):
    success: bool
    """Whether the action succeeded"""

    comment_id: Optional[str] = None
    """Comment ID"""
