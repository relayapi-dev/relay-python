# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.whatsapp import business_profile_update_params, business_profile_retrieve_params
from ...types.whatsapp.business_profile_update_response import BusinessProfileUpdateResponse
from ...types.whatsapp.business_profile_retrieve_response import BusinessProfileRetrieveResponse

__all__ = ["BusinessProfileResource", "AsyncBusinessProfileResource"]


class BusinessProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BusinessProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return BusinessProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return BusinessProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BusinessProfileRetrieveResponse:
        """
        Get WhatsApp Business profile

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/whatsapp/business-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, business_profile_retrieve_params.BusinessProfileRetrieveParams
                ),
            ),
            cast_to=BusinessProfileRetrieveResponse,
        )

    def update(
        self,
        *,
        account_id: str,
        about: str | Omit = omit,
        address: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        websites: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BusinessProfileUpdateResponse:
        """
        Update WhatsApp Business profile

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/whatsapp/business-profile",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "about": about,
                    "address": address,
                    "description": description,
                    "email": email,
                    "websites": websites,
                },
                business_profile_update_params.BusinessProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessProfileUpdateResponse,
        )


class AsyncBusinessProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBusinessProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncBusinessProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BusinessProfileRetrieveResponse:
        """
        Get WhatsApp Business profile

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/whatsapp/business-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, business_profile_retrieve_params.BusinessProfileRetrieveParams
                ),
            ),
            cast_to=BusinessProfileRetrieveResponse,
        )

    async def update(
        self,
        *,
        account_id: str,
        about: str | Omit = omit,
        address: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        websites: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BusinessProfileUpdateResponse:
        """
        Update WhatsApp Business profile

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/whatsapp/business-profile",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "about": about,
                    "address": address,
                    "description": description,
                    "email": email,
                    "websites": websites,
                },
                business_profile_update_params.BusinessProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessProfileUpdateResponse,
        )


class BusinessProfileResourceWithRawResponse:
    def __init__(self, business_profile: BusinessProfileResource) -> None:
        self._business_profile = business_profile

        self.retrieve = to_raw_response_wrapper(
            business_profile.retrieve,
        )
        self.update = to_raw_response_wrapper(
            business_profile.update,
        )


class AsyncBusinessProfileResourceWithRawResponse:
    def __init__(self, business_profile: AsyncBusinessProfileResource) -> None:
        self._business_profile = business_profile

        self.retrieve = async_to_raw_response_wrapper(
            business_profile.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            business_profile.update,
        )


class BusinessProfileResourceWithStreamingResponse:
    def __init__(self, business_profile: BusinessProfileResource) -> None:
        self._business_profile = business_profile

        self.retrieve = to_streamed_response_wrapper(
            business_profile.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            business_profile.update,
        )


class AsyncBusinessProfileResourceWithStreamingResponse:
    def __init__(self, business_profile: AsyncBusinessProfileResource) -> None:
        self._business_profile = business_profile

        self.retrieve = async_to_streamed_response_wrapper(
            business_profile.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            business_profile.update,
        )
