# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["HealthRetrieveResponse", "Error"]


class Error(BaseModel):
    code: str

    message: str


class HealthRetrieveResponse(BaseModel):
    id: str

    healthy: bool

    platform: str

    token_expires_at: Optional[str] = None

    username: Optional[str] = None

    error: Optional[Error] = None
