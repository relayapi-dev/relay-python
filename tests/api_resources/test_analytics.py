# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from relay.types import (
    AnalyticsRetrieveResponse,
    AnalyticsGetBestTimeResponse,
    AnalyticsGetContentDecayResponse,
    AnalyticsGetPostTimelineResponse,
    AnalyticsListDailyMetricsResponse,
    AnalyticsGetPostingFrequencyResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        analytics = client.analytics.retrieve()
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Relay) -> None:
        analytics = client.analytics.retrieve(
            account_id="account_id",
            from_date="from_date",
            limit=1,
            offset=0,
            platform="twitter",
            post_id="post_id",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.analytics.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.analytics.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_best_time(self, client: Relay) -> None:
        analytics = client.analytics.get_best_time()
        assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_best_time_with_all_params(self, client: Relay) -> None:
        analytics = client.analytics.get_best_time(
            account_id="account_id",
            from_date="from_date",
            platform="twitter",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_best_time(self, client: Relay) -> None:
        response = client.analytics.with_raw_response.get_best_time()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_best_time(self, client: Relay) -> None:
        with client.analytics.with_streaming_response.get_best_time() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_content_decay(self, client: Relay) -> None:
        analytics = client.analytics.get_content_decay(
            post_id="post_id",
        )
        assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_content_decay_with_all_params(self, client: Relay) -> None:
        analytics = client.analytics.get_content_decay(
            post_id="post_id",
            days=1,
        )
        assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_content_decay(self, client: Relay) -> None:
        response = client.analytics.with_raw_response.get_content_decay(
            post_id="post_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_content_decay(self, client: Relay) -> None:
        with client.analytics.with_streaming_response.get_content_decay(
            post_id="post_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_post_timeline(self, client: Relay) -> None:
        analytics = client.analytics.get_post_timeline(
            post_id="post_id",
        )
        assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_post_timeline_with_all_params(self, client: Relay) -> None:
        analytics = client.analytics.get_post_timeline(
            post_id="post_id",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_post_timeline(self, client: Relay) -> None:
        response = client.analytics.with_raw_response.get_post_timeline(
            post_id="post_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_post_timeline(self, client: Relay) -> None:
        with client.analytics.with_streaming_response.get_post_timeline(
            post_id="post_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_posting_frequency(self, client: Relay) -> None:
        analytics = client.analytics.get_posting_frequency()
        assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_posting_frequency_with_all_params(self, client: Relay) -> None:
        analytics = client.analytics.get_posting_frequency(
            account_id="account_id",
            from_date="from_date",
            platform="twitter",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_posting_frequency(self, client: Relay) -> None:
        response = client.analytics.with_raw_response.get_posting_frequency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_posting_frequency(self, client: Relay) -> None:
        with client.analytics.with_streaming_response.get_posting_frequency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_daily_metrics(self, client: Relay) -> None:
        analytics = client.analytics.list_daily_metrics()
        assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_daily_metrics_with_all_params(self, client: Relay) -> None:
        analytics = client.analytics.list_daily_metrics(
            account_id="account_id",
            from_date="from_date",
            platform="twitter",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_daily_metrics(self, client: Relay) -> None:
        response = client.analytics.with_raw_response.list_daily_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_daily_metrics(self, client: Relay) -> None:
        with client.analytics.with_streaming_response.list_daily_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.retrieve()
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.retrieve(
            account_id="account_id",
            from_date="from_date",
            limit=1,
            offset=0,
            platform="twitter",
            post_id="post_id",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_best_time(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_best_time()
        assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_best_time_with_all_params(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_best_time(
            account_id="account_id",
            from_date="from_date",
            platform="twitter",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_best_time(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.with_raw_response.get_best_time()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_best_time(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.with_streaming_response.get_best_time() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetBestTimeResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_content_decay(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_content_decay(
            post_id="post_id",
        )
        assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_content_decay_with_all_params(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_content_decay(
            post_id="post_id",
            days=1,
        )
        assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_content_decay(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.with_raw_response.get_content_decay(
            post_id="post_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_content_decay(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.with_streaming_response.get_content_decay(
            post_id="post_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetContentDecayResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_post_timeline(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_post_timeline(
            post_id="post_id",
        )
        assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_post_timeline_with_all_params(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_post_timeline(
            post_id="post_id",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_post_timeline(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.with_raw_response.get_post_timeline(
            post_id="post_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_post_timeline(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.with_streaming_response.get_post_timeline(
            post_id="post_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetPostTimelineResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_posting_frequency(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_posting_frequency()
        assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_posting_frequency_with_all_params(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.get_posting_frequency(
            account_id="account_id",
            from_date="from_date",
            platform="twitter",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_posting_frequency(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.with_raw_response.get_posting_frequency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_posting_frequency(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.with_streaming_response.get_posting_frequency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetPostingFrequencyResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_daily_metrics(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.list_daily_metrics()
        assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_daily_metrics_with_all_params(self, async_client: AsyncRelay) -> None:
        analytics = await async_client.analytics.list_daily_metrics(
            account_id="account_id",
            from_date="from_date",
            platform="twitter",
            to_date="to_date",
        )
        assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_daily_metrics(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.with_raw_response.list_daily_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_daily_metrics(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.with_streaming_response.list_daily_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsListDailyMetricsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True
