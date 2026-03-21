# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.accounts import RedditFlairRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedditFlairs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        reddit_flair = client.accounts.reddit_flairs.retrieve(
            id="id",
            subreddit="subreddit",
        )
        assert_matches_type(RedditFlairRetrieveResponse, reddit_flair, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.accounts.reddit_flairs.with_raw_response.retrieve(
            id="id",
            subreddit="subreddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reddit_flair = response.parse()
        assert_matches_type(RedditFlairRetrieveResponse, reddit_flair, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.accounts.reddit_flairs.with_streaming_response.retrieve(
            id="id",
            subreddit="subreddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reddit_flair = response.parse()
            assert_matches_type(RedditFlairRetrieveResponse, reddit_flair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.reddit_flairs.with_raw_response.retrieve(
                id="",
                subreddit="subreddit",
            )


class TestAsyncRedditFlairs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        reddit_flair = await async_client.accounts.reddit_flairs.retrieve(
            id="id",
            subreddit="subreddit",
        )
        assert_matches_type(RedditFlairRetrieveResponse, reddit_flair, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.accounts.reddit_flairs.with_raw_response.retrieve(
            id="id",
            subreddit="subreddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reddit_flair = await response.parse()
        assert_matches_type(RedditFlairRetrieveResponse, reddit_flair, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.accounts.reddit_flairs.with_streaming_response.retrieve(
            id="id",
            subreddit="subreddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reddit_flair = await response.parse()
            assert_matches_type(RedditFlairRetrieveResponse, reddit_flair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.reddit_flairs.with_raw_response.retrieve(
                id="",
                subreddit="subreddit",
            )
