# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MediaGetPresignURLResponse"]


class MediaGetPresignURLResponse(BaseModel):
    expires_in: int
    """Seconds until the upload URL expires"""

    upload_url: str
    """Pre-signed PUT URL for uploading"""

    url: str
    """Public URL after upload completes"""
