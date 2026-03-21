# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AnalyticsGetPostTimelineResponse", "Data"]


class Data(BaseModel):
    clicks: float

    comments: float

    date: str
    """Date (YYYY-MM-DD)"""

    impressions: float

    likes: float

    shares: float

    views: float


class AnalyticsGetPostTimelineResponse(BaseModel):
    data: List[Data]

    post_id: str
