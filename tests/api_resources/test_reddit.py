# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from relay.types import RedditSearchResponse, RedditGetFeedResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReddit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_feed(self, client: Relay) -> None:
        reddit = client.reddit.get_feed(
            account_id="account_id",
            subreddit="subreddit",
        )
        assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_feed_with_all_params(self, client: Relay) -> None:
        reddit = client.reddit.get_feed(
            account_id="account_id",
            subreddit="subreddit",
            cursor="cursor",
            limit=1,
            sort="hot",
            time="hour",
        )
        assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_feed(self, client: Relay) -> None:
        response = client.reddit.with_raw_response.get_feed(
            account_id="account_id",
            subreddit="subreddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reddit = response.parse()
        assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_feed(self, client: Relay) -> None:
        with client.reddit.with_streaming_response.get_feed(
            account_id="account_id",
            subreddit="subreddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reddit = response.parse()
            assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Relay) -> None:
        reddit = client.reddit.search(
            account_id="account_id",
            query="query",
        )
        assert_matches_type(RedditSearchResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Relay) -> None:
        reddit = client.reddit.search(
            account_id="account_id",
            query="query",
            cursor="cursor",
            limit=1,
            sort="relevance",
            subreddit="subreddit",
            time="hour",
        )
        assert_matches_type(RedditSearchResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Relay) -> None:
        response = client.reddit.with_raw_response.search(
            account_id="account_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reddit = response.parse()
        assert_matches_type(RedditSearchResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Relay) -> None:
        with client.reddit.with_streaming_response.search(
            account_id="account_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reddit = response.parse()
            assert_matches_type(RedditSearchResponse, reddit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReddit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_feed(self, async_client: AsyncRelay) -> None:
        reddit = await async_client.reddit.get_feed(
            account_id="account_id",
            subreddit="subreddit",
        )
        assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_feed_with_all_params(self, async_client: AsyncRelay) -> None:
        reddit = await async_client.reddit.get_feed(
            account_id="account_id",
            subreddit="subreddit",
            cursor="cursor",
            limit=1,
            sort="hot",
            time="hour",
        )
        assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_feed(self, async_client: AsyncRelay) -> None:
        response = await async_client.reddit.with_raw_response.get_feed(
            account_id="account_id",
            subreddit="subreddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reddit = await response.parse()
        assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_feed(self, async_client: AsyncRelay) -> None:
        async with async_client.reddit.with_streaming_response.get_feed(
            account_id="account_id",
            subreddit="subreddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reddit = await response.parse()
            assert_matches_type(RedditGetFeedResponse, reddit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncRelay) -> None:
        reddit = await async_client.reddit.search(
            account_id="account_id",
            query="query",
        )
        assert_matches_type(RedditSearchResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncRelay) -> None:
        reddit = await async_client.reddit.search(
            account_id="account_id",
            query="query",
            cursor="cursor",
            limit=1,
            sort="relevance",
            subreddit="subreddit",
            time="hour",
        )
        assert_matches_type(RedditSearchResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncRelay) -> None:
        response = await async_client.reddit.with_raw_response.search(
            account_id="account_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reddit = await response.parse()
        assert_matches_type(RedditSearchResponse, reddit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncRelay) -> None:
        async with async_client.reddit.with_streaming_response.search(
            account_id="account_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reddit = await response.parse()
            assert_matches_type(RedditSearchResponse, reddit, path=["response"])

        assert cast(Any, response.is_closed) is True
