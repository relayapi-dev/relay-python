# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["RedditFlairRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    text: str


class RedditFlairRetrieveResponse(BaseModel):
    data: List[Data]
