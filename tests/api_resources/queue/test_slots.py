# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.queue import (
    SlotListResponse,
    SlotCreateResponse,
    SlotUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSlots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        slot = client.queue.slots.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
        )
        assert_matches_type(SlotCreateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Relay) -> None:
        slot = client.queue.slots.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
            name="name",
        )
        assert_matches_type(SlotCreateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.queue.slots.with_raw_response.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = response.parse()
        assert_matches_type(SlotCreateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.queue.slots.with_streaming_response.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = response.parse()
            assert_matches_type(SlotCreateResponse, slot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Relay) -> None:
        slot = client.queue.slots.update()
        assert_matches_type(SlotUpdateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Relay) -> None:
        slot = client.queue.slots.update(
            name="name",
            set_as_default=True,
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
        )
        assert_matches_type(SlotUpdateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Relay) -> None:
        response = client.queue.slots.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = response.parse()
        assert_matches_type(SlotUpdateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Relay) -> None:
        with client.queue.slots.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = response.parse()
            assert_matches_type(SlotUpdateResponse, slot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        slot = client.queue.slots.list()
        assert_matches_type(SlotListResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.queue.slots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = response.parse()
        assert_matches_type(SlotListResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.queue.slots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = response.parse()
            assert_matches_type(SlotListResponse, slot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Relay) -> None:
        slot = client.queue.slots.delete()
        assert slot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Relay) -> None:
        response = client.queue.slots.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = response.parse()
        assert slot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Relay) -> None:
        with client.queue.slots.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = response.parse()
            assert slot is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSlots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        slot = await async_client.queue.slots.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
        )
        assert_matches_type(SlotCreateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRelay) -> None:
        slot = await async_client.queue.slots.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
            name="name",
        )
        assert_matches_type(SlotCreateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.queue.slots.with_raw_response.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = await response.parse()
        assert_matches_type(SlotCreateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.queue.slots.with_streaming_response.create(
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = await response.parse()
            assert_matches_type(SlotCreateResponse, slot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRelay) -> None:
        slot = await async_client.queue.slots.update()
        assert_matches_type(SlotUpdateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRelay) -> None:
        slot = await async_client.queue.slots.update(
            name="name",
            set_as_default=True,
            slots=[
                {
                    "day_of_week": 0,
                    "time": "73:16",
                    "timezone": "timezone",
                }
            ],
        )
        assert_matches_type(SlotUpdateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRelay) -> None:
        response = await async_client.queue.slots.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = await response.parse()
        assert_matches_type(SlotUpdateResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRelay) -> None:
        async with async_client.queue.slots.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = await response.parse()
            assert_matches_type(SlotUpdateResponse, slot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        slot = await async_client.queue.slots.list()
        assert_matches_type(SlotListResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.queue.slots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = await response.parse()
        assert_matches_type(SlotListResponse, slot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.queue.slots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = await response.parse()
            assert_matches_type(SlotListResponse, slot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRelay) -> None:
        slot = await async_client.queue.slots.delete()
        assert slot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRelay) -> None:
        response = await async_client.queue.slots.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slot = await response.parse()
        assert slot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRelay) -> None:
        async with async_client.queue.slots.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slot = await response.parse()
            assert slot is None

        assert cast(Any, response.is_closed) is True
