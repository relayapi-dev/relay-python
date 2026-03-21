# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AnalyticsGetBestTimeResponse", "Data"]


class Data(BaseModel):
    avg_engagement: float
    """Average engagement score"""

    day_of_week: int
    """Day of week (0=Sunday)"""

    hour_utc: int
    """Hour in UTC"""

    post_count: float
    """Number of posts analyzed"""


class AnalyticsGetBestTimeResponse(BaseModel):
    data: List[Data]
