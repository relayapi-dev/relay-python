# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AnalyticsGetPostingFrequencyResponse", "Data"]


class Data(BaseModel):
    avg_engagement: float
    """Average engagement"""

    avg_impressions: float
    """Average impressions"""

    posts_per_week: float
    """Average posts per week in bucket"""

    sample_weeks: float
    """Number of weeks in sample"""


class AnalyticsGetPostingFrequencyResponse(BaseModel):
    data: List[Data]

    optimal_frequency: Optional[float] = None
    """Recommended posts per week"""
