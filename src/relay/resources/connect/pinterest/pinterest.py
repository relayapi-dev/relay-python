# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .boards import (
    BoardsResource,
    AsyncBoardsResource,
    BoardsResourceWithRawResponse,
    AsyncBoardsResourceWithRawResponse,
    BoardsResourceWithStreamingResponse,
    AsyncBoardsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PinterestResource", "AsyncPinterestResource"]


class PinterestResource(SyncAPIResource):
    @cached_property
    def boards(self) -> BoardsResource:
        return BoardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PinterestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return PinterestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PinterestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return PinterestResourceWithStreamingResponse(self)


class AsyncPinterestResource(AsyncAPIResource):
    @cached_property
    def boards(self) -> AsyncBoardsResource:
        return AsyncBoardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPinterestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPinterestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPinterestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncPinterestResourceWithStreamingResponse(self)


class PinterestResourceWithRawResponse:
    def __init__(self, pinterest: PinterestResource) -> None:
        self._pinterest = pinterest

    @cached_property
    def boards(self) -> BoardsResourceWithRawResponse:
        return BoardsResourceWithRawResponse(self._pinterest.boards)


class AsyncPinterestResourceWithRawResponse:
    def __init__(self, pinterest: AsyncPinterestResource) -> None:
        self._pinterest = pinterest

    @cached_property
    def boards(self) -> AsyncBoardsResourceWithRawResponse:
        return AsyncBoardsResourceWithRawResponse(self._pinterest.boards)


class PinterestResourceWithStreamingResponse:
    def __init__(self, pinterest: PinterestResource) -> None:
        self._pinterest = pinterest

    @cached_property
    def boards(self) -> BoardsResourceWithStreamingResponse:
        return BoardsResourceWithStreamingResponse(self._pinterest.boards)


class AsyncPinterestResourceWithStreamingResponse:
    def __init__(self, pinterest: AsyncPinterestResource) -> None:
        self._pinterest = pinterest

    @cached_property
    def boards(self) -> AsyncBoardsResourceWithStreamingResponse:
        return AsyncBoardsResourceWithStreamingResponse(self._pinterest.boards)
