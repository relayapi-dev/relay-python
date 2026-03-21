# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["AnalyticsListDailyMetricsResponse", "Data"]


class Data(BaseModel):
    clicks: float
    """Total clicks"""

    comments: float
    """Total comments"""

    date: str
    """Date (YYYY-MM-DD)"""

    impressions: float
    """Total impressions"""

    likes: float
    """Total likes"""

    platforms: Dict[str, float]
    """Post count per platform"""

    post_count: float
    """Posts published on this date"""

    shares: float
    """Total shares"""

    views: float
    """Total views"""


class AnalyticsListDailyMetricsResponse(BaseModel):
    data: List[Data]
