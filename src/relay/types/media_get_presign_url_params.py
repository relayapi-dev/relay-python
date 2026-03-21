# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MediaGetPresignURLParams"]


class MediaGetPresignURLParams(TypedDict, total=False):
    content_type: Required[str]
    """MIME type of the file to upload"""

    filename: Required[str]
    """Desired filename"""
