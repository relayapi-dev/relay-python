# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LinkedinOrganizationRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    vanity_name: Optional[str] = None


class LinkedinOrganizationRetrieveResponse(BaseModel):
    data: List[Data]
