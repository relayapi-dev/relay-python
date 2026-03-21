# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.connect.pinterest import board_select_params
from ....types.connect.pinterest.board_list_response import BoardListResponse
from ....types.connect.pinterest.board_select_response import BoardSelectResponse

__all__ = ["BoardsResource", "AsyncBoardsResource"]


class BoardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BoardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return BoardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BoardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return BoardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoardListResponse:
        """List Pinterest boards after OAuth"""
        return self._get(
            "/v1/connect/pinterest/boards",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoardListResponse,
        )

    def select(
        self,
        *,
        board_id: str,
        connect_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoardSelectResponse:
        """
        Select Pinterest board

        Args:
          board_id: Selected Pinterest board ID

          connect_token: Token from pending data or OAuth flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connect/pinterest/boards",
            body=maybe_transform(
                {
                    "board_id": board_id,
                    "connect_token": connect_token,
                },
                board_select_params.BoardSelectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoardSelectResponse,
        )


class AsyncBoardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBoardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBoardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBoardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncBoardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoardListResponse:
        """List Pinterest boards after OAuth"""
        return await self._get(
            "/v1/connect/pinterest/boards",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoardListResponse,
        )

    async def select(
        self,
        *,
        board_id: str,
        connect_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoardSelectResponse:
        """
        Select Pinterest board

        Args:
          board_id: Selected Pinterest board ID

          connect_token: Token from pending data or OAuth flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connect/pinterest/boards",
            body=await async_maybe_transform(
                {
                    "board_id": board_id,
                    "connect_token": connect_token,
                },
                board_select_params.BoardSelectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoardSelectResponse,
        )


class BoardsResourceWithRawResponse:
    def __init__(self, boards: BoardsResource) -> None:
        self._boards = boards

        self.list = to_raw_response_wrapper(
            boards.list,
        )
        self.select = to_raw_response_wrapper(
            boards.select,
        )


class AsyncBoardsResourceWithRawResponse:
    def __init__(self, boards: AsyncBoardsResource) -> None:
        self._boards = boards

        self.list = async_to_raw_response_wrapper(
            boards.list,
        )
        self.select = async_to_raw_response_wrapper(
            boards.select,
        )


class BoardsResourceWithStreamingResponse:
    def __init__(self, boards: BoardsResource) -> None:
        self._boards = boards

        self.list = to_streamed_response_wrapper(
            boards.list,
        )
        self.select = to_streamed_response_wrapper(
            boards.select,
        )


class AsyncBoardsResourceWithStreamingResponse:
    def __init__(self, boards: AsyncBoardsResource) -> None:
        self._boards = boards

        self.list = async_to_streamed_response_wrapper(
            boards.list,
        )
        self.select = async_to_streamed_response_wrapper(
            boards.select,
        )
