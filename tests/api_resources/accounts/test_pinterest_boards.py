# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.accounts import (
    PinterestBoardRetrieveResponse,
    PinterestBoardSetDefaultResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPinterestBoards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        pinterest_board = client.accounts.pinterest_boards.retrieve(
            "id",
        )
        assert_matches_type(PinterestBoardRetrieveResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.accounts.pinterest_boards.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinterest_board = response.parse()
        assert_matches_type(PinterestBoardRetrieveResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.accounts.pinterest_boards.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinterest_board = response.parse()
            assert_matches_type(PinterestBoardRetrieveResponse, pinterest_board, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.pinterest_boards.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_default(self, client: Relay) -> None:
        pinterest_board = client.accounts.pinterest_boards.set_default(
            id="id",
            board_id="board_id",
        )
        assert_matches_type(PinterestBoardSetDefaultResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_default(self, client: Relay) -> None:
        response = client.accounts.pinterest_boards.with_raw_response.set_default(
            id="id",
            board_id="board_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinterest_board = response.parse()
        assert_matches_type(PinterestBoardSetDefaultResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_default(self, client: Relay) -> None:
        with client.accounts.pinterest_boards.with_streaming_response.set_default(
            id="id",
            board_id="board_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinterest_board = response.parse()
            assert_matches_type(PinterestBoardSetDefaultResponse, pinterest_board, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_default(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.pinterest_boards.with_raw_response.set_default(
                id="",
                board_id="board_id",
            )


class TestAsyncPinterestBoards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        pinterest_board = await async_client.accounts.pinterest_boards.retrieve(
            "id",
        )
        assert_matches_type(PinterestBoardRetrieveResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.accounts.pinterest_boards.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinterest_board = await response.parse()
        assert_matches_type(PinterestBoardRetrieveResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.accounts.pinterest_boards.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinterest_board = await response.parse()
            assert_matches_type(PinterestBoardRetrieveResponse, pinterest_board, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.pinterest_boards.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_default(self, async_client: AsyncRelay) -> None:
        pinterest_board = await async_client.accounts.pinterest_boards.set_default(
            id="id",
            board_id="board_id",
        )
        assert_matches_type(PinterestBoardSetDefaultResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_default(self, async_client: AsyncRelay) -> None:
        response = await async_client.accounts.pinterest_boards.with_raw_response.set_default(
            id="id",
            board_id="board_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinterest_board = await response.parse()
        assert_matches_type(PinterestBoardSetDefaultResponse, pinterest_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_default(self, async_client: AsyncRelay) -> None:
        async with async_client.accounts.pinterest_boards.with_streaming_response.set_default(
            id="id",
            board_id="board_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinterest_board = await response.parse()
            assert_matches_type(PinterestBoardSetDefaultResponse, pinterest_board, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_default(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.pinterest_boards.with_raw_response.set_default(
                id="",
                board_id="board_id",
            )
