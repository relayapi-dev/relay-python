# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.twitter import RetweetUndoResponse, RetweetCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetweet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        retweet = client.twitter.retweet.create(
            account_id="account_id",
            tweet_id="tweet_id",
        )
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.twitter.retweet.with_raw_response.create(
            account_id="account_id",
            tweet_id="tweet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = response.parse()
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.twitter.retweet.with_streaming_response.create(
            account_id="account_id",
            tweet_id="tweet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = response.parse()
            assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_undo(self, client: Relay) -> None:
        retweet = client.twitter.retweet.undo(
            account_id="account_id",
            tweet_id="tweet_id",
        )
        assert_matches_type(RetweetUndoResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_undo(self, client: Relay) -> None:
        response = client.twitter.retweet.with_raw_response.undo(
            account_id="account_id",
            tweet_id="tweet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = response.parse()
        assert_matches_type(RetweetUndoResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_undo(self, client: Relay) -> None:
        with client.twitter.retweet.with_streaming_response.undo(
            account_id="account_id",
            tweet_id="tweet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = response.parse()
            assert_matches_type(RetweetUndoResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetweet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        retweet = await async_client.twitter.retweet.create(
            account_id="account_id",
            tweet_id="tweet_id",
        )
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.twitter.retweet.with_raw_response.create(
            account_id="account_id",
            tweet_id="tweet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = await response.parse()
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.twitter.retweet.with_streaming_response.create(
            account_id="account_id",
            tweet_id="tweet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = await response.parse()
            assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_undo(self, async_client: AsyncRelay) -> None:
        retweet = await async_client.twitter.retweet.undo(
            account_id="account_id",
            tweet_id="tweet_id",
        )
        assert_matches_type(RetweetUndoResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_undo(self, async_client: AsyncRelay) -> None:
        response = await async_client.twitter.retweet.with_raw_response.undo(
            account_id="account_id",
            tweet_id="tweet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = await response.parse()
        assert_matches_type(RetweetUndoResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_undo(self, async_client: AsyncRelay) -> None:
        async with async_client.twitter.retweet.with_streaming_response.undo(
            account_id="account_id",
            tweet_id="tweet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = await response.parse()
            assert_matches_type(RetweetUndoResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True
