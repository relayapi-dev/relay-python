# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.inbox import ReviewListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        review = client.inbox.reviews.list()
        assert_matches_type(ReviewListResponse, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Relay) -> None:
        review = client.inbox.reviews.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
            max_rating=1,
            min_rating=1,
            platform="twitter",
        )
        assert_matches_type(ReviewListResponse, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.inbox.reviews.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ReviewListResponse, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.inbox.reviews.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ReviewListResponse, review, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReviews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        review = await async_client.inbox.reviews.list()
        assert_matches_type(ReviewListResponse, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRelay) -> None:
        review = await async_client.inbox.reviews.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
            max_rating=1,
            min_rating=1,
            platform="twitter",
        )
        assert_matches_type(ReviewListResponse, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.reviews.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ReviewListResponse, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.reviews.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ReviewListResponse, review, path=["response"])

        assert cast(Any, response.is_closed) is True
