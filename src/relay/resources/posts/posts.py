# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ...types import post_list_params, post_create_params, post_update_params, post_bulk_create_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.post_list_response import PostListResponse
from ...types.post_retry_response import PostRetryResponse
from ...types.post_create_response import PostCreateResponse
from ...types.post_update_response import PostUpdateResponse
from ...types.post_retrieve_response import PostRetrieveResponse
from ...types.post_unpublish_response import PostUnpublishResponse
from ...types.post_bulk_create_response import PostBulkCreateResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        scheduled_at: str,
        targets: SequenceNotStr[str],
        content: str | Omit = omit,
        media: Iterable[post_create_params.Media] | Omit = omit,
        target_options: Dict[str, Dict[str, Optional[object]]] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostCreateResponse:
        """Create a post.

        Use scheduled_at: "now" to publish immediately, "draft" to save
        as draft, or an ISO timestamp to schedule.

        Args:
          scheduled_at: Publish intent. Use "now" to publish immediately, "draft" to save as draft, or
              an ISO 8601 timestamp to schedule.

          targets: Account IDs or platform names to publish to

          content: Post text. Optional if target_options provide per-target content.

          media: Media attachments

          target_options: Per-target customizations keyed by target value (account ID or platform name)

          timezone: IANA timezone for scheduling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/posts",
            body=maybe_transform(
                {
                    "scheduled_at": scheduled_at,
                    "targets": targets,
                    "content": content,
                    "media": media,
                    "target_options": target_options,
                    "timezone": timezone,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )

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
    ) -> PostRetrieveResponse:
        """
        Get a post

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
            path_template("/v1/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        content: str | Omit = omit,
        media: Iterable[post_update_params.Media] | Omit = omit,
        scheduled_at: str | Omit = omit,
        target_options: Dict[str, Dict[str, Optional[object]]] | Omit = omit,
        targets: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostUpdateResponse:
        """
        Update a draft or scheduled post.

        Args:
          id: Resource ID

          content: Post text

          media: Updated media

          scheduled_at: Publish intent. Use "now" to publish immediately, "draft" to save as draft, or
              an ISO 8601 timestamp to schedule.

          targets: Updated targets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/posts/{id}", id=id),
            body=maybe_transform(
                {
                    "content": content,
                    "media": media,
                    "scheduled_at": scheduled_at,
                    "target_options": target_options,
                    "targets": targets,
                    "timezone": timezone,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostListResponse:
        """
        List posts

        Args:
          cursor: Pagination cursor

          limit: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/posts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a draft or scheduled post.

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk_create(
        self,
        *,
        posts: Iterable[post_bulk_create_params.Post],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostBulkCreateResponse:
        """Create multiple posts in a single request.

        Each item follows the same schema as
        single post creation.

        Args:
          posts: Array of posts to create (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/posts/bulk",
            body=maybe_transform({"posts": posts}, post_bulk_create_params.PostBulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostBulkCreateResponse,
        )

    def retry(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostRetryResponse:
        """
        Retry publishing for failed targets on a post.

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/posts/{id}/retry", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetryResponse,
        )

    def unpublish(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostUnpublishResponse:
        """
        Attempt to delete the post from each platform and set the post status to
        cancelled.

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/posts/{id}/unpublish", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUnpublishResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        scheduled_at: str,
        targets: SequenceNotStr[str],
        content: str | Omit = omit,
        media: Iterable[post_create_params.Media] | Omit = omit,
        target_options: Dict[str, Dict[str, Optional[object]]] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostCreateResponse:
        """Create a post.

        Use scheduled_at: "now" to publish immediately, "draft" to save
        as draft, or an ISO timestamp to schedule.

        Args:
          scheduled_at: Publish intent. Use "now" to publish immediately, "draft" to save as draft, or
              an ISO 8601 timestamp to schedule.

          targets: Account IDs or platform names to publish to

          content: Post text. Optional if target_options provide per-target content.

          media: Media attachments

          target_options: Per-target customizations keyed by target value (account ID or platform name)

          timezone: IANA timezone for scheduling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/posts",
            body=await async_maybe_transform(
                {
                    "scheduled_at": scheduled_at,
                    "targets": targets,
                    "content": content,
                    "media": media,
                    "target_options": target_options,
                    "timezone": timezone,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )

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
    ) -> PostRetrieveResponse:
        """
        Get a post

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
            path_template("/v1/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        content: str | Omit = omit,
        media: Iterable[post_update_params.Media] | Omit = omit,
        scheduled_at: str | Omit = omit,
        target_options: Dict[str, Dict[str, Optional[object]]] | Omit = omit,
        targets: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostUpdateResponse:
        """
        Update a draft or scheduled post.

        Args:
          id: Resource ID

          content: Post text

          media: Updated media

          scheduled_at: Publish intent. Use "now" to publish immediately, "draft" to save as draft, or
              an ISO 8601 timestamp to schedule.

          targets: Updated targets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/posts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "media": media,
                    "scheduled_at": scheduled_at,
                    "target_options": target_options,
                    "targets": targets,
                    "timezone": timezone,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUpdateResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostListResponse:
        """
        List posts

        Args:
          cursor: Pagination cursor

          limit: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/posts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a draft or scheduled post.

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk_create(
        self,
        *,
        posts: Iterable[post_bulk_create_params.Post],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostBulkCreateResponse:
        """Create multiple posts in a single request.

        Each item follows the same schema as
        single post creation.

        Args:
          posts: Array of posts to create (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/posts/bulk",
            body=await async_maybe_transform({"posts": posts}, post_bulk_create_params.PostBulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostBulkCreateResponse,
        )

    async def retry(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostRetryResponse:
        """
        Retry publishing for failed targets on a post.

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/posts/{id}/retry", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetryResponse,
        )

    async def unpublish(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostUnpublishResponse:
        """
        Attempt to delete the post from each platform and set the post status to
        cancelled.

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/posts/{id}/unpublish", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUnpublishResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            posts.update,
        )
        self.list = to_raw_response_wrapper(
            posts.list,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            posts.bulk_create,
        )
        self.retry = to_raw_response_wrapper(
            posts.retry,
        )
        self.unpublish = to_raw_response_wrapper(
            posts.unpublish,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._posts.logs)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.list = async_to_raw_response_wrapper(
            posts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            posts.bulk_create,
        )
        self.retry = async_to_raw_response_wrapper(
            posts.retry,
        )
        self.unpublish = async_to_raw_response_wrapper(
            posts.unpublish,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._posts.logs)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.list = to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            posts.bulk_create,
        )
        self.retry = to_streamed_response_wrapper(
            posts.retry,
        )
        self.unpublish = to_streamed_response_wrapper(
            posts.unpublish,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._posts.logs)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            posts.bulk_create,
        )
        self.retry = async_to_streamed_response_wrapper(
            posts.retry,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            posts.unpublish,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._posts.logs)
