# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .reply import (
    ReplyResource,
    AsyncReplyResource,
    ReplyResourceWithRawResponse,
    AsyncReplyResourceWithRawResponse,
    ReplyResourceWithStreamingResponse,
    AsyncReplyResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.inbox import review_list_params
from ...._base_client import make_request_options
from ....types.inbox.review_list_response import ReviewListResponse

__all__ = ["ReviewsResource", "AsyncReviewsResource"]


class ReviewsResource(SyncAPIResource):
    @cached_property
    def reply(self) -> ReplyResource:
        return ReplyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return ReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return ReviewsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        max_rating: int | Omit = omit,
        min_rating: int | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewListResponse:
        """
        List reviews across platforms

        Args:
          account_id: Filter by account ID

          cursor: Pagination cursor

          limit: Number of items

          platform: Filter by platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/inbox/reviews",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                        "max_rating": max_rating,
                        "min_rating": min_rating,
                        "platform": platform,
                    },
                    review_list_params.ReviewListParams,
                ),
            ),
            cast_to=ReviewListResponse,
        )


class AsyncReviewsResource(AsyncAPIResource):
    @cached_property
    def reply(self) -> AsyncReplyResource:
        return AsyncReplyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncReviewsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        max_rating: int | Omit = omit,
        min_rating: int | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewListResponse:
        """
        List reviews across platforms

        Args:
          account_id: Filter by account ID

          cursor: Pagination cursor

          limit: Number of items

          platform: Filter by platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/inbox/reviews",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                        "max_rating": max_rating,
                        "min_rating": min_rating,
                        "platform": platform,
                    },
                    review_list_params.ReviewListParams,
                ),
            ),
            cast_to=ReviewListResponse,
        )


class ReviewsResourceWithRawResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.list = to_raw_response_wrapper(
            reviews.list,
        )

    @cached_property
    def reply(self) -> ReplyResourceWithRawResponse:
        return ReplyResourceWithRawResponse(self._reviews.reply)


class AsyncReviewsResourceWithRawResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.list = async_to_raw_response_wrapper(
            reviews.list,
        )

    @cached_property
    def reply(self) -> AsyncReplyResourceWithRawResponse:
        return AsyncReplyResourceWithRawResponse(self._reviews.reply)


class ReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.list = to_streamed_response_wrapper(
            reviews.list,
        )

    @cached_property
    def reply(self) -> ReplyResourceWithStreamingResponse:
        return ReplyResourceWithStreamingResponse(self._reviews.reply)


class AsyncReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.list = async_to_streamed_response_wrapper(
            reviews.list,
        )

    @cached_property
    def reply(self) -> AsyncReplyResourceWithStreamingResponse:
        return AsyncReplyResourceWithStreamingResponse(self._reviews.reply)
