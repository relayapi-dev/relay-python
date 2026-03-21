# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SnapchatResource", "AsyncSnapchatResource"]


class SnapchatResource(SyncAPIResource):
    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SnapchatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return SnapchatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapchatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return SnapchatResourceWithStreamingResponse(self)


class AsyncSnapchatResource(AsyncAPIResource):
    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSnapchatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapchatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapchatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncSnapchatResourceWithStreamingResponse(self)


class SnapchatResourceWithRawResponse:
    def __init__(self, snapchat: SnapchatResource) -> None:
        self._snapchat = snapchat

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._snapchat.profiles)


class AsyncSnapchatResourceWithRawResponse:
    def __init__(self, snapchat: AsyncSnapchatResource) -> None:
        self._snapchat = snapchat

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._snapchat.profiles)


class SnapchatResourceWithStreamingResponse:
    def __init__(self, snapchat: SnapchatResource) -> None:
        self._snapchat = snapchat

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._snapchat.profiles)


class AsyncSnapchatResourceWithStreamingResponse:
    def __init__(self, snapchat: AsyncSnapchatResource) -> None:
        self._snapchat = snapchat

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._snapchat.profiles)
