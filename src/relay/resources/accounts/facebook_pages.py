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
from ...types.accounts import facebook_page_set_default_params
from ...types.accounts.facebook_page_retrieve_response import FacebookPageRetrieveResponse
from ...types.accounts.facebook_page_set_default_response import FacebookPageSetDefaultResponse

__all__ = ["FacebookPagesResource", "AsyncFacebookPagesResource"]


class FacebookPagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FacebookPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return FacebookPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FacebookPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return FacebookPagesResourceWithStreamingResponse(self)

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
    ) -> FacebookPageRetrieveResponse:
        """
        Fetch Facebook pages for an account

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
            path_template("/v1/accounts/{id}/facebook-pages", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FacebookPageRetrieveResponse,
        )

    def set_default(
        self,
        id: str,
        *,
        page_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FacebookPageSetDefaultResponse:
        """
        Set default Facebook page

        Args:
          id: Resource ID

          page_id: Facebook page ID to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/accounts/{id}/facebook-pages", id=id),
            body=maybe_transform({"page_id": page_id}, facebook_page_set_default_params.FacebookPageSetDefaultParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FacebookPageSetDefaultResponse,
        )


class AsyncFacebookPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFacebookPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFacebookPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFacebookPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncFacebookPagesResourceWithStreamingResponse(self)

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
    ) -> FacebookPageRetrieveResponse:
        """
        Fetch Facebook pages for an account

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
            path_template("/v1/accounts/{id}/facebook-pages", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FacebookPageRetrieveResponse,
        )

    async def set_default(
        self,
        id: str,
        *,
        page_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FacebookPageSetDefaultResponse:
        """
        Set default Facebook page

        Args:
          id: Resource ID

          page_id: Facebook page ID to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/accounts/{id}/facebook-pages", id=id),
            body=await async_maybe_transform(
                {"page_id": page_id}, facebook_page_set_default_params.FacebookPageSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FacebookPageSetDefaultResponse,
        )


class FacebookPagesResourceWithRawResponse:
    def __init__(self, facebook_pages: FacebookPagesResource) -> None:
        self._facebook_pages = facebook_pages

        self.retrieve = to_raw_response_wrapper(
            facebook_pages.retrieve,
        )
        self.set_default = to_raw_response_wrapper(
            facebook_pages.set_default,
        )


class AsyncFacebookPagesResourceWithRawResponse:
    def __init__(self, facebook_pages: AsyncFacebookPagesResource) -> None:
        self._facebook_pages = facebook_pages

        self.retrieve = async_to_raw_response_wrapper(
            facebook_pages.retrieve,
        )
        self.set_default = async_to_raw_response_wrapper(
            facebook_pages.set_default,
        )


class FacebookPagesResourceWithStreamingResponse:
    def __init__(self, facebook_pages: FacebookPagesResource) -> None:
        self._facebook_pages = facebook_pages

        self.retrieve = to_streamed_response_wrapper(
            facebook_pages.retrieve,
        )
        self.set_default = to_streamed_response_wrapper(
            facebook_pages.set_default,
        )


class AsyncFacebookPagesResourceWithStreamingResponse:
    def __init__(self, facebook_pages: AsyncFacebookPagesResource) -> None:
        self._facebook_pages = facebook_pages

        self.retrieve = async_to_streamed_response_wrapper(
            facebook_pages.retrieve,
        )
        self.set_default = async_to_streamed_response_wrapper(
            facebook_pages.set_default,
        )
