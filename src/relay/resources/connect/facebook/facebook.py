# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FacebookResource", "AsyncFacebookResource"]


class FacebookResource(SyncAPIResource):
    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FacebookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return FacebookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FacebookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return FacebookResourceWithStreamingResponse(self)


class AsyncFacebookResource(AsyncAPIResource):
    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFacebookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFacebookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFacebookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncFacebookResourceWithStreamingResponse(self)


class FacebookResourceWithRawResponse:
    def __init__(self, facebook: FacebookResource) -> None:
        self._facebook = facebook

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._facebook.pages)


class AsyncFacebookResourceWithRawResponse:
    def __init__(self, facebook: AsyncFacebookResource) -> None:
        self._facebook = facebook

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._facebook.pages)


class FacebookResourceWithStreamingResponse:
    def __init__(self, facebook: FacebookResource) -> None:
        self._facebook = facebook

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._facebook.pages)


class AsyncFacebookResourceWithStreamingResponse:
    def __init__(self, facebook: AsyncFacebookResource) -> None:
        self._facebook = facebook

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._facebook.pages)
