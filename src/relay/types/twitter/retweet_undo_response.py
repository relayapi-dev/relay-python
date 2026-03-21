# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RetweetUndoResponse"]


class RetweetUndoResponse(BaseModel):
    success: bool
    """Whether the action succeeded"""
