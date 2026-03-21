# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ValidateValidatePostResponse", "Error", "Warning"]


class Error(BaseModel):
    code: str
    """Error code"""

    message: str
    """Human-readable error message"""

    target: str
    """Target identifier (account ID, platform, or field name)"""


class Warning(BaseModel):
    code: str
    """Error code"""

    message: str
    """Human-readable error message"""

    target: str
    """Target identifier (account ID, platform, or field name)"""


class ValidateValidatePostResponse(BaseModel):
    errors: List[Error]
    """Blocking errors"""

    valid: bool
    """Whether the post is valid for all targets"""

    warnings: List[Warning]
    """Non-blocking warnings"""
