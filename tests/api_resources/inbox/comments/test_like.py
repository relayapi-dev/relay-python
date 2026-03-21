# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.inbox.comments import LikeCreateResponse, LikeDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLike:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        like = client.inbox.comments.like.create(
            "comment_id",
        )
        assert_matches_type(LikeCreateResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.inbox.comments.like.with_raw_response.create(
            "comment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        like = response.parse()
        assert_matches_type(LikeCreateResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.inbox.comments.like.with_streaming_response.create(
            "comment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            like = response.parse()
            assert_matches_type(LikeCreateResponse, like, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.inbox.comments.like.with_raw_response.create(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Relay) -> None:
        like = client.inbox.comments.like.delete(
            "comment_id",
        )
        assert_matches_type(LikeDeleteResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Relay) -> None:
        response = client.inbox.comments.like.with_raw_response.delete(
            "comment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        like = response.parse()
        assert_matches_type(LikeDeleteResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Relay) -> None:
        with client.inbox.comments.like.with_streaming_response.delete(
            "comment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            like = response.parse()
            assert_matches_type(LikeDeleteResponse, like, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.inbox.comments.like.with_raw_response.delete(
                "",
            )


class TestAsyncLike:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        like = await async_client.inbox.comments.like.create(
            "comment_id",
        )
        assert_matches_type(LikeCreateResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.like.with_raw_response.create(
            "comment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        like = await response.parse()
        assert_matches_type(LikeCreateResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.like.with_streaming_response.create(
            "comment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            like = await response.parse()
            assert_matches_type(LikeCreateResponse, like, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.inbox.comments.like.with_raw_response.create(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRelay) -> None:
        like = await async_client.inbox.comments.like.delete(
            "comment_id",
        )
        assert_matches_type(LikeDeleteResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.like.with_raw_response.delete(
            "comment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        like = await response.parse()
        assert_matches_type(LikeDeleteResponse, like, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.like.with_streaming_response.delete(
            "comment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            like = await response.parse()
            assert_matches_type(LikeDeleteResponse, like, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.inbox.comments.like.with_raw_response.delete(
                "",
            )
