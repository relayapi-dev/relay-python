# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["UsageRetrieveResponse", "APICalls", "Plan", "Usage"]


class APICalls(BaseModel):
    current_minute: float
    """API calls in the current minute"""

    limit_per_minute: float
    """Max API calls per minute"""


class Plan(BaseModel):
    api_calls_per_min: float
    """API calls allowed per minute"""

    name: str
    """Plan name"""

    posts_limit: float
    """Max posts per billing cycle"""


class Usage(BaseModel):
    cycle_end: datetime
    """Current billing cycle end"""

    cycle_resets_at: datetime
    """When the cycle resets"""

    cycle_start: datetime
    """Current billing cycle start"""

    posts_limit: float
    """Max posts per billing cycle"""

    posts_used: float
    """Posts used this cycle"""


class UsageRetrieveResponse(BaseModel):
    api_calls: APICalls

    plan: Plan

    usage: Usage
