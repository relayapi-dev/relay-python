# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .slots import (
    SlotsResource,
    AsyncSlotsResource,
    SlotsResourceWithRawResponse,
    AsyncSlotsResourceWithRawResponse,
    SlotsResourceWithStreamingResponse,
    AsyncSlotsResourceWithStreamingResponse,
)
from ...types import queue_preview_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.queue_preview_response import QueuePreviewResponse
from ...types.queue_get_next_slot_response import QueueGetNextSlotResponse

__all__ = ["QueueResource", "AsyncQueueResource"]


class QueueResource(SyncAPIResource):
    @cached_property
    def slots(self) -> SlotsResource:
        return SlotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> QueueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return QueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return QueueResourceWithStreamingResponse(self)

    def get_next_slot(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueGetNextSlotResponse:
        """Get next available queue slot"""
        return self._get(
            "/v1/queue/next-slot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueGetNextSlotResponse,
        )

    def preview(
        self,
        *,
        count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueuePreviewResponse:
        """
        Preview upcoming queue slots

        Args:
          count: Number of upcoming slots to preview

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/queue/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"count": count}, queue_preview_params.QueuePreviewParams),
            ),
            cast_to=QueuePreviewResponse,
        )


class AsyncQueueResource(AsyncAPIResource):
    @cached_property
    def slots(self) -> AsyncSlotsResource:
        return AsyncSlotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQueueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncQueueResourceWithStreamingResponse(self)

    async def get_next_slot(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueGetNextSlotResponse:
        """Get next available queue slot"""
        return await self._get(
            "/v1/queue/next-slot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueGetNextSlotResponse,
        )

    async def preview(
        self,
        *,
        count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueuePreviewResponse:
        """
        Preview upcoming queue slots

        Args:
          count: Number of upcoming slots to preview

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/queue/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"count": count}, queue_preview_params.QueuePreviewParams),
            ),
            cast_to=QueuePreviewResponse,
        )


class QueueResourceWithRawResponse:
    def __init__(self, queue: QueueResource) -> None:
        self._queue = queue

        self.get_next_slot = to_raw_response_wrapper(
            queue.get_next_slot,
        )
        self.preview = to_raw_response_wrapper(
            queue.preview,
        )

    @cached_property
    def slots(self) -> SlotsResourceWithRawResponse:
        return SlotsResourceWithRawResponse(self._queue.slots)


class AsyncQueueResourceWithRawResponse:
    def __init__(self, queue: AsyncQueueResource) -> None:
        self._queue = queue

        self.get_next_slot = async_to_raw_response_wrapper(
            queue.get_next_slot,
        )
        self.preview = async_to_raw_response_wrapper(
            queue.preview,
        )

    @cached_property
    def slots(self) -> AsyncSlotsResourceWithRawResponse:
        return AsyncSlotsResourceWithRawResponse(self._queue.slots)


class QueueResourceWithStreamingResponse:
    def __init__(self, queue: QueueResource) -> None:
        self._queue = queue

        self.get_next_slot = to_streamed_response_wrapper(
            queue.get_next_slot,
        )
        self.preview = to_streamed_response_wrapper(
            queue.preview,
        )

    @cached_property
    def slots(self) -> SlotsResourceWithStreamingResponse:
        return SlotsResourceWithStreamingResponse(self._queue.slots)


class AsyncQueueResourceWithStreamingResponse:
    def __init__(self, queue: AsyncQueueResource) -> None:
        self._queue = queue

        self.get_next_slot = async_to_streamed_response_wrapper(
            queue.get_next_slot,
        )
        self.preview = async_to_streamed_response_wrapper(
            queue.preview,
        )

    @cached_property
    def slots(self) -> AsyncSlotsResourceWithStreamingResponse:
        return AsyncSlotsResourceWithStreamingResponse(self._queue.slots)
