# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["HideCreateResponse"]


class HideCreateResponse(BaseModel):
    success: bool
    """Whether the action succeeded"""

    comment_id: Optional[str] = None
    """Comment ID"""
