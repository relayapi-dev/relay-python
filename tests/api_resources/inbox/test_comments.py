# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.inbox import (
    CommentListResponse,
    CommentReplyResponse,
    CommentDeleteResponse,
    CommentRetrieveResponse,
    CommentPrivateReplyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        comment = client.inbox.comments.retrieve(
            post_id="post_id",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Relay) -> None:
        comment = client.inbox.comments.retrieve(
            post_id="post_id",
            account_id="account_id",
            cursor="cursor",
            limit=1,
            platform="twitter",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.inbox.comments.with_raw_response.retrieve(
            post_id="post_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.inbox.comments.with_streaming_response.retrieve(
            post_id="post_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.inbox.comments.with_raw_response.retrieve(
                post_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        comment = client.inbox.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Relay) -> None:
        comment = client.inbox.comments.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
            platform="twitter",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.inbox.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.inbox.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Relay) -> None:
        comment = client.inbox.comments.delete(
            "comment_id",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Relay) -> None:
        response = client.inbox.comments.with_raw_response.delete(
            "comment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Relay) -> None:
        with client.inbox.comments.with_streaming_response.delete(
            "comment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.inbox.comments.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_private_reply(self, client: Relay) -> None:
        comment = client.inbox.comments.private_reply(
            comment_id="comment_id",
            account_id="account_id",
            text="x",
        )
        assert_matches_type(CommentPrivateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_private_reply(self, client: Relay) -> None:
        response = client.inbox.comments.with_raw_response.private_reply(
            comment_id="comment_id",
            account_id="account_id",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentPrivateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_private_reply(self, client: Relay) -> None:
        with client.inbox.comments.with_streaming_response.private_reply(
            comment_id="comment_id",
            account_id="account_id",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentPrivateReplyResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_private_reply(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.inbox.comments.with_raw_response.private_reply(
                comment_id="",
                account_id="account_id",
                text="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reply(self, client: Relay) -> None:
        comment = client.inbox.comments.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
        )
        assert_matches_type(CommentReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reply_with_all_params(self, client: Relay) -> None:
        comment = client.inbox.comments.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
            comment_id="comment_id",
        )
        assert_matches_type(CommentReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: Relay) -> None:
        response = client.inbox.comments.with_raw_response.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: Relay) -> None:
        with client.inbox.comments.with_streaming_response.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentReplyResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reply(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.inbox.comments.with_raw_response.reply(
                post_id="",
                account_id="account_id",
                text="x",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.retrieve(
            post_id="post_id",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.retrieve(
            post_id="post_id",
            account_id="account_id",
            cursor="cursor",
            limit=1,
            platform="twitter",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.with_raw_response.retrieve(
            post_id="post_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.with_streaming_response.retrieve(
            post_id="post_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.inbox.comments.with_raw_response.retrieve(
                post_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
            platform="twitter",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.delete(
            "comment_id",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.with_raw_response.delete(
            "comment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.with_streaming_response.delete(
            "comment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.inbox.comments.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_private_reply(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.private_reply(
            comment_id="comment_id",
            account_id="account_id",
            text="x",
        )
        assert_matches_type(CommentPrivateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_private_reply(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.with_raw_response.private_reply(
            comment_id="comment_id",
            account_id="account_id",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentPrivateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_private_reply(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.with_streaming_response.private_reply(
            comment_id="comment_id",
            account_id="account_id",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentPrivateReplyResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_private_reply(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.inbox.comments.with_raw_response.private_reply(
                comment_id="",
                account_id="account_id",
                text="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
        )
        assert_matches_type(CommentReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncRelay) -> None:
        comment = await async_client.inbox.comments.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
            comment_id="comment_id",
        )
        assert_matches_type(CommentReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncRelay) -> None:
        response = await async_client.inbox.comments.with_raw_response.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncRelay) -> None:
        async with async_client.inbox.comments.with_streaming_response.reply(
            post_id="post_id",
            account_id="account_id",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentReplyResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reply(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.inbox.comments.with_raw_response.reply(
                post_id="",
                account_id="account_id",
                text="x",
            )
