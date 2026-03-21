# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from relay.types import (
    ConnectStartOAuthFlowResponse,
    ConnectFetchPendingDataResponse,
    ConnectCompleteOAuthCallbackResponse,
    ConnectCreateBlueskyConnectionResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_oauth_callback(self, client: Relay) -> None:
        connect = client.connect.complete_oauth_callback(
            platform="twitter",
            code="code",
        )
        assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_oauth_callback_with_all_params(self, client: Relay) -> None:
        connect = client.connect.complete_oauth_callback(
            platform="twitter",
            code="code",
            redirect_url="https://example.com",
        )
        assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_oauth_callback(self, client: Relay) -> None:
        response = client.connect.with_raw_response.complete_oauth_callback(
            platform="twitter",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_oauth_callback(self, client: Relay) -> None:
        with client.connect.with_streaming_response.complete_oauth_callback(
            platform="twitter",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_bluesky_connection(self, client: Relay) -> None:
        connect = client.connect.create_bluesky_connection(
            app_password="app_password",
            handle="handle",
        )
        assert_matches_type(ConnectCreateBlueskyConnectionResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_bluesky_connection(self, client: Relay) -> None:
        response = client.connect.with_raw_response.create_bluesky_connection(
            app_password="app_password",
            handle="handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectCreateBlueskyConnectionResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_bluesky_connection(self, client: Relay) -> None:
        with client.connect.with_streaming_response.create_bluesky_connection(
            app_password="app_password",
            handle="handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectCreateBlueskyConnectionResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fetch_pending_data(self, client: Relay) -> None:
        connect = client.connect.fetch_pending_data(
            token="token",
        )
        assert_matches_type(ConnectFetchPendingDataResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fetch_pending_data(self, client: Relay) -> None:
        response = client.connect.with_raw_response.fetch_pending_data(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectFetchPendingDataResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fetch_pending_data(self, client: Relay) -> None:
        with client.connect.with_streaming_response.fetch_pending_data(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectFetchPendingDataResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_oauth_flow(self, client: Relay) -> None:
        connect = client.connect.start_oauth_flow(
            platform="twitter",
        )
        assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_oauth_flow_with_all_params(self, client: Relay) -> None:
        connect = client.connect.start_oauth_flow(
            platform="twitter",
            headless="headless",
            redirect_url="https://example.com",
        )
        assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_oauth_flow(self, client: Relay) -> None:
        response = client.connect.with_raw_response.start_oauth_flow(
            platform="twitter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_oauth_flow(self, client: Relay) -> None:
        with client.connect.with_streaming_response.start_oauth_flow(
            platform="twitter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_oauth_callback(self, async_client: AsyncRelay) -> None:
        connect = await async_client.connect.complete_oauth_callback(
            platform="twitter",
            code="code",
        )
        assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_oauth_callback_with_all_params(self, async_client: AsyncRelay) -> None:
        connect = await async_client.connect.complete_oauth_callback(
            platform="twitter",
            code="code",
            redirect_url="https://example.com",
        )
        assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_oauth_callback(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.with_raw_response.complete_oauth_callback(
            platform="twitter",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_oauth_callback(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.with_streaming_response.complete_oauth_callback(
            platform="twitter",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectCompleteOAuthCallbackResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_bluesky_connection(self, async_client: AsyncRelay) -> None:
        connect = await async_client.connect.create_bluesky_connection(
            app_password="app_password",
            handle="handle",
        )
        assert_matches_type(ConnectCreateBlueskyConnectionResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_bluesky_connection(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.with_raw_response.create_bluesky_connection(
            app_password="app_password",
            handle="handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectCreateBlueskyConnectionResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_bluesky_connection(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.with_streaming_response.create_bluesky_connection(
            app_password="app_password",
            handle="handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectCreateBlueskyConnectionResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fetch_pending_data(self, async_client: AsyncRelay) -> None:
        connect = await async_client.connect.fetch_pending_data(
            token="token",
        )
        assert_matches_type(ConnectFetchPendingDataResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fetch_pending_data(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.with_raw_response.fetch_pending_data(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectFetchPendingDataResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_pending_data(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.with_streaming_response.fetch_pending_data(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectFetchPendingDataResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_oauth_flow(self, async_client: AsyncRelay) -> None:
        connect = await async_client.connect.start_oauth_flow(
            platform="twitter",
        )
        assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_oauth_flow_with_all_params(self, async_client: AsyncRelay) -> None:
        connect = await async_client.connect.start_oauth_flow(
            platform="twitter",
            headless="headless",
            redirect_url="https://example.com",
        )
        assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_oauth_flow(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.with_raw_response.start_oauth_flow(
            platform="twitter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_oauth_flow(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.with_streaming_response.start_oauth_flow(
            platform="twitter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectStartOAuthFlowResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True
