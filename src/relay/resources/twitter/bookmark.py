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
from ...types.twitter import bookmark_create_params, bookmark_remove_params
from ...types.twitter.bookmark_create_response import BookmarkCreateResponse
from ...types.twitter.bookmark_remove_response import BookmarkRemoveResponse

__all__ = ["BookmarkResource", "AsyncBookmarkResource"]


class BookmarkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookmarkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return BookmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return BookmarkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        tweet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BookmarkCreateResponse:
        """
        Bookmark a tweet

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to bookmark

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/twitter/bookmark",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                bookmark_create_params.BookmarkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkCreateResponse,
        )

    def remove(
        self,
        *,
        account_id: str,
        tweet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BookmarkRemoveResponse:
        """
        Remove a bookmark

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to bookmark

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/twitter/bookmark",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                bookmark_remove_params.BookmarkRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkRemoveResponse,
        )


class AsyncBookmarkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookmarkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncBookmarkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        tweet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BookmarkCreateResponse:
        """
        Bookmark a tweet

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to bookmark

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/twitter/bookmark",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                bookmark_create_params.BookmarkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkCreateResponse,
        )

    async def remove(
        self,
        *,
        account_id: str,
        tweet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BookmarkRemoveResponse:
        """
        Remove a bookmark

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to bookmark

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/twitter/bookmark",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                bookmark_remove_params.BookmarkRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkRemoveResponse,
        )


class BookmarkResourceWithRawResponse:
    def __init__(self, bookmark: BookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = to_raw_response_wrapper(
            bookmark.create,
        )
        self.remove = to_raw_response_wrapper(
            bookmark.remove,
        )


class AsyncBookmarkResourceWithRawResponse:
    def __init__(self, bookmark: AsyncBookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = async_to_raw_response_wrapper(
            bookmark.create,
        )
        self.remove = async_to_raw_response_wrapper(
            bookmark.remove,
        )


class BookmarkResourceWithStreamingResponse:
    def __init__(self, bookmark: BookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = to_streamed_response_wrapper(
            bookmark.create,
        )
        self.remove = to_streamed_response_wrapper(
            bookmark.remove,
        )


class AsyncBookmarkResourceWithStreamingResponse:
    def __init__(self, bookmark: AsyncBookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = async_to_streamed_response_wrapper(
            bookmark.create,
        )
        self.remove = async_to_streamed_response_wrapper(
            bookmark.remove,
        )
