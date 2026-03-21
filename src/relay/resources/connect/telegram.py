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
from ...types.connect import telegram_connect_directly_params, telegram_poll_connection_status_params
from ...types.connect.telegram_connect_directly_response import TelegramConnectDirectlyResponse
from ...types.connect.telegram_initiate_connection_response import TelegramInitiateConnectionResponse
from ...types.connect.telegram_poll_connection_status_response import TelegramPollConnectionStatusResponse

__all__ = ["TelegramResource", "AsyncTelegramResource"]


class TelegramResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return TelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return TelegramResourceWithStreamingResponse(self)

    def connect_directly(
        self,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramConnectDirectlyResponse:
        """
        Connect Telegram directly with chat ID

        Args:
          chat_id: Telegram chat or channel ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connect/telegram/direct",
            body=maybe_transform({"chat_id": chat_id}, telegram_connect_directly_params.TelegramConnectDirectlyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelegramConnectDirectlyResponse,
        )

    def initiate_connection(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramInitiateConnectionResponse:
        """Generates a 6-character access code (valid 15 minutes)."""
        return self._post(
            "/v1/connect/telegram",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelegramInitiateConnectionResponse,
        )

    def poll_connection_status(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramPollConnectionStatusResponse:
        """
        Poll Telegram connection status

        Args:
          code: The 6-character access code to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connect/telegram",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"code": code}, telegram_poll_connection_status_params.TelegramPollConnectionStatusParams
                ),
            ),
            cast_to=TelegramPollConnectionStatusResponse,
        )


class AsyncTelegramResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncTelegramResourceWithStreamingResponse(self)

    async def connect_directly(
        self,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramConnectDirectlyResponse:
        """
        Connect Telegram directly with chat ID

        Args:
          chat_id: Telegram chat or channel ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connect/telegram/direct",
            body=await async_maybe_transform(
                {"chat_id": chat_id}, telegram_connect_directly_params.TelegramConnectDirectlyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelegramConnectDirectlyResponse,
        )

    async def initiate_connection(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramInitiateConnectionResponse:
        """Generates a 6-character access code (valid 15 minutes)."""
        return await self._post(
            "/v1/connect/telegram",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelegramInitiateConnectionResponse,
        )

    async def poll_connection_status(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramPollConnectionStatusResponse:
        """
        Poll Telegram connection status

        Args:
          code: The 6-character access code to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connect/telegram",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"code": code}, telegram_poll_connection_status_params.TelegramPollConnectionStatusParams
                ),
            ),
            cast_to=TelegramPollConnectionStatusResponse,
        )


class TelegramResourceWithRawResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.connect_directly = to_raw_response_wrapper(
            telegram.connect_directly,
        )
        self.initiate_connection = to_raw_response_wrapper(
            telegram.initiate_connection,
        )
        self.poll_connection_status = to_raw_response_wrapper(
            telegram.poll_connection_status,
        )


class AsyncTelegramResourceWithRawResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.connect_directly = async_to_raw_response_wrapper(
            telegram.connect_directly,
        )
        self.initiate_connection = async_to_raw_response_wrapper(
            telegram.initiate_connection,
        )
        self.poll_connection_status = async_to_raw_response_wrapper(
            telegram.poll_connection_status,
        )


class TelegramResourceWithStreamingResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.connect_directly = to_streamed_response_wrapper(
            telegram.connect_directly,
        )
        self.initiate_connection = to_streamed_response_wrapper(
            telegram.initiate_connection,
        )
        self.poll_connection_status = to_streamed_response_wrapper(
            telegram.poll_connection_status,
        )


class AsyncTelegramResourceWithStreamingResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.connect_directly = async_to_streamed_response_wrapper(
            telegram.connect_directly,
        )
        self.initiate_connection = async_to_streamed_response_wrapper(
            telegram.initiate_connection,
        )
        self.poll_connection_status = async_to_streamed_response_wrapper(
            telegram.poll_connection_status,
        )
