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
from ...types.accounts import pinterest_board_set_default_params
from ...types.accounts.pinterest_board_retrieve_response import PinterestBoardRetrieveResponse
from ...types.accounts.pinterest_board_set_default_response import PinterestBoardSetDefaultResponse

__all__ = ["PinterestBoardsResource", "AsyncPinterestBoardsResource"]


class PinterestBoardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PinterestBoardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return PinterestBoardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PinterestBoardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return PinterestBoardsResourceWithStreamingResponse(self)

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
    ) -> PinterestBoardRetrieveResponse:
        """
        Fetch Pinterest boards for an account

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
            path_template("/v1/accounts/{id}/pinterest-boards", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinterestBoardRetrieveResponse,
        )

    def set_default(
        self,
        id: str,
        *,
        board_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinterestBoardSetDefaultResponse:
        """
        Set default Pinterest board

        Args:
          id: Resource ID

          board_id: Pinterest board ID to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/accounts/{id}/pinterest-boards", id=id),
            body=maybe_transform(
                {"board_id": board_id}, pinterest_board_set_default_params.PinterestBoardSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinterestBoardSetDefaultResponse,
        )


class AsyncPinterestBoardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPinterestBoardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPinterestBoardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPinterestBoardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncPinterestBoardsResourceWithStreamingResponse(self)

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
    ) -> PinterestBoardRetrieveResponse:
        """
        Fetch Pinterest boards for an account

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
            path_template("/v1/accounts/{id}/pinterest-boards", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinterestBoardRetrieveResponse,
        )

    async def set_default(
        self,
        id: str,
        *,
        board_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinterestBoardSetDefaultResponse:
        """
        Set default Pinterest board

        Args:
          id: Resource ID

          board_id: Pinterest board ID to set as default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/accounts/{id}/pinterest-boards", id=id),
            body=await async_maybe_transform(
                {"board_id": board_id}, pinterest_board_set_default_params.PinterestBoardSetDefaultParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinterestBoardSetDefaultResponse,
        )


class PinterestBoardsResourceWithRawResponse:
    def __init__(self, pinterest_boards: PinterestBoardsResource) -> None:
        self._pinterest_boards = pinterest_boards

        self.retrieve = to_raw_response_wrapper(
            pinterest_boards.retrieve,
        )
        self.set_default = to_raw_response_wrapper(
            pinterest_boards.set_default,
        )


class AsyncPinterestBoardsResourceWithRawResponse:
    def __init__(self, pinterest_boards: AsyncPinterestBoardsResource) -> None:
        self._pinterest_boards = pinterest_boards

        self.retrieve = async_to_raw_response_wrapper(
            pinterest_boards.retrieve,
        )
        self.set_default = async_to_raw_response_wrapper(
            pinterest_boards.set_default,
        )


class PinterestBoardsResourceWithStreamingResponse:
    def __init__(self, pinterest_boards: PinterestBoardsResource) -> None:
        self._pinterest_boards = pinterest_boards

        self.retrieve = to_streamed_response_wrapper(
            pinterest_boards.retrieve,
        )
        self.set_default = to_streamed_response_wrapper(
            pinterest_boards.set_default,
        )


class AsyncPinterestBoardsResourceWithStreamingResponse:
    def __init__(self, pinterest_boards: AsyncPinterestBoardsResource) -> None:
        self._pinterest_boards = pinterest_boards

        self.retrieve = async_to_streamed_response_wrapper(
            pinterest_boards.retrieve,
        )
        self.set_default = async_to_streamed_response_wrapper(
            pinterest_boards.set_default,
        )
