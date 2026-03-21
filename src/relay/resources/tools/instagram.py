# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tools import instagram_check_hashtag_safety_params
from ..._base_client import make_request_options
from ...types.tools.instagram_check_hashtag_safety_response import InstagramCheckHashtagSafetyResponse

__all__ = ["InstagramResource", "AsyncInstagramResource"]


class InstagramResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstagramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return InstagramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstagramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return InstagramResourceWithStreamingResponse(self)

    def check_hashtag_safety(
        self,
        *,
        hashtags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramCheckHashtagSafetyResponse:
        """
        Check Instagram hashtag safety status

        Args:
          hashtags: Hashtags to check (without # prefix)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/instagram/hashtag-checker",
            body=maybe_transform(
                {"hashtags": hashtags}, instagram_check_hashtag_safety_params.InstagramCheckHashtagSafetyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramCheckHashtagSafetyResponse,
        )


class AsyncInstagramResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstagramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstagramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstagramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncInstagramResourceWithStreamingResponse(self)

    async def check_hashtag_safety(
        self,
        *,
        hashtags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramCheckHashtagSafetyResponse:
        """
        Check Instagram hashtag safety status

        Args:
          hashtags: Hashtags to check (without # prefix)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/instagram/hashtag-checker",
            body=await async_maybe_transform(
                {"hashtags": hashtags}, instagram_check_hashtag_safety_params.InstagramCheckHashtagSafetyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramCheckHashtagSafetyResponse,
        )


class InstagramResourceWithRawResponse:
    def __init__(self, instagram: InstagramResource) -> None:
        self._instagram = instagram

        self.check_hashtag_safety = to_raw_response_wrapper(
            instagram.check_hashtag_safety,
        )


class AsyncInstagramResourceWithRawResponse:
    def __init__(self, instagram: AsyncInstagramResource) -> None:
        self._instagram = instagram

        self.check_hashtag_safety = async_to_raw_response_wrapper(
            instagram.check_hashtag_safety,
        )


class InstagramResourceWithStreamingResponse:
    def __init__(self, instagram: InstagramResource) -> None:
        self._instagram = instagram

        self.check_hashtag_safety = to_streamed_response_wrapper(
            instagram.check_hashtag_safety,
        )


class AsyncInstagramResourceWithStreamingResponse:
    def __init__(self, instagram: AsyncInstagramResource) -> None:
        self._instagram = instagram

        self.check_hashtag_safety = async_to_streamed_response_wrapper(
            instagram.check_hashtag_safety,
        )
