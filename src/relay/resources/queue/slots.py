# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.queue import slot_create_params, slot_update_params
from ..._base_client import make_request_options
from ...types.queue.slot_list_response import SlotListResponse
from ...types.queue.slot_create_response import SlotCreateResponse
from ...types.queue.slot_update_response import SlotUpdateResponse

__all__ = ["SlotsResource", "AsyncSlotsResource"]


class SlotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return SlotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return SlotsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        slots: Iterable[slot_create_params.Slot],
        timezone: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlotCreateResponse:
        """
        Create a queue schedule

        Args:
          slots: Time slots

          timezone: Default timezone for slots

          name: Schedule name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/queue/slots",
            body=maybe_transform(
                {
                    "slots": slots,
                    "timezone": timezone,
                    "name": name,
                },
                slot_create_params.SlotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotCreateResponse,
        )

    def update(
        self,
        *,
        name: str | Omit = omit,
        set_as_default: bool | Omit = omit,
        slots: Iterable[slot_update_params.Slot] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlotUpdateResponse:
        """
        Update queue schedule

        Args:
          name: Schedule name

          set_as_default: Set this schedule as the default

          slots: Updated time slots

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/queue/slots",
            body=maybe_transform(
                {
                    "name": name,
                    "set_as_default": set_as_default,
                    "slots": slots,
                },
                slot_update_params.SlotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlotListResponse:
        """List queue schedules"""
        return self._get(
            "/v1/queue/slots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotListResponse,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete queue schedule"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v1/queue/slots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSlotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSlotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncSlotsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        slots: Iterable[slot_create_params.Slot],
        timezone: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlotCreateResponse:
        """
        Create a queue schedule

        Args:
          slots: Time slots

          timezone: Default timezone for slots

          name: Schedule name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/queue/slots",
            body=await async_maybe_transform(
                {
                    "slots": slots,
                    "timezone": timezone,
                    "name": name,
                },
                slot_create_params.SlotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotCreateResponse,
        )

    async def update(
        self,
        *,
        name: str | Omit = omit,
        set_as_default: bool | Omit = omit,
        slots: Iterable[slot_update_params.Slot] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlotUpdateResponse:
        """
        Update queue schedule

        Args:
          name: Schedule name

          set_as_default: Set this schedule as the default

          slots: Updated time slots

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/queue/slots",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "set_as_default": set_as_default,
                    "slots": slots,
                },
                slot_update_params.SlotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlotListResponse:
        """List queue schedules"""
        return await self._get(
            "/v1/queue/slots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotListResponse,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete queue schedule"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v1/queue/slots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SlotsResourceWithRawResponse:
    def __init__(self, slots: SlotsResource) -> None:
        self._slots = slots

        self.create = to_raw_response_wrapper(
            slots.create,
        )
        self.update = to_raw_response_wrapper(
            slots.update,
        )
        self.list = to_raw_response_wrapper(
            slots.list,
        )
        self.delete = to_raw_response_wrapper(
            slots.delete,
        )


class AsyncSlotsResourceWithRawResponse:
    def __init__(self, slots: AsyncSlotsResource) -> None:
        self._slots = slots

        self.create = async_to_raw_response_wrapper(
            slots.create,
        )
        self.update = async_to_raw_response_wrapper(
            slots.update,
        )
        self.list = async_to_raw_response_wrapper(
            slots.list,
        )
        self.delete = async_to_raw_response_wrapper(
            slots.delete,
        )


class SlotsResourceWithStreamingResponse:
    def __init__(self, slots: SlotsResource) -> None:
        self._slots = slots

        self.create = to_streamed_response_wrapper(
            slots.create,
        )
        self.update = to_streamed_response_wrapper(
            slots.update,
        )
        self.list = to_streamed_response_wrapper(
            slots.list,
        )
        self.delete = to_streamed_response_wrapper(
            slots.delete,
        )


class AsyncSlotsResourceWithStreamingResponse:
    def __init__(self, slots: AsyncSlotsResource) -> None:
        self._slots = slots

        self.create = async_to_streamed_response_wrapper(
            slots.create,
        )
        self.update = async_to_streamed_response_wrapper(
            slots.update,
        )
        self.list = async_to_streamed_response_wrapper(
            slots.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            slots.delete,
        )
