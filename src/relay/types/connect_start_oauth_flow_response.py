# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectStartOAuthFlowResponse"]


class ConnectStartOAuthFlowResponse(BaseModel):
    auth_url: str
    """URL to redirect the user for OAuth authorization"""
