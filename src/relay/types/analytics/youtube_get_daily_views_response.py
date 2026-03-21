# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["YoutubeGetDailyViewsResponse", "Data"]


class Data(BaseModel):
    date: str
    """Date (YYYY-MM-DD)"""

    subscribers_gained: float
    """Net subscribers gained"""

    views: float
    """Total views"""

    watch_time_minutes: float
    """Watch time in minutes"""


class YoutubeGetDailyViewsResponse(BaseModel):
    data: List[Data]
