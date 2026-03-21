# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import reddit_search_params, reddit_get_feed_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.reddit_search_response import RedditSearchResponse
from ..types.reddit_get_feed_response import RedditGetFeedResponse

__all__ = ["RedditResource", "AsyncRedditResource"]


class RedditResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return RedditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return RedditResourceWithStreamingResponse(self)

    def get_feed(
        self,
        *,
        account_id: str,
        subreddit: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort: Literal["hot", "new", "top", "rising"] | Omit = omit,
        time: Literal["hour", "day", "week", "month", "year", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedditGetFeedResponse:
        """
        Get subreddit feed

        Args:
          account_id: Reddit account ID

          subreddit: Subreddit name

          cursor: Pagination cursor

          limit: Number of items per page

          sort: Sort order

          time: Time filter (for top sort)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/reddit/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "subreddit": subreddit,
                        "cursor": cursor,
                        "limit": limit,
                        "sort": sort,
                        "time": time,
                    },
                    reddit_get_feed_params.RedditGetFeedParams,
                ),
            ),
            cast_to=RedditGetFeedResponse,
        )

    def search(
        self,
        *,
        account_id: str,
        query: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort: Literal["relevance", "hot", "top", "new", "comments"] | Omit = omit,
        subreddit: str | Omit = omit,
        time: Literal["hour", "day", "week", "month", "year", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedditSearchResponse:
        """
        Search Reddit posts

        Args:
          account_id: Reddit account ID

          query: Search query

          cursor: Pagination cursor

          limit: Number of items per page

          sort: Sort order

          subreddit: Limit to subreddit

          time: Time filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/reddit/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "query": query,
                        "cursor": cursor,
                        "limit": limit,
                        "sort": sort,
                        "subreddit": subreddit,
                        "time": time,
                    },
                    reddit_search_params.RedditSearchParams,
                ),
            ),
            cast_to=RedditSearchResponse,
        )


class AsyncRedditResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncRedditResourceWithStreamingResponse(self)

    async def get_feed(
        self,
        *,
        account_id: str,
        subreddit: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort: Literal["hot", "new", "top", "rising"] | Omit = omit,
        time: Literal["hour", "day", "week", "month", "year", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedditGetFeedResponse:
        """
        Get subreddit feed

        Args:
          account_id: Reddit account ID

          subreddit: Subreddit name

          cursor: Pagination cursor

          limit: Number of items per page

          sort: Sort order

          time: Time filter (for top sort)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/reddit/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "subreddit": subreddit,
                        "cursor": cursor,
                        "limit": limit,
                        "sort": sort,
                        "time": time,
                    },
                    reddit_get_feed_params.RedditGetFeedParams,
                ),
            ),
            cast_to=RedditGetFeedResponse,
        )

    async def search(
        self,
        *,
        account_id: str,
        query: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort: Literal["relevance", "hot", "top", "new", "comments"] | Omit = omit,
        subreddit: str | Omit = omit,
        time: Literal["hour", "day", "week", "month", "year", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedditSearchResponse:
        """
        Search Reddit posts

        Args:
          account_id: Reddit account ID

          query: Search query

          cursor: Pagination cursor

          limit: Number of items per page

          sort: Sort order

          subreddit: Limit to subreddit

          time: Time filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/reddit/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "query": query,
                        "cursor": cursor,
                        "limit": limit,
                        "sort": sort,
                        "subreddit": subreddit,
                        "time": time,
                    },
                    reddit_search_params.RedditSearchParams,
                ),
            ),
            cast_to=RedditSearchResponse,
        )


class RedditResourceWithRawResponse:
    def __init__(self, reddit: RedditResource) -> None:
        self._reddit = reddit

        self.get_feed = to_raw_response_wrapper(
            reddit.get_feed,
        )
        self.search = to_raw_response_wrapper(
            reddit.search,
        )


class AsyncRedditResourceWithRawResponse:
    def __init__(self, reddit: AsyncRedditResource) -> None:
        self._reddit = reddit

        self.get_feed = async_to_raw_response_wrapper(
            reddit.get_feed,
        )
        self.search = async_to_raw_response_wrapper(
            reddit.search,
        )


class RedditResourceWithStreamingResponse:
    def __init__(self, reddit: RedditResource) -> None:
        self._reddit = reddit

        self.get_feed = to_streamed_response_wrapper(
            reddit.get_feed,
        )
        self.search = to_streamed_response_wrapper(
            reddit.search,
        )


class AsyncRedditResourceWithStreamingResponse:
    def __init__(self, reddit: AsyncRedditResource) -> None:
        self._reddit = reddit

        self.get_feed = async_to_streamed_response_wrapper(
            reddit.get_feed,
        )
        self.search = async_to_streamed_response_wrapper(
            reddit.search,
        )
