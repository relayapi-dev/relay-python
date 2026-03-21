# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from relay.types import QueuePreviewResponse, QueueGetNextSlotResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_next_slot(self, client: Relay) -> None:
        queue = client.queue.get_next_slot()
        assert_matches_type(QueueGetNextSlotResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_next_slot(self, client: Relay) -> None:
        response = client.queue.with_raw_response.get_next_slot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueGetNextSlotResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_next_slot(self, client: Relay) -> None:
        with client.queue.with_streaming_response.get_next_slot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueGetNextSlotResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview(self, client: Relay) -> None:
        queue = client.queue.preview()
        assert_matches_type(QueuePreviewResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview_with_all_params(self, client: Relay) -> None:
        queue = client.queue.preview(
            count=1,
        )
        assert_matches_type(QueuePreviewResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_preview(self, client: Relay) -> None:
        response = client.queue.with_raw_response.preview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueuePreviewResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_preview(self, client: Relay) -> None:
        with client.queue.with_streaming_response.preview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueuePreviewResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_next_slot(self, async_client: AsyncRelay) -> None:
        queue = await async_client.queue.get_next_slot()
        assert_matches_type(QueueGetNextSlotResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_next_slot(self, async_client: AsyncRelay) -> None:
        response = await async_client.queue.with_raw_response.get_next_slot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueGetNextSlotResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_next_slot(self, async_client: AsyncRelay) -> None:
        async with async_client.queue.with_streaming_response.get_next_slot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueGetNextSlotResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncRelay) -> None:
        queue = await async_client.queue.preview()
        assert_matches_type(QueuePreviewResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncRelay) -> None:
        queue = await async_client.queue.preview(
            count=1,
        )
        assert_matches_type(QueuePreviewResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncRelay) -> None:
        response = await async_client.queue.with_raw_response.preview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueuePreviewResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncRelay) -> None:
        async with async_client.queue.with_streaming_response.preview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueuePreviewResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True
