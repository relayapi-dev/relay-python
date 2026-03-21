# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.whatsapp import (
    BroadcastListResponse,
    BroadcastSendResponse,
    BroadcastCreateResponse,
    BroadcastRetrieveResponse,
    BroadcastScheduleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBroadcasts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.create(
            account_id="account_id",
            name="name",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.create(
            account_id="account_id",
            name="name",
            recipients=[
                {
                    "phone": "phone",
                    "variables": {"foo": "string"},
                }
            ],
            template={
                "language": "language",
                "name": "name",
                "components": [
                    {
                        "type": "header",
                        "parameters": [{"foo": "bar"}],
                    }
                ],
            },
            scheduled_at="scheduled_at",
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.whatsapp.broadcasts.with_raw_response.create(
            account_id="account_id",
            name="name",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.whatsapp.broadcasts.with_streaming_response.create(
            account_id="account_id",
            name="name",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.retrieve(
            "broadcast_id",
        )
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.whatsapp.broadcasts.with_raw_response.retrieve(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.whatsapp.broadcasts.with_streaming_response.retrieve(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.whatsapp.broadcasts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.list(
            account_id="account_id",
        )
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.whatsapp.broadcasts.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.whatsapp.broadcasts.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.delete(
            "broadcast_id",
        )
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Relay) -> None:
        response = client.whatsapp.broadcasts.with_raw_response.delete(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Relay) -> None:
        with client.whatsapp.broadcasts.with_streaming_response.delete(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.whatsapp.broadcasts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schedule(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.schedule(
            "broadcast_id",
        )
        assert_matches_type(BroadcastScheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_schedule(self, client: Relay) -> None:
        response = client.whatsapp.broadcasts.with_raw_response.schedule(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastScheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_schedule(self, client: Relay) -> None:
        with client.whatsapp.broadcasts.with_streaming_response.schedule(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastScheduleResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_schedule(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.whatsapp.broadcasts.with_raw_response.schedule(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Relay) -> None:
        broadcast = client.whatsapp.broadcasts.send(
            "broadcast_id",
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Relay) -> None:
        response = client.whatsapp.broadcasts.with_raw_response.send(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Relay) -> None:
        with client.whatsapp.broadcasts.with_streaming_response.send(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.whatsapp.broadcasts.with_raw_response.send(
                "",
            )


class TestAsyncBroadcasts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.create(
            account_id="account_id",
            name="name",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.create(
            account_id="account_id",
            name="name",
            recipients=[
                {
                    "phone": "phone",
                    "variables": {"foo": "string"},
                }
            ],
            template={
                "language": "language",
                "name": "name",
                "components": [
                    {
                        "type": "header",
                        "parameters": [{"foo": "bar"}],
                    }
                ],
            },
            scheduled_at="scheduled_at",
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.broadcasts.with_raw_response.create(
            account_id="account_id",
            name="name",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.broadcasts.with_streaming_response.create(
            account_id="account_id",
            name="name",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.retrieve(
            "broadcast_id",
        )
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.broadcasts.with_raw_response.retrieve(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.broadcasts.with_streaming_response.retrieve(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.whatsapp.broadcasts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.list(
            account_id="account_id",
        )
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.broadcasts.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.broadcasts.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.delete(
            "broadcast_id",
        )
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.broadcasts.with_raw_response.delete(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.broadcasts.with_streaming_response.delete(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.whatsapp.broadcasts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.schedule(
            "broadcast_id",
        )
        assert_matches_type(BroadcastScheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.broadcasts.with_raw_response.schedule(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastScheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.broadcasts.with_streaming_response.schedule(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastScheduleResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_schedule(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.whatsapp.broadcasts.with_raw_response.schedule(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncRelay) -> None:
        broadcast = await async_client.whatsapp.broadcasts.send(
            "broadcast_id",
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.broadcasts.with_raw_response.send(
            "broadcast_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.broadcasts.with_streaming_response.send(
            "broadcast_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.whatsapp.broadcasts.with_raw_response.send(
                "",
            )
