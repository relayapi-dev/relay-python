# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import (
    analytics_retrieve_params,
    analytics_get_best_time_params,
    analytics_get_content_decay_params,
    analytics_get_post_timeline_params,
    analytics_list_daily_metrics_params,
    analytics_get_posting_frequency_params,
)
from .youtube import (
    YoutubeResource,
    AsyncYoutubeResource,
    YoutubeResourceWithRawResponse,
    AsyncYoutubeResourceWithRawResponse,
    YoutubeResourceWithStreamingResponse,
    AsyncYoutubeResourceWithStreamingResponse,
)
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
from ...types.analytics_retrieve_response import AnalyticsRetrieveResponse
from ...types.analytics_get_best_time_response import AnalyticsGetBestTimeResponse
from ...types.analytics_get_content_decay_response import AnalyticsGetContentDecayResponse
from ...types.analytics_get_post_timeline_response import AnalyticsGetPostTimelineResponse
from ...types.analytics_list_daily_metrics_response import AnalyticsListDailyMetricsResponse
from ...types.analytics_get_posting_frequency_response import AnalyticsGetPostingFrequencyResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def youtube(self) -> YoutubeResource:
        return YoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        post_id: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsRetrieveResponse:
        """
        Get post analytics

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601 date string)

          limit: Number of items

          offset: Offset

          platform: Filter by platform

          post_id: Filter by post ID

          to_date: End date (ISO 8601 date string)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "limit": limit,
                        "offset": offset,
                        "platform": platform,
                        "post_id": post_id,
                        "to_date": to_date,
                    },
                    analytics_retrieve_params.AnalyticsRetrieveParams,
                ),
            ),
            cast_to=AnalyticsRetrieveResponse,
        )

    def get_best_time(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetBestTimeResponse:
        """
        Get best posting times based on engagement

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601)

          platform: Filter by platform

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/best-time",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "platform": platform,
                        "to_date": to_date,
                    },
                    analytics_get_best_time_params.AnalyticsGetBestTimeParams,
                ),
            ),
            cast_to=AnalyticsGetBestTimeResponse,
        )

    def get_content_decay(
        self,
        *,
        post_id: str,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetContentDecayResponse:
        """
        Get engagement decay curve for a post

        Args:
          post_id: Post ID to analyze decay for

          days: Number of days to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/content-decay",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "post_id": post_id,
                        "days": days,
                    },
                    analytics_get_content_decay_params.AnalyticsGetContentDecayParams,
                ),
            ),
            cast_to=AnalyticsGetContentDecayResponse,
        )

    def get_post_timeline(
        self,
        *,
        post_id: str,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetPostTimelineResponse:
        """
        Get per-post daily timeline of metrics

        Args:
          post_id: Post ID

          from_date: Start date (ISO 8601)

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/post-timeline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "post_id": post_id,
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    analytics_get_post_timeline_params.AnalyticsGetPostTimelineParams,
                ),
            ),
            cast_to=AnalyticsGetPostTimelineResponse,
        )

    def get_posting_frequency(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetPostingFrequencyResponse:
        """
        Get posting frequency vs engagement analysis

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601)

          platform: Filter by platform

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/posting-frequency",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "platform": platform,
                        "to_date": to_date,
                    },
                    analytics_get_posting_frequency_params.AnalyticsGetPostingFrequencyParams,
                ),
            ),
            cast_to=AnalyticsGetPostingFrequencyResponse,
        )

    def list_daily_metrics(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsListDailyMetricsResponse:
        """
        Get daily aggregated metrics

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601)

          platform: Filter by platform

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/daily-metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "platform": platform,
                        "to_date": to_date,
                    },
                    analytics_list_daily_metrics_params.AnalyticsListDailyMetricsParams,
                ),
            ),
            cast_to=AnalyticsListDailyMetricsResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def youtube(self) -> AsyncYoutubeResource:
        return AsyncYoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        post_id: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsRetrieveResponse:
        """
        Get post analytics

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601 date string)

          limit: Number of items

          offset: Offset

          platform: Filter by platform

          post_id: Filter by post ID

          to_date: End date (ISO 8601 date string)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "limit": limit,
                        "offset": offset,
                        "platform": platform,
                        "post_id": post_id,
                        "to_date": to_date,
                    },
                    analytics_retrieve_params.AnalyticsRetrieveParams,
                ),
            ),
            cast_to=AnalyticsRetrieveResponse,
        )

    async def get_best_time(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetBestTimeResponse:
        """
        Get best posting times based on engagement

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601)

          platform: Filter by platform

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/best-time",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "platform": platform,
                        "to_date": to_date,
                    },
                    analytics_get_best_time_params.AnalyticsGetBestTimeParams,
                ),
            ),
            cast_to=AnalyticsGetBestTimeResponse,
        )

    async def get_content_decay(
        self,
        *,
        post_id: str,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetContentDecayResponse:
        """
        Get engagement decay curve for a post

        Args:
          post_id: Post ID to analyze decay for

          days: Number of days to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/content-decay",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "post_id": post_id,
                        "days": days,
                    },
                    analytics_get_content_decay_params.AnalyticsGetContentDecayParams,
                ),
            ),
            cast_to=AnalyticsGetContentDecayResponse,
        )

    async def get_post_timeline(
        self,
        *,
        post_id: str,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetPostTimelineResponse:
        """
        Get per-post daily timeline of metrics

        Args:
          post_id: Post ID

          from_date: Start date (ISO 8601)

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/post-timeline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "post_id": post_id,
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    analytics_get_post_timeline_params.AnalyticsGetPostTimelineParams,
                ),
            ),
            cast_to=AnalyticsGetPostTimelineResponse,
        )

    async def get_posting_frequency(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetPostingFrequencyResponse:
        """
        Get posting frequency vs engagement analysis

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601)

          platform: Filter by platform

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/posting-frequency",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "platform": platform,
                        "to_date": to_date,
                    },
                    analytics_get_posting_frequency_params.AnalyticsGetPostingFrequencyParams,
                ),
            ),
            cast_to=AnalyticsGetPostingFrequencyResponse,
        )

    async def list_daily_metrics(
        self,
        *,
        account_id: str | Omit = omit,
        from_date: str | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsListDailyMetricsResponse:
        """
        Get daily aggregated metrics

        Args:
          account_id: Filter by account ID

          from_date: Start date (ISO 8601)

          platform: Filter by platform

          to_date: End date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/daily-metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_date": from_date,
                        "platform": platform,
                        "to_date": to_date,
                    },
                    analytics_list_daily_metrics_params.AnalyticsListDailyMetricsParams,
                ),
            ),
            cast_to=AnalyticsListDailyMetricsResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = to_raw_response_wrapper(
            analytics.retrieve,
        )
        self.get_best_time = to_raw_response_wrapper(
            analytics.get_best_time,
        )
        self.get_content_decay = to_raw_response_wrapper(
            analytics.get_content_decay,
        )
        self.get_post_timeline = to_raw_response_wrapper(
            analytics.get_post_timeline,
        )
        self.get_posting_frequency = to_raw_response_wrapper(
            analytics.get_posting_frequency,
        )
        self.list_daily_metrics = to_raw_response_wrapper(
            analytics.list_daily_metrics,
        )

    @cached_property
    def youtube(self) -> YoutubeResourceWithRawResponse:
        return YoutubeResourceWithRawResponse(self._analytics.youtube)


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = async_to_raw_response_wrapper(
            analytics.retrieve,
        )
        self.get_best_time = async_to_raw_response_wrapper(
            analytics.get_best_time,
        )
        self.get_content_decay = async_to_raw_response_wrapper(
            analytics.get_content_decay,
        )
        self.get_post_timeline = async_to_raw_response_wrapper(
            analytics.get_post_timeline,
        )
        self.get_posting_frequency = async_to_raw_response_wrapper(
            analytics.get_posting_frequency,
        )
        self.list_daily_metrics = async_to_raw_response_wrapper(
            analytics.list_daily_metrics,
        )

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithRawResponse:
        return AsyncYoutubeResourceWithRawResponse(self._analytics.youtube)


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = to_streamed_response_wrapper(
            analytics.retrieve,
        )
        self.get_best_time = to_streamed_response_wrapper(
            analytics.get_best_time,
        )
        self.get_content_decay = to_streamed_response_wrapper(
            analytics.get_content_decay,
        )
        self.get_post_timeline = to_streamed_response_wrapper(
            analytics.get_post_timeline,
        )
        self.get_posting_frequency = to_streamed_response_wrapper(
            analytics.get_posting_frequency,
        )
        self.list_daily_metrics = to_streamed_response_wrapper(
            analytics.list_daily_metrics,
        )

    @cached_property
    def youtube(self) -> YoutubeResourceWithStreamingResponse:
        return YoutubeResourceWithStreamingResponse(self._analytics.youtube)


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = async_to_streamed_response_wrapper(
            analytics.retrieve,
        )
        self.get_best_time = async_to_streamed_response_wrapper(
            analytics.get_best_time,
        )
        self.get_content_decay = async_to_streamed_response_wrapper(
            analytics.get_content_decay,
        )
        self.get_post_timeline = async_to_streamed_response_wrapper(
            analytics.get_post_timeline,
        )
        self.get_posting_frequency = async_to_streamed_response_wrapper(
            analytics.get_posting_frequency,
        )
        self.list_daily_metrics = async_to_streamed_response_wrapper(
            analytics.list_daily_metrics,
        )

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithStreamingResponse:
        return AsyncYoutubeResourceWithStreamingResponse(self._analytics.youtube)
