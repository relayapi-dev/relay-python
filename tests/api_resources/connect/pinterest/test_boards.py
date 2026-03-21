# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.connect.pinterest import BoardListResponse, BoardSelectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBoards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        board = client.connect.pinterest.boards.list()
        assert_matches_type(BoardListResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.connect.pinterest.boards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        board = response.parse()
        assert_matches_type(BoardListResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.connect.pinterest.boards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            board = response.parse()
            assert_matches_type(BoardListResponse, board, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_select(self, client: Relay) -> None:
        board = client.connect.pinterest.boards.select(
            board_id="board_id",
            connect_token="connect_token",
        )
        assert_matches_type(BoardSelectResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_select(self, client: Relay) -> None:
        response = client.connect.pinterest.boards.with_raw_response.select(
            board_id="board_id",
            connect_token="connect_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        board = response.parse()
        assert_matches_type(BoardSelectResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_select(self, client: Relay) -> None:
        with client.connect.pinterest.boards.with_streaming_response.select(
            board_id="board_id",
            connect_token="connect_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            board = response.parse()
            assert_matches_type(BoardSelectResponse, board, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBoards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        board = await async_client.connect.pinterest.boards.list()
        assert_matches_type(BoardListResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.pinterest.boards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        board = await response.parse()
        assert_matches_type(BoardListResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.pinterest.boards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            board = await response.parse()
            assert_matches_type(BoardListResponse, board, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_select(self, async_client: AsyncRelay) -> None:
        board = await async_client.connect.pinterest.boards.select(
            board_id="board_id",
            connect_token="connect_token",
        )
        assert_matches_type(BoardSelectResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_select(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.pinterest.boards.with_raw_response.select(
            board_id="board_id",
            connect_token="connect_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        board = await response.parse()
        assert_matches_type(BoardSelectResponse, board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_select(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.pinterest.boards.with_streaming_response.select(
            board_id="board_id",
            connect_token="connect_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            board = await response.parse()
            assert_matches_type(BoardSelectResponse, board, path=["response"])

        assert cast(Any, response.is_closed) is True
