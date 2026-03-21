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
from ...types.accounts import reddit_flair_retrieve_params
from ...types.accounts.reddit_flair_retrieve_response import RedditFlairRetrieveResponse

__all__ = ["RedditFlairsResource", "AsyncRedditFlairsResource"]


class RedditFlairsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedditFlairsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return RedditFlairsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedditFlairsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return RedditFlairsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        subreddit: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedditFlairRetrieveResponse:
        """
        Fetch Reddit flairs for a subreddit

        Args:
          id: Resource ID

          subreddit: Subreddit name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/accounts/{id}/reddit-flairs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"subreddit": subreddit}, reddit_flair_retrieve_params.RedditFlairRetrieveParams),
            ),
            cast_to=RedditFlairRetrieveResponse,
        )


class AsyncRedditFlairsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedditFlairsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedditFlairsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedditFlairsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncRedditFlairsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        subreddit: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedditFlairRetrieveResponse:
        """
        Fetch Reddit flairs for a subreddit

        Args:
          id: Resource ID

          subreddit: Subreddit name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/accounts/{id}/reddit-flairs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"subreddit": subreddit}, reddit_flair_retrieve_params.RedditFlairRetrieveParams
                ),
            ),
            cast_to=RedditFlairRetrieveResponse,
        )


class RedditFlairsResourceWithRawResponse:
    def __init__(self, reddit_flairs: RedditFlairsResource) -> None:
        self._reddit_flairs = reddit_flairs

        self.retrieve = to_raw_response_wrapper(
            reddit_flairs.retrieve,
        )


class AsyncRedditFlairsResourceWithRawResponse:
    def __init__(self, reddit_flairs: AsyncRedditFlairsResource) -> None:
        self._reddit_flairs = reddit_flairs

        self.retrieve = async_to_raw_response_wrapper(
            reddit_flairs.retrieve,
        )


class RedditFlairsResourceWithStreamingResponse:
    def __init__(self, reddit_flairs: RedditFlairsResource) -> None:
        self._reddit_flairs = reddit_flairs

        self.retrieve = to_streamed_response_wrapper(
            reddit_flairs.retrieve,
        )


class AsyncRedditFlairsResourceWithStreamingResponse:
    def __init__(self, reddit_flairs: AsyncRedditFlairsResource) -> None:
        self._reddit_flairs = reddit_flairs

        self.retrieve = async_to_streamed_response_wrapper(
            reddit_flairs.retrieve,
        )
