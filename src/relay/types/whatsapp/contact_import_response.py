# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContactImportResponse"]


class ContactImportResponse(BaseModel):
    failed: float
    """Failed count"""

    imported: float
    """Successfully imported count"""

    skipped: float
    """Skipped (duplicate) count"""
