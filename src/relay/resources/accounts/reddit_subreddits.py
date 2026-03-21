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
from ...types.accounts import reddit_subreddit_set_default_params
from ...types.accounts.reddit_subreddit_retrieve_response import RedditSubredditRetrieveResponse
from ...types.accounts.reddit_subreddit_set_default_response import RedditSubredditSetDefaultResponse

__all__ = ["RedditSubredditsResource", "AsyncRedditSubredditsResource"]


class RedditSubredditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedditSubredditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return RedditSubredditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedditSubredditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return RedditSubredditsResourceWithStreamingResponse(self)

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
    ) -> RedditSubredditRetrieveResponse:
        """
        Fetch Reddit subreddits for an account

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
            path_template("/v1/accounts/{id}/reddit-subreddits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedditSubredditRetrieveResponse,
        )

    def set_default(
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
    ) -> RedditSubredditSetDefaultResponse:
        """
        Set default Reddit subreddit

        Args:
          id: Resource ID

          subreddit: Subreddit name to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/accounts/{id}/reddit-subreddits", id=id),
            body=maybe_transform(
                {"subreddit": subreddit}, reddit_subreddit_set_default_params.RedditSubredditSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedditSubredditSetDefaultResponse,
        )


class AsyncRedditSubredditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedditSubredditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedditSubredditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedditSubredditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncRedditSubredditsResourceWithStreamingResponse(self)

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
    ) -> RedditSubredditRetrieveResponse:
        """
        Fetch Reddit subreddits for an account

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
            path_template("/v1/accounts/{id}/reddit-subreddits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedditSubredditRetrieveResponse,
        )

    async def set_default(
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
    ) -> RedditSubredditSetDefaultResponse:
        """
        Set default Reddit subreddit

        Args:
          id: Resource ID

          subreddit: Subreddit name to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/accounts/{id}/reddit-subreddits", id=id),
            body=await async_maybe_transform(
                {"subreddit": subreddit}, reddit_subreddit_set_default_params.RedditSubredditSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedditSubredditSetDefaultResponse,
        )


class RedditSubredditsResourceWithRawResponse:
    def __init__(self, reddit_subreddits: RedditSubredditsResource) -> None:
        self._reddit_subreddits = reddit_subreddits

        self.retrieve = to_raw_response_wrapper(
            reddit_subreddits.retrieve,
        )
        self.set_default = to_raw_response_wrapper(
            reddit_subreddits.set_default,
        )


class AsyncRedditSubredditsResourceWithRawResponse:
    def __init__(self, reddit_subreddits: AsyncRedditSubredditsResource) -> None:
        self._reddit_subreddits = reddit_subreddits

        self.retrieve = async_to_raw_response_wrapper(
            reddit_subreddits.retrieve,
        )
        self.set_default = async_to_raw_response_wrapper(
            reddit_subreddits.set_default,
        )


class RedditSubredditsResourceWithStreamingResponse:
    def __init__(self, reddit_subreddits: RedditSubredditsResource) -> None:
        self._reddit_subreddits = reddit_subreddits

        self.retrieve = to_streamed_response_wrapper(
            reddit_subreddits.retrieve,
        )
        self.set_default = to_streamed_response_wrapper(
            reddit_subreddits.set_default,
        )


class AsyncRedditSubredditsResourceWithStreamingResponse:
    def __init__(self, reddit_subreddits: AsyncRedditSubredditsResource) -> None:
        self._reddit_subreddits = reddit_subreddits

        self.retrieve = async_to_streamed_response_wrapper(
            reddit_subreddits.retrieve,
        )
        self.set_default = async_to_streamed_response_wrapper(
            reddit_subreddits.set_default,
        )
