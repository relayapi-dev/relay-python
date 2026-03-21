# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GmbLocationRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    address: Optional[str] = None

    name: str


class GmbLocationRetrieveResponse(BaseModel):
    data: List[Data]
