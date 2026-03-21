# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.inbox.comments.hide_create_response import HideCreateResponse
from ....types.inbox.comments.hide_delete_response import HideDeleteResponse

__all__ = ["HideResource", "AsyncHideResource"]


class HideResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return HideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return HideResourceWithStreamingResponse(self)

    def create(
        self,
        comment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HideCreateResponse:
        """
        Hide a comment

        Args:
          comment_id: Comment ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._post(
            path_template("/v1/inbox/comments/{comment_id}/hide", comment_id=comment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HideCreateResponse,
        )

    def delete(
        self,
        comment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HideDeleteResponse:
        """
        Unhide a comment

        Args:
          comment_id: Comment ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._delete(
            path_template("/v1/inbox/comments/{comment_id}/hide", comment_id=comment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HideDeleteResponse,
        )


class AsyncHideResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncHideResourceWithStreamingResponse(self)

    async def create(
        self,
        comment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HideCreateResponse:
        """
        Hide a comment

        Args:
          comment_id: Comment ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._post(
            path_template("/v1/inbox/comments/{comment_id}/hide", comment_id=comment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HideCreateResponse,
        )

    async def delete(
        self,
        comment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HideDeleteResponse:
        """
        Unhide a comment

        Args:
          comment_id: Comment ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._delete(
            path_template("/v1/inbox/comments/{comment_id}/hide", comment_id=comment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HideDeleteResponse,
        )


class HideResourceWithRawResponse:
    def __init__(self, hide: HideResource) -> None:
        self._hide = hide

        self.create = to_raw_response_wrapper(
            hide.create,
        )
        self.delete = to_raw_response_wrapper(
            hide.delete,
        )


class AsyncHideResourceWithRawResponse:
    def __init__(self, hide: AsyncHideResource) -> None:
        self._hide = hide

        self.create = async_to_raw_response_wrapper(
            hide.create,
        )
        self.delete = async_to_raw_response_wrapper(
            hide.delete,
        )


class HideResourceWithStreamingResponse:
    def __init__(self, hide: HideResource) -> None:
        self._hide = hide

        self.create = to_streamed_response_wrapper(
            hide.create,
        )
        self.delete = to_streamed_response_wrapper(
            hide.delete,
        )


class AsyncHideResourceWithStreamingResponse:
    def __init__(self, hide: AsyncHideResource) -> None:
        self._hide = hide

        self.create = async_to_streamed_response_wrapper(
            hide.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            hide.delete,
        )
