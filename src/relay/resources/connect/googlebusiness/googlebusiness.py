# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GooglebusinessResource", "AsyncGooglebusinessResource"]


class GooglebusinessResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GooglebusinessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return GooglebusinessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GooglebusinessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return GooglebusinessResourceWithStreamingResponse(self)


class AsyncGooglebusinessResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGooglebusinessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGooglebusinessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGooglebusinessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncGooglebusinessResourceWithStreamingResponse(self)


class GooglebusinessResourceWithRawResponse:
    def __init__(self, googlebusiness: GooglebusinessResource) -> None:
        self._googlebusiness = googlebusiness

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._googlebusiness.locations)


class AsyncGooglebusinessResourceWithRawResponse:
    def __init__(self, googlebusiness: AsyncGooglebusinessResource) -> None:
        self._googlebusiness = googlebusiness

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._googlebusiness.locations)


class GooglebusinessResourceWithStreamingResponse:
    def __init__(self, googlebusiness: GooglebusinessResource) -> None:
        self._googlebusiness = googlebusiness

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._googlebusiness.locations)


class AsyncGooglebusinessResourceWithStreamingResponse:
    def __init__(self, googlebusiness: AsyncGooglebusinessResource) -> None:
        self._googlebusiness = googlebusiness

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._googlebusiness.locations)
