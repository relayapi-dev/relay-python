# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MediaUploadResponse"]


class MediaUploadResponse(BaseModel):
    filename: str
    """Original filename"""

    size: int
    """File size in bytes"""

    type: str
    """MIME type of the uploaded file"""

    url: str
    """Public URL of the uploaded file"""
