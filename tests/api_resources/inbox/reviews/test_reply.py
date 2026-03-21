# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.inbox.reviews import ReplyCreateResponse, ReplyDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReply:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        reply = client.inbox.reviews.reply.create(
            review_id="review_id",
            account_id="account_id",
            text="x",
        )
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.inbox.reviews.reply.with_raw_response.create(
            review_id="review_id",
            account_id="account_id",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.inbox.reviews.reply.with_streaming_response.create(
            review_id="review_id",
            account_id="account_id",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyCreateResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `review_id` but received ''"):
            client.inbox.reviews.reply.with_raw_response.create(
                review_id="",
                account_id="account_id",
                text="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Relay) -> None:
        reply = client.inbox.reviews.reply.delete(
            "review_id",
        )
        assert_matches_type(ReplyDeleteResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Relay) -> None:
        response = client.inbox.reviews.reply.with_raw_response.delete(
            "review_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyDeleteResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Relay) -> None:
        with client.inbox.reviews.reply.with_streaming_response.delete(
            "review_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyDeleteResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `review_id` but received ''"):
            client.inbox.reviews.reply.with_raw_response.delete(
                "",
            )


class TestAsyncReply:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        reply = await async_client.inbox.reviews.reply.create(
            review_id="review_id",
            account_id="account_id",
            text="x",
        )
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.reviews.reply.with_raw_response.create(
            review_id="review_id",
            account_id="account_id",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.reviews.reply.with_streaming_response.create(
            review_id="review_id",
            account_id="account_id",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyCreateResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `review_id` but received ''"):
            await async_client.inbox.reviews.reply.with_raw_response.create(
                review_id="",
                account_id="account_id",
                text="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRelay) -> None:
        reply = await async_client.inbox.reviews.reply.delete(
            "review_id",
        )
        assert_matches_type(ReplyDeleteResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.reviews.reply.with_raw_response.delete(
            "review_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyDeleteResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.reviews.reply.with_streaming_response.delete(
            "review_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyDeleteResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `review_id` but received ''"):
            await async_client.inbox.reviews.reply.with_raw_response.delete(
                "",
            )
