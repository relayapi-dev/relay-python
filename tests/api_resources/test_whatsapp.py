# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from relay.types import (
    WhatsappBulkSendResponse,
    WhatsappListPhoneNumbersResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhatsapp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_send(self, client: Relay) -> None:
        whatsapp = client.whatsapp.bulk_send(
            account_id="account_id",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )
        assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_send_with_all_params(self, client: Relay) -> None:
        whatsapp = client.whatsapp.bulk_send(
            account_id="account_id",
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
        )
        assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_send(self, client: Relay) -> None:
        response = client.whatsapp.with_raw_response.bulk_send(
            account_id="account_id",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = response.parse()
        assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_send(self, client: Relay) -> None:
        with client.whatsapp.with_streaming_response.bulk_send(
            account_id="account_id",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = response.parse()
            assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_phone_numbers(self, client: Relay) -> None:
        whatsapp = client.whatsapp.list_phone_numbers(
            account_id="account_id",
        )
        assert_matches_type(WhatsappListPhoneNumbersResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_phone_numbers(self, client: Relay) -> None:
        response = client.whatsapp.with_raw_response.list_phone_numbers(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = response.parse()
        assert_matches_type(WhatsappListPhoneNumbersResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_phone_numbers(self, client: Relay) -> None:
        with client.whatsapp.with_streaming_response.list_phone_numbers(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = response.parse()
            assert_matches_type(WhatsappListPhoneNumbersResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWhatsapp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_send(self, async_client: AsyncRelay) -> None:
        whatsapp = await async_client.whatsapp.bulk_send(
            account_id="account_id",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )
        assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_send_with_all_params(self, async_client: AsyncRelay) -> None:
        whatsapp = await async_client.whatsapp.bulk_send(
            account_id="account_id",
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
        )
        assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_send(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.with_raw_response.bulk_send(
            account_id="account_id",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = await response.parse()
        assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_send(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.with_streaming_response.bulk_send(
            account_id="account_id",
            recipients=[{"phone": "phone"}],
            template={
                "language": "language",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = await response.parse()
            assert_matches_type(WhatsappBulkSendResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_phone_numbers(self, async_client: AsyncRelay) -> None:
        whatsapp = await async_client.whatsapp.list_phone_numbers(
            account_id="account_id",
        )
        assert_matches_type(WhatsappListPhoneNumbersResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_phone_numbers(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.with_raw_response.list_phone_numbers(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = await response.parse()
        assert_matches_type(WhatsappListPhoneNumbersResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_phone_numbers(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.with_streaming_response.list_phone_numbers(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = await response.parse()
            assert_matches_type(WhatsappListPhoneNumbersResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True
