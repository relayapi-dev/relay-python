# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .validate import (
    ValidateResource,
    AsyncValidateResource,
    ValidateResourceWithRawResponse,
    AsyncValidateResourceWithRawResponse,
    ValidateResourceWithStreamingResponse,
    AsyncValidateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .instagram import (
    InstagramResource,
    AsyncInstagramResource,
    InstagramResourceWithRawResponse,
    AsyncInstagramResourceWithRawResponse,
    InstagramResourceWithStreamingResponse,
    AsyncInstagramResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def validate(self) -> ValidateResource:
        return ValidateResource(self._client)

    @cached_property
    def instagram(self) -> InstagramResource:
        return InstagramResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def validate(self) -> AsyncValidateResource:
        return AsyncValidateResource(self._client)

    @cached_property
    def instagram(self) -> AsyncInstagramResource:
        return AsyncInstagramResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

    @cached_property
    def validate(self) -> ValidateResourceWithRawResponse:
        return ValidateResourceWithRawResponse(self._tools.validate)

    @cached_property
    def instagram(self) -> InstagramResourceWithRawResponse:
        return InstagramResourceWithRawResponse(self._tools.instagram)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

    @cached_property
    def validate(self) -> AsyncValidateResourceWithRawResponse:
        return AsyncValidateResourceWithRawResponse(self._tools.validate)

    @cached_property
    def instagram(self) -> AsyncInstagramResourceWithRawResponse:
        return AsyncInstagramResourceWithRawResponse(self._tools.instagram)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

    @cached_property
    def validate(self) -> ValidateResourceWithStreamingResponse:
        return ValidateResourceWithStreamingResponse(self._tools.validate)

    @cached_property
    def instagram(self) -> InstagramResourceWithStreamingResponse:
        return InstagramResourceWithStreamingResponse(self._tools.instagram)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

    @cached_property
    def validate(self) -> AsyncValidateResourceWithStreamingResponse:
        return AsyncValidateResourceWithStreamingResponse(self._tools.validate)

    @cached_property
    def instagram(self) -> AsyncInstagramResourceWithStreamingResponse:
        return AsyncInstagramResourceWithStreamingResponse(self._tools.instagram)
