# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.connect import whatsapp_connect_via_credentials_params, whatsapp_complete_embedded_signup_params
from ...types.connect.whatsapp_get_sdk_config_response import WhatsappGetSDKConfigResponse
from ...types.connect.whatsapp_connect_via_credentials_response import WhatsappConnectViaCredentialsResponse
from ...types.connect.whatsapp_complete_embedded_signup_response import WhatsappCompleteEmbeddedSignupResponse

__all__ = ["WhatsappResource", "AsyncWhatsappResource"]


class WhatsappResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return WhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return WhatsappResourceWithStreamingResponse(self)

    def complete_embedded_signup(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappCompleteEmbeddedSignupResponse:
        """
        Complete WhatsApp Embedded Signup

        Args:
          code: Code from WhatsApp embedded signup flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connect/whatsapp/embedded-signup",
            body=maybe_transform(
                {"code": code}, whatsapp_complete_embedded_signup_params.WhatsappCompleteEmbeddedSignupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappCompleteEmbeddedSignupResponse,
        )

    def connect_via_credentials(
        self,
        *,
        access_token: str,
        phone_number_id: str,
        waba_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappConnectViaCredentialsResponse:
        """
        Connect WhatsApp via System User credentials

        Args:
          access_token: WhatsApp Business API access token

          phone_number_id: WhatsApp phone number ID

          waba_id: WhatsApp Business Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connect/whatsapp/credentials",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "phone_number_id": phone_number_id,
                    "waba_id": waba_id,
                },
                whatsapp_connect_via_credentials_params.WhatsappConnectViaCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappConnectViaCredentialsResponse,
        )

    def get_sdk_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappGetSDKConfigResponse:
        """Get WhatsApp Embedded Signup SDK config"""
        return self._get(
            "/v1/connect/whatsapp/sdk-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappGetSDKConfigResponse,
        )


class AsyncWhatsappResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncWhatsappResourceWithStreamingResponse(self)

    async def complete_embedded_signup(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappCompleteEmbeddedSignupResponse:
        """
        Complete WhatsApp Embedded Signup

        Args:
          code: Code from WhatsApp embedded signup flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connect/whatsapp/embedded-signup",
            body=await async_maybe_transform(
                {"code": code}, whatsapp_complete_embedded_signup_params.WhatsappCompleteEmbeddedSignupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappCompleteEmbeddedSignupResponse,
        )

    async def connect_via_credentials(
        self,
        *,
        access_token: str,
        phone_number_id: str,
        waba_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappConnectViaCredentialsResponse:
        """
        Connect WhatsApp via System User credentials

        Args:
          access_token: WhatsApp Business API access token

          phone_number_id: WhatsApp phone number ID

          waba_id: WhatsApp Business Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connect/whatsapp/credentials",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "phone_number_id": phone_number_id,
                    "waba_id": waba_id,
                },
                whatsapp_connect_via_credentials_params.WhatsappConnectViaCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappConnectViaCredentialsResponse,
        )

    async def get_sdk_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappGetSDKConfigResponse:
        """Get WhatsApp Embedded Signup SDK config"""
        return await self._get(
            "/v1/connect/whatsapp/sdk-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappGetSDKConfigResponse,
        )


class WhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.complete_embedded_signup = to_raw_response_wrapper(
            whatsapp.complete_embedded_signup,
        )
        self.connect_via_credentials = to_raw_response_wrapper(
            whatsapp.connect_via_credentials,
        )
        self.get_sdk_config = to_raw_response_wrapper(
            whatsapp.get_sdk_config,
        )


class AsyncWhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.complete_embedded_signup = async_to_raw_response_wrapper(
            whatsapp.complete_embedded_signup,
        )
        self.connect_via_credentials = async_to_raw_response_wrapper(
            whatsapp.connect_via_credentials,
        )
        self.get_sdk_config = async_to_raw_response_wrapper(
            whatsapp.get_sdk_config,
        )


class WhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.complete_embedded_signup = to_streamed_response_wrapper(
            whatsapp.complete_embedded_signup,
        )
        self.connect_via_credentials = to_streamed_response_wrapper(
            whatsapp.connect_via_credentials,
        )
        self.get_sdk_config = to_streamed_response_wrapper(
            whatsapp.get_sdk_config,
        )


class AsyncWhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.complete_embedded_signup = async_to_streamed_response_wrapper(
            whatsapp.complete_embedded_signup,
        )
        self.connect_via_credentials = async_to_streamed_response_wrapper(
            whatsapp.connect_via_credentials,
        )
        self.get_sdk_config = async_to_streamed_response_wrapper(
            whatsapp.get_sdk_config,
        )
