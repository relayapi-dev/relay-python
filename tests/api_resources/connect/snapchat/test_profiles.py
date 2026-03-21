# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.connect.snapchat import ProfileListResponse, ProfileSelectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        profile = client.connect.snapchat.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.connect.snapchat.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.connect.snapchat.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_select(self, client: Relay) -> None:
        profile = client.connect.snapchat.profiles.select(
            connect_token="connect_token",
            profile_id="profile_id",
        )
        assert_matches_type(ProfileSelectResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_select(self, client: Relay) -> None:
        response = client.connect.snapchat.profiles.with_raw_response.select(
            connect_token="connect_token",
            profile_id="profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileSelectResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_select(self, client: Relay) -> None:
        with client.connect.snapchat.profiles.with_streaming_response.select(
            connect_token="connect_token",
            profile_id="profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileSelectResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        profile = await async_client.connect.snapchat.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.snapchat.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.snapchat.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_select(self, async_client: AsyncRelay) -> None:
        profile = await async_client.connect.snapchat.profiles.select(
            connect_token="connect_token",
            profile_id="profile_id",
        )
        assert_matches_type(ProfileSelectResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_select(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.snapchat.profiles.with_raw_response.select(
            connect_token="connect_token",
            profile_id="profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileSelectResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_select(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.snapchat.profiles.with_streaming_response.select(
            connect_token="connect_token",
            profile_id="profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileSelectResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
