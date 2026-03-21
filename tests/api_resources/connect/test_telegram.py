# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.connect import (
    TelegramConnectDirectlyResponse,
    TelegramInitiateConnectionResponse,
    TelegramPollConnectionStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelegram:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_directly(self, client: Relay) -> None:
        telegram = client.connect.telegram.connect_directly(
            chat_id="chat_id",
        )
        assert_matches_type(TelegramConnectDirectlyResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect_directly(self, client: Relay) -> None:
        response = client.connect.telegram.with_raw_response.connect_directly(
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = response.parse()
        assert_matches_type(TelegramConnectDirectlyResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect_directly(self, client: Relay) -> None:
        with client.connect.telegram.with_streaming_response.connect_directly(
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = response.parse()
            assert_matches_type(TelegramConnectDirectlyResponse, telegram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_connection(self, client: Relay) -> None:
        telegram = client.connect.telegram.initiate_connection()
        assert_matches_type(TelegramInitiateConnectionResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_connection(self, client: Relay) -> None:
        response = client.connect.telegram.with_raw_response.initiate_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = response.parse()
        assert_matches_type(TelegramInitiateConnectionResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_connection(self, client: Relay) -> None:
        with client.connect.telegram.with_streaming_response.initiate_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = response.parse()
            assert_matches_type(TelegramInitiateConnectionResponse, telegram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_poll_connection_status(self, client: Relay) -> None:
        telegram = client.connect.telegram.poll_connection_status(
            code="code",
        )
        assert_matches_type(TelegramPollConnectionStatusResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_poll_connection_status(self, client: Relay) -> None:
        response = client.connect.telegram.with_raw_response.poll_connection_status(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = response.parse()
        assert_matches_type(TelegramPollConnectionStatusResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_poll_connection_status(self, client: Relay) -> None:
        with client.connect.telegram.with_streaming_response.poll_connection_status(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = response.parse()
            assert_matches_type(TelegramPollConnectionStatusResponse, telegram, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTelegram:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_directly(self, async_client: AsyncRelay) -> None:
        telegram = await async_client.connect.telegram.connect_directly(
            chat_id="chat_id",
        )
        assert_matches_type(TelegramConnectDirectlyResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect_directly(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.telegram.with_raw_response.connect_directly(
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = await response.parse()
        assert_matches_type(TelegramConnectDirectlyResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect_directly(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.telegram.with_streaming_response.connect_directly(
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = await response.parse()
            assert_matches_type(TelegramConnectDirectlyResponse, telegram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_connection(self, async_client: AsyncRelay) -> None:
        telegram = await async_client.connect.telegram.initiate_connection()
        assert_matches_type(TelegramInitiateConnectionResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_connection(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.telegram.with_raw_response.initiate_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = await response.parse()
        assert_matches_type(TelegramInitiateConnectionResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_connection(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.telegram.with_streaming_response.initiate_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = await response.parse()
            assert_matches_type(TelegramInitiateConnectionResponse, telegram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_poll_connection_status(self, async_client: AsyncRelay) -> None:
        telegram = await async_client.connect.telegram.poll_connection_status(
            code="code",
        )
        assert_matches_type(TelegramPollConnectionStatusResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_poll_connection_status(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.telegram.with_raw_response.poll_connection_status(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = await response.parse()
        assert_matches_type(TelegramPollConnectionStatusResponse, telegram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_poll_connection_status(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.telegram.with_streaming_response.poll_connection_status(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = await response.parse()
            assert_matches_type(TelegramPollConnectionStatusResponse, telegram, path=["response"])

        assert cast(Any, response.is_closed) is True
