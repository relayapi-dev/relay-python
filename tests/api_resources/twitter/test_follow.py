# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.twitter import (
    FollowCreateResponse,
    FollowUnfollowResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        follow = client.twitter.follow.create(
            account_id="account_id",
            target_user_id="target_user_id",
        )
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.twitter.follow.with_raw_response.create(
            account_id="account_id",
            target_user_id="target_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = response.parse()
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.twitter.follow.with_streaming_response.create(
            account_id="account_id",
            target_user_id="target_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = response.parse()
            assert_matches_type(FollowCreateResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unfollow(self, client: Relay) -> None:
        follow = client.twitter.follow.unfollow(
            account_id="account_id",
            target_user_id="target_user_id",
        )
        assert_matches_type(FollowUnfollowResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unfollow(self, client: Relay) -> None:
        response = client.twitter.follow.with_raw_response.unfollow(
            account_id="account_id",
            target_user_id="target_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = response.parse()
        assert_matches_type(FollowUnfollowResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unfollow(self, client: Relay) -> None:
        with client.twitter.follow.with_streaming_response.unfollow(
            account_id="account_id",
            target_user_id="target_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = response.parse()
            assert_matches_type(FollowUnfollowResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFollow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        follow = await async_client.twitter.follow.create(
            account_id="account_id",
            target_user_id="target_user_id",
        )
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.twitter.follow.with_raw_response.create(
            account_id="account_id",
            target_user_id="target_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = await response.parse()
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.twitter.follow.with_streaming_response.create(
            account_id="account_id",
            target_user_id="target_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = await response.parse()
            assert_matches_type(FollowCreateResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unfollow(self, async_client: AsyncRelay) -> None:
        follow = await async_client.twitter.follow.unfollow(
            account_id="account_id",
            target_user_id="target_user_id",
        )
        assert_matches_type(FollowUnfollowResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unfollow(self, async_client: AsyncRelay) -> None:
        response = await async_client.twitter.follow.with_raw_response.unfollow(
            account_id="account_id",
            target_user_id="target_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = await response.parse()
        assert_matches_type(FollowUnfollowResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unfollow(self, async_client: AsyncRelay) -> None:
        async with async_client.twitter.follow.with_streaming_response.unfollow(
            account_id="account_id",
            target_user_id="target_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = await response.parse()
            assert_matches_type(FollowUnfollowResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True
