# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.tools import InstagramCheckHashtagSafetyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstagram:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_hashtag_safety(self, client: Relay) -> None:
        instagram = client.tools.instagram.check_hashtag_safety(
            hashtags=["string"],
        )
        assert_matches_type(InstagramCheckHashtagSafetyResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_hashtag_safety(self, client: Relay) -> None:
        response = client.tools.instagram.with_raw_response.check_hashtag_safety(
            hashtags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = response.parse()
        assert_matches_type(InstagramCheckHashtagSafetyResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_hashtag_safety(self, client: Relay) -> None:
        with client.tools.instagram.with_streaming_response.check_hashtag_safety(
            hashtags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = response.parse()
            assert_matches_type(InstagramCheckHashtagSafetyResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstagram:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_hashtag_safety(self, async_client: AsyncRelay) -> None:
        instagram = await async_client.tools.instagram.check_hashtag_safety(
            hashtags=["string"],
        )
        assert_matches_type(InstagramCheckHashtagSafetyResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_hashtag_safety(self, async_client: AsyncRelay) -> None:
        response = await async_client.tools.instagram.with_raw_response.check_hashtag_safety(
            hashtags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = await response.parse()
        assert_matches_type(InstagramCheckHashtagSafetyResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_hashtag_safety(self, async_client: AsyncRelay) -> None:
        async with async_client.tools.instagram.with_streaming_response.check_hashtag_safety(
            hashtags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = await response.parse()
            assert_matches_type(InstagramCheckHashtagSafetyResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True
