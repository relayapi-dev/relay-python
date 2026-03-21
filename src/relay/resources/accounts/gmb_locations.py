# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts import gmb_location_set_default_params
from ...types.accounts.gmb_location_retrieve_response import GmbLocationRetrieveResponse
from ...types.accounts.gmb_location_set_default_response import GmbLocationSetDefaultResponse

__all__ = ["GmbLocationsResource", "AsyncGmbLocationsResource"]


class GmbLocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GmbLocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return GmbLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GmbLocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return GmbLocationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GmbLocationRetrieveResponse:
        """
        Fetch Google My Business locations

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/accounts/{id}/gmb-locations", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GmbLocationRetrieveResponse,
        )

    def set_default(
        self,
        id: str,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GmbLocationSetDefaultResponse:
        """
        Set default GMB location

        Args:
          id: Resource ID

          location_id: Google My Business location ID to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/accounts/{id}/gmb-locations", id=id),
            body=maybe_transform(
                {"location_id": location_id}, gmb_location_set_default_params.GmbLocationSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GmbLocationSetDefaultResponse,
        )


class AsyncGmbLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGmbLocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGmbLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGmbLocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncGmbLocationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GmbLocationRetrieveResponse:
        """
        Fetch Google My Business locations

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/accounts/{id}/gmb-locations", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GmbLocationRetrieveResponse,
        )

    async def set_default(
        self,
        id: str,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GmbLocationSetDefaultResponse:
        """
        Set default GMB location

        Args:
          id: Resource ID

          location_id: Google My Business location ID to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/accounts/{id}/gmb-locations", id=id),
            body=await async_maybe_transform(
                {"location_id": location_id}, gmb_location_set_default_params.GmbLocationSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GmbLocationSetDefaultResponse,
        )


class GmbLocationsResourceWithRawResponse:
    def __init__(self, gmb_locations: GmbLocationsResource) -> None:
        self._gmb_locations = gmb_locations

        self.retrieve = to_raw_response_wrapper(
            gmb_locations.retrieve,
        )
        self.set_default = to_raw_response_wrapper(
            gmb_locations.set_default,
        )


class AsyncGmbLocationsResourceWithRawResponse:
    def __init__(self, gmb_locations: AsyncGmbLocationsResource) -> None:
        self._gmb_locations = gmb_locations

        self.retrieve = async_to_raw_response_wrapper(
            gmb_locations.retrieve,
        )
        self.set_default = async_to_raw_response_wrapper(
            gmb_locations.set_default,
        )


class GmbLocationsResourceWithStreamingResponse:
    def __init__(self, gmb_locations: GmbLocationsResource) -> None:
        self._gmb_locations = gmb_locations

        self.retrieve = to_streamed_response_wrapper(
            gmb_locations.retrieve,
        )
        self.set_default = to_streamed_response_wrapper(
            gmb_locations.set_default,
        )


class AsyncGmbLocationsResourceWithStreamingResponse:
    def __init__(self, gmb_locations: AsyncGmbLocationsResource) -> None:
        self._gmb_locations = gmb_locations

        self.retrieve = async_to_streamed_response_wrapper(
            gmb_locations.retrieve,
        )
        self.set_default = async_to_streamed_response_wrapper(
            gmb_locations.set_default,
        )
