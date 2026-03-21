# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.analytics import YoutubeGetDailyViewsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestYoutube:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_views(self, client: Relay) -> None:
        youtube = client.analytics.youtube.get_daily_views(
            account_id="account_id",
        )
        assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_views_with_all_params(self, client: Relay) -> None:
        youtube = client.analytics.youtube.get_daily_views(
            account_id="account_id",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_views(self, client: Relay) -> None:
        response = client.analytics.youtube.with_raw_response.get_daily_views(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_views(self, client: Relay) -> None:
        with client.analytics.youtube.with_streaming_response.get_daily_views(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncYoutube:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_views(self, async_client: AsyncRelay) -> None:
        youtube = await async_client.analytics.youtube.get_daily_views(
            account_id="account_id",
        )
        assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_views_with_all_params(self, async_client: AsyncRelay) -> None:
        youtube = await async_client.analytics.youtube.get_daily_views(
            account_id="account_id",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_views(self, async_client: AsyncRelay) -> None:
        response = await async_client.analytics.youtube.with_raw_response.get_daily_views(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_views(self, async_client: AsyncRelay) -> None:
        async with async_client.analytics.youtube.with_streaming_response.get_daily_views(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetDailyViewsResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True
