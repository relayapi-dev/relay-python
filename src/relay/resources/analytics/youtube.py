# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.analytics import youtube_get_daily_views_params
from ...types.analytics.youtube_get_daily_views_response import YoutubeGetDailyViewsResponse

__all__ = ["YoutubeResource", "AsyncYoutubeResource"]


class YoutubeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> YoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return YoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return YoutubeResourceWithStreamingResponse(self)

    def get_daily_views(
        self,
        *,
        account_id: str,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetDailyViewsResponse:
        """
        Get YouTube daily views and watch time

        Args:
          account_id: YouTube account ID

          from_date: Start date (ISO 8601)

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/youtube/daily-views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    youtube_get_daily_views_params.YoutubeGetDailyViewsParams,
                ),
            ),
            cast_to=YoutubeGetDailyViewsResponse,
        )


class AsyncYoutubeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncYoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncYoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncYoutubeResourceWithStreamingResponse(self)

    async def get_daily_views(
        self,
        *,
        account_id: str,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetDailyViewsResponse:
        """
        Get YouTube daily views and watch time

        Args:
          account_id: YouTube account ID

          from_date: Start date (ISO 8601)

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/youtube/daily-views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    youtube_get_daily_views_params.YoutubeGetDailyViewsParams,
                ),
            ),
            cast_to=YoutubeGetDailyViewsResponse,
        )


class YoutubeResourceWithRawResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

        self.get_daily_views = to_raw_response_wrapper(
            youtube.get_daily_views,
        )


class AsyncYoutubeResourceWithRawResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

        self.get_daily_views = async_to_raw_response_wrapper(
            youtube.get_daily_views,
        )


class YoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

        self.get_daily_views = to_streamed_response_wrapper(
            youtube.get_daily_views,
        )


class AsyncYoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

        self.get_daily_views = async_to_streamed_response_wrapper(
            youtube.get_daily_views,
        )
