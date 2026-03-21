# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WhatsappGetSDKConfigResponse"]


class WhatsappGetSDKConfigResponse(BaseModel):
    app_id: str
    """Facebook App ID for WhatsApp embedded signup"""

    config_id: str
    """WhatsApp configuration ID"""
