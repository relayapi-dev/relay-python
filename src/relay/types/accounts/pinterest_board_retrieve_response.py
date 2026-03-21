# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PinterestBoardRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    url: Optional[str] = None


class PinterestBoardRetrieveResponse(BaseModel):
    data: List[Data]
