# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .follow import (
    FollowResource,
    AsyncFollowResource,
    FollowResourceWithRawResponse,
    AsyncFollowResourceWithRawResponse,
    FollowResourceWithStreamingResponse,
    AsyncFollowResourceWithStreamingResponse,
)
from .retweet import (
    RetweetResource,
    AsyncRetweetResource,
    RetweetResourceWithRawResponse,
    AsyncRetweetResourceWithRawResponse,
    RetweetResourceWithStreamingResponse,
    AsyncRetweetResourceWithStreamingResponse,
)
from .bookmark import (
    BookmarkResource,
    AsyncBookmarkResource,
    BookmarkResourceWithRawResponse,
    AsyncBookmarkResourceWithRawResponse,
    BookmarkResourceWithStreamingResponse,
    AsyncBookmarkResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TwitterResource", "AsyncTwitterResource"]


class TwitterResource(SyncAPIResource):
    @cached_property
    def retweet(self) -> RetweetResource:
        return RetweetResource(self._client)

    @cached_property
    def bookmark(self) -> BookmarkResource:
        return BookmarkResource(self._client)

    @cached_property
    def follow(self) -> FollowResource:
        return FollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> TwitterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return TwitterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TwitterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return TwitterResourceWithStreamingResponse(self)


class AsyncTwitterResource(AsyncAPIResource):
    @cached_property
    def retweet(self) -> AsyncRetweetResource:
        return AsyncRetweetResource(self._client)

    @cached_property
    def bookmark(self) -> AsyncBookmarkResource:
        return AsyncBookmarkResource(self._client)

    @cached_property
    def follow(self) -> AsyncFollowResource:
        return AsyncFollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTwitterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTwitterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTwitterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncTwitterResourceWithStreamingResponse(self)


class TwitterResourceWithRawResponse:
    def __init__(self, twitter: TwitterResource) -> None:
        self._twitter = twitter

    @cached_property
    def retweet(self) -> RetweetResourceWithRawResponse:
        return RetweetResourceWithRawResponse(self._twitter.retweet)

    @cached_property
    def bookmark(self) -> BookmarkResourceWithRawResponse:
        return BookmarkResourceWithRawResponse(self._twitter.bookmark)

    @cached_property
    def follow(self) -> FollowResourceWithRawResponse:
        return FollowResourceWithRawResponse(self._twitter.follow)


class AsyncTwitterResourceWithRawResponse:
    def __init__(self, twitter: AsyncTwitterResource) -> None:
        self._twitter = twitter

    @cached_property
    def retweet(self) -> AsyncRetweetResourceWithRawResponse:
        return AsyncRetweetResourceWithRawResponse(self._twitter.retweet)

    @cached_property
    def bookmark(self) -> AsyncBookmarkResourceWithRawResponse:
        return AsyncBookmarkResourceWithRawResponse(self._twitter.bookmark)

    @cached_property
    def follow(self) -> AsyncFollowResourceWithRawResponse:
        return AsyncFollowResourceWithRawResponse(self._twitter.follow)


class TwitterResourceWithStreamingResponse:
    def __init__(self, twitter: TwitterResource) -> None:
        self._twitter = twitter

    @cached_property
    def retweet(self) -> RetweetResourceWithStreamingResponse:
        return RetweetResourceWithStreamingResponse(self._twitter.retweet)

    @cached_property
    def bookmark(self) -> BookmarkResourceWithStreamingResponse:
        return BookmarkResourceWithStreamingResponse(self._twitter.bookmark)

    @cached_property
    def follow(self) -> FollowResourceWithStreamingResponse:
        return FollowResourceWithStreamingResponse(self._twitter.follow)


class AsyncTwitterResourceWithStreamingResponse:
    def __init__(self, twitter: AsyncTwitterResource) -> None:
        self._twitter = twitter

    @cached_property
    def retweet(self) -> AsyncRetweetResourceWithStreamingResponse:
        return AsyncRetweetResourceWithStreamingResponse(self._twitter.retweet)

    @cached_property
    def bookmark(self) -> AsyncBookmarkResourceWithStreamingResponse:
        return AsyncBookmarkResourceWithStreamingResponse(self._twitter.bookmark)

    @cached_property
    def follow(self) -> AsyncFollowResourceWithStreamingResponse:
        return AsyncFollowResourceWithStreamingResponse(self._twitter.follow)
