# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .hide import (
    HideResource,
    AsyncHideResource,
    HideResourceWithRawResponse,
    AsyncHideResourceWithRawResponse,
    HideResourceWithStreamingResponse,
    AsyncHideResourceWithStreamingResponse,
)
from .like import (
    LikeResource,
    AsyncLikeResource,
    LikeResourceWithRawResponse,
    AsyncLikeResourceWithRawResponse,
    LikeResourceWithStreamingResponse,
    AsyncLikeResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.inbox import (
    comment_list_params,
    comment_reply_params,
    comment_retrieve_params,
    comment_private_reply_params,
)
from ...._base_client import make_request_options
from ....types.inbox.comment_list_response import CommentListResponse
from ....types.inbox.comment_reply_response import CommentReplyResponse
from ....types.inbox.comment_delete_response import CommentDeleteResponse
from ....types.inbox.comment_retrieve_response import CommentRetrieveResponse
from ....types.inbox.comment_private_reply_response import CommentPrivateReplyResponse

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    @cached_property
    def hide(self) -> HideResource:
        return HideResource(self._client)

    @cached_property
    def like(self) -> LikeResource:
        return LikeResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        post_id: str,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> CommentRetrieveResponse:
        """
        Get comments for a specific post

        Args:
          post_id: Post ID

          account_id: Filter by account ID

          cursor: Pagination cursor

          limit: Number of items

          platform: Filter by platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._get(
            path_template("/v1/inbox/comments/{post_id}", post_id=post_id),
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
                        "platform": platform,
                    },
                    comment_retrieve_params.CommentRetrieveParams,
                ),
            ),
            cast_to=CommentRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> CommentListResponse:
        """
        List comments across platforms

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
            "/v1/inbox/comments",
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
                        "platform": platform,
                    },
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
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
    ) -> CommentDeleteResponse:
        """
        Delete a comment

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
            path_template("/v1/inbox/comments/{comment_id}", comment_id=comment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentDeleteResponse,
        )

    def private_reply(
        self,
        comment_id: str,
        *,
        account_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentPrivateReplyResponse:
        """
        Send a private reply to a commenter

        Args:
          comment_id: Comment ID

          account_id: Account ID to reply from

          text: Private reply text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._post(
            path_template("/v1/inbox/comments/{comment_id}/private-reply", comment_id=comment_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                },
                comment_private_reply_params.CommentPrivateReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentPrivateReplyResponse,
        )

    def reply(
        self,
        post_id: str,
        *,
        account_id: str,
        text: str,
        comment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentReplyResponse:
        """
        Reply to a comment

        Args:
          post_id: Post ID

          account_id: Account ID to reply from

          text: Reply text

          comment_id: Parent comment ID for threaded replies

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._post(
            path_template("/v1/inbox/comments/{post_id}/reply", post_id=post_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                    "comment_id": comment_id,
                },
                comment_reply_params.CommentReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentReplyResponse,
        )


class AsyncCommentsResource(AsyncAPIResource):
    @cached_property
    def hide(self) -> AsyncHideResource:
        return AsyncHideResource(self._client)

    @cached_property
    def like(self) -> AsyncLikeResource:
        return AsyncLikeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        post_id: str,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> CommentRetrieveResponse:
        """
        Get comments for a specific post

        Args:
          post_id: Post ID

          account_id: Filter by account ID

          cursor: Pagination cursor

          limit: Number of items

          platform: Filter by platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._get(
            path_template("/v1/inbox/comments/{post_id}", post_id=post_id),
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
                        "platform": platform,
                    },
                    comment_retrieve_params.CommentRetrieveParams,
                ),
            ),
            cast_to=CommentRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> CommentListResponse:
        """
        List comments across platforms

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
            "/v1/inbox/comments",
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
                        "platform": platform,
                    },
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
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
    ) -> CommentDeleteResponse:
        """
        Delete a comment

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
            path_template("/v1/inbox/comments/{comment_id}", comment_id=comment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentDeleteResponse,
        )

    async def private_reply(
        self,
        comment_id: str,
        *,
        account_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentPrivateReplyResponse:
        """
        Send a private reply to a commenter

        Args:
          comment_id: Comment ID

          account_id: Account ID to reply from

          text: Private reply text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._post(
            path_template("/v1/inbox/comments/{comment_id}/private-reply", comment_id=comment_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                },
                comment_private_reply_params.CommentPrivateReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentPrivateReplyResponse,
        )

    async def reply(
        self,
        post_id: str,
        *,
        account_id: str,
        text: str,
        comment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentReplyResponse:
        """
        Reply to a comment

        Args:
          post_id: Post ID

          account_id: Account ID to reply from

          text: Reply text

          comment_id: Parent comment ID for threaded replies

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._post(
            path_template("/v1/inbox/comments/{post_id}/reply", post_id=post_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                    "comment_id": comment_id,
                },
                comment_reply_params.CommentReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentReplyResponse,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.retrieve = to_raw_response_wrapper(
            comments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            comments.list,
        )
        self.delete = to_raw_response_wrapper(
            comments.delete,
        )
        self.private_reply = to_raw_response_wrapper(
            comments.private_reply,
        )
        self.reply = to_raw_response_wrapper(
            comments.reply,
        )

    @cached_property
    def hide(self) -> HideResourceWithRawResponse:
        return HideResourceWithRawResponse(self._comments.hide)

    @cached_property
    def like(self) -> LikeResourceWithRawResponse:
        return LikeResourceWithRawResponse(self._comments.like)


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.retrieve = async_to_raw_response_wrapper(
            comments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            comments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            comments.delete,
        )
        self.private_reply = async_to_raw_response_wrapper(
            comments.private_reply,
        )
        self.reply = async_to_raw_response_wrapper(
            comments.reply,
        )

    @cached_property
    def hide(self) -> AsyncHideResourceWithRawResponse:
        return AsyncHideResourceWithRawResponse(self._comments.hide)

    @cached_property
    def like(self) -> AsyncLikeResourceWithRawResponse:
        return AsyncLikeResourceWithRawResponse(self._comments.like)


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.retrieve = to_streamed_response_wrapper(
            comments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = to_streamed_response_wrapper(
            comments.delete,
        )
        self.private_reply = to_streamed_response_wrapper(
            comments.private_reply,
        )
        self.reply = to_streamed_response_wrapper(
            comments.reply,
        )

    @cached_property
    def hide(self) -> HideResourceWithStreamingResponse:
        return HideResourceWithStreamingResponse(self._comments.hide)

    @cached_property
    def like(self) -> LikeResourceWithStreamingResponse:
        return LikeResourceWithStreamingResponse(self._comments.like)


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.retrieve = async_to_streamed_response_wrapper(
            comments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            comments.delete,
        )
        self.private_reply = async_to_streamed_response_wrapper(
            comments.private_reply,
        )
        self.reply = async_to_streamed_response_wrapper(
            comments.reply,
        )

    @cached_property
    def hide(self) -> AsyncHideResourceWithStreamingResponse:
        return AsyncHideResourceWithStreamingResponse(self._comments.hide)

    @cached_property
    def like(self) -> AsyncLikeResourceWithStreamingResponse:
        return AsyncLikeResourceWithStreamingResponse(self._comments.like)
