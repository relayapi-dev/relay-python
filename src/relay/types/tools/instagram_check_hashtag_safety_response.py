# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InstagramCheckHashtagSafetyResponse", "Result"]


class Result(BaseModel):
    hashtag: str
    """Hashtag checked"""

    status: Literal["safe", "restricted", "banned"]
    """Hashtag safety status"""


class InstagramCheckHashtagSafetyResponse(BaseModel):
    results: List[Result]
