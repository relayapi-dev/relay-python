# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.whatsapp import broadcast_list_params, broadcast_create_params
from ...types.whatsapp.broadcast_list_response import BroadcastListResponse
from ...types.whatsapp.broadcast_send_response import BroadcastSendResponse
from ...types.whatsapp.broadcast_create_response import BroadcastCreateResponse
from ...types.whatsapp.broadcast_retrieve_response import BroadcastRetrieveResponse
from ...types.whatsapp.broadcast_schedule_response import BroadcastScheduleResponse

__all__ = ["BroadcastsResource", "AsyncBroadcastsResource"]


class BroadcastsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return BroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return BroadcastsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        recipients: Iterable[broadcast_create_params.Recipient],
        template: broadcast_create_params.Template,
        scheduled_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCreateResponse:
        """
        Create a broadcast

        Args:
          account_id: WhatsApp account ID

          name: Broadcast name

          recipients: Recipient list

          scheduled_at: ISO 8601 timestamp to schedule send

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/whatsapp/broadcasts",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "recipients": recipients,
                    "template": template,
                    "scheduled_at": scheduled_at,
                },
                broadcast_create_params.BroadcastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastCreateResponse,
        )

    def retrieve(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRetrieveResponse:
        """
        Get broadcast details

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastListResponse:
        """
        List broadcasts

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/whatsapp/broadcasts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, broadcast_list_params.BroadcastListParams),
            ),
            cast_to=BroadcastListResponse,
        )

    def delete(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a broadcast

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def schedule(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastScheduleResponse:
        """
        Schedule a broadcast

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}/schedule", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastScheduleResponse,
        )

    def send(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSendResponse:
        """
        Send a broadcast immediately

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}/send", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastSendResponse,
        )


class AsyncBroadcastsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncBroadcastsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        recipients: Iterable[broadcast_create_params.Recipient],
        template: broadcast_create_params.Template,
        scheduled_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCreateResponse:
        """
        Create a broadcast

        Args:
          account_id: WhatsApp account ID

          name: Broadcast name

          recipients: Recipient list

          scheduled_at: ISO 8601 timestamp to schedule send

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/whatsapp/broadcasts",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "recipients": recipients,
                    "template": template,
                    "scheduled_at": scheduled_at,
                },
                broadcast_create_params.BroadcastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastCreateResponse,
        )

    async def retrieve(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRetrieveResponse:
        """
        Get broadcast details

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._get(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastListResponse:
        """
        List broadcasts

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/whatsapp/broadcasts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, broadcast_list_params.BroadcastListParams
                ),
            ),
            cast_to=BroadcastListResponse,
        )

    async def delete(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a broadcast

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def schedule(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastScheduleResponse:
        """
        Schedule a broadcast

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}/schedule", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastScheduleResponse,
        )

    async def send(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSendResponse:
        """
        Send a broadcast immediately

        Args:
          broadcast_id: Broadcast ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            path_template("/v1/whatsapp/broadcasts/{broadcast_id}/send", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastSendResponse,
        )


class BroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_raw_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            broadcasts.list,
        )
        self.delete = to_raw_response_wrapper(
            broadcasts.delete,
        )
        self.schedule = to_raw_response_wrapper(
            broadcasts.schedule,
        )
        self.send = to_raw_response_wrapper(
            broadcasts.send,
        )


class AsyncBroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_raw_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            broadcasts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            broadcasts.delete,
        )
        self.schedule = async_to_raw_response_wrapper(
            broadcasts.schedule,
        )
        self.send = async_to_raw_response_wrapper(
            broadcasts.send,
        )


class BroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.delete = to_streamed_response_wrapper(
            broadcasts.delete,
        )
        self.schedule = to_streamed_response_wrapper(
            broadcasts.schedule,
        )
        self.send = to_streamed_response_wrapper(
            broadcasts.send,
        )


class AsyncBroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            broadcasts.delete,
        )
        self.schedule = async_to_streamed_response_wrapper(
            broadcasts.schedule,
        )
        self.send = async_to_streamed_response_wrapper(
            broadcasts.send,
        )
