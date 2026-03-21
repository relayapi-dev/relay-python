# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FacebookPageRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    access_token: Optional[str] = None


class FacebookPageRetrieveResponse(BaseModel):
    data: List[Data]
