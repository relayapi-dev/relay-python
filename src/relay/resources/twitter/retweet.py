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
from ...types.twitter import retweet_undo_params, retweet_create_params
from ...types.twitter.retweet_undo_response import RetweetUndoResponse
from ...types.twitter.retweet_create_response import RetweetCreateResponse

__all__ = ["RetweetResource", "AsyncRetweetResource"]


class RetweetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetweetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return RetweetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetweetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return RetweetResourceWithStreamingResponse(self)

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
    ) -> RetweetCreateResponse:
        """
        Retweet a tweet

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to retweet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/twitter/retweet",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                retweet_create_params.RetweetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetCreateResponse,
        )

    def undo(
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
    ) -> RetweetUndoResponse:
        """
        Undo a retweet

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to retweet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/twitter/retweet",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                retweet_undo_params.RetweetUndoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetUndoResponse,
        )


class AsyncRetweetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetweetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetweetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetweetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncRetweetResourceWithStreamingResponse(self)

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
    ) -> RetweetCreateResponse:
        """
        Retweet a tweet

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to retweet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/twitter/retweet",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                retweet_create_params.RetweetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetCreateResponse,
        )

    async def undo(
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
    ) -> RetweetUndoResponse:
        """
        Undo a retweet

        Args:
          account_id: Twitter account ID

          tweet_id: Tweet ID to retweet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/twitter/retweet",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "tweet_id": tweet_id,
                },
                retweet_undo_params.RetweetUndoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetUndoResponse,
        )


class RetweetResourceWithRawResponse:
    def __init__(self, retweet: RetweetResource) -> None:
        self._retweet = retweet

        self.create = to_raw_response_wrapper(
            retweet.create,
        )
        self.undo = to_raw_response_wrapper(
            retweet.undo,
        )


class AsyncRetweetResourceWithRawResponse:
    def __init__(self, retweet: AsyncRetweetResource) -> None:
        self._retweet = retweet

        self.create = async_to_raw_response_wrapper(
            retweet.create,
        )
        self.undo = async_to_raw_response_wrapper(
            retweet.undo,
        )


class RetweetResourceWithStreamingResponse:
    def __init__(self, retweet: RetweetResource) -> None:
        self._retweet = retweet

        self.create = to_streamed_response_wrapper(
            retweet.create,
        )
        self.undo = to_streamed_response_wrapper(
            retweet.undo,
        )


class AsyncRetweetResourceWithStreamingResponse:
    def __init__(self, retweet: AsyncRetweetResource) -> None:
        self._retweet = retweet

        self.create = async_to_streamed_response_wrapper(
            retweet.create,
        )
        self.undo = async_to_streamed_response_wrapper(
            retweet.undo,
        )
