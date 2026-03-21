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
from ...types.twitter import follow_create_params, follow_unfollow_params
from ...types.twitter.follow_create_response import FollowCreateResponse
from ...types.twitter.follow_unfollow_response import FollowUnfollowResponse

__all__ = ["FollowResource", "AsyncFollowResource"]


class FollowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FollowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return FollowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return FollowResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        target_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowCreateResponse:
        """
        Follow a user

        Args:
          account_id: Twitter account ID

          target_user_id: User ID to follow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/twitter/follow",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "target_user_id": target_user_id,
                },
                follow_create_params.FollowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowCreateResponse,
        )

    def unfollow(
        self,
        *,
        account_id: str,
        target_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowUnfollowResponse:
        """
        Unfollow a user

        Args:
          account_id: Twitter account ID

          target_user_id: User ID to follow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/twitter/follow",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "target_user_id": target_user_id,
                },
                follow_unfollow_params.FollowUnfollowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowUnfollowResponse,
        )


class AsyncFollowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFollowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncFollowResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        target_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowCreateResponse:
        """
        Follow a user

        Args:
          account_id: Twitter account ID

          target_user_id: User ID to follow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/twitter/follow",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "target_user_id": target_user_id,
                },
                follow_create_params.FollowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowCreateResponse,
        )

    async def unfollow(
        self,
        *,
        account_id: str,
        target_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowUnfollowResponse:
        """
        Unfollow a user

        Args:
          account_id: Twitter account ID

          target_user_id: User ID to follow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/twitter/follow",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "target_user_id": target_user_id,
                },
                follow_unfollow_params.FollowUnfollowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowUnfollowResponse,
        )


class FollowResourceWithRawResponse:
    def __init__(self, follow: FollowResource) -> None:
        self._follow = follow

        self.create = to_raw_response_wrapper(
            follow.create,
        )
        self.unfollow = to_raw_response_wrapper(
            follow.unfollow,
        )


class AsyncFollowResourceWithRawResponse:
    def __init__(self, follow: AsyncFollowResource) -> None:
        self._follow = follow

        self.create = async_to_raw_response_wrapper(
            follow.create,
        )
        self.unfollow = async_to_raw_response_wrapper(
            follow.unfollow,
        )


class FollowResourceWithStreamingResponse:
    def __init__(self, follow: FollowResource) -> None:
        self._follow = follow

        self.create = to_streamed_response_wrapper(
            follow.create,
        )
        self.unfollow = to_streamed_response_wrapper(
            follow.unfollow,
        )


class AsyncFollowResourceWithStreamingResponse:
    def __init__(self, follow: AsyncFollowResource) -> None:
        self._follow = follow

        self.create = async_to_streamed_response_wrapper(
            follow.create,
        )
        self.unfollow = async_to_streamed_response_wrapper(
            follow.unfollow,
        )
