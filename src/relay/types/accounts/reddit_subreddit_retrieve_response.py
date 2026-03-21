# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RedditSubredditRetrieveResponse", "Data"]


class Data(BaseModel):
    display_name: str

    name: str

    subscribers: Optional[float] = None


class RedditSubredditRetrieveResponse(BaseModel):
    data: List[Data]
