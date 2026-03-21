# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from relay.types import ConnectionListLogsResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_logs(self, client: Relay) -> None:
        connection = client.connections.list_logs()
        assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_logs_with_all_params(self, client: Relay) -> None:
        connection = client.connections.list_logs(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_logs(self, client: Relay) -> None:
        response = client.connections.with_raw_response.list_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_logs(self, client: Relay) -> None:
        with client.connections.with_streaming_response.list_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_logs(self, async_client: AsyncRelay) -> None:
        connection = await async_client.connections.list_logs()
        assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_logs_with_all_params(self, async_client: AsyncRelay) -> None:
        connection = await async_client.connections.list_logs(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_logs(self, async_client: AsyncRelay) -> None:
        response = await async_client.connections.with_raw_response.list_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_logs(self, async_client: AsyncRelay) -> None:
        async with async_client.connections.with_streaming_response.list_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListLogsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True
