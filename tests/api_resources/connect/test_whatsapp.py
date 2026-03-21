# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.connect import (
    WhatsappGetSDKConfigResponse,
    WhatsappConnectViaCredentialsResponse,
    WhatsappCompleteEmbeddedSignupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhatsapp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_embedded_signup(self, client: Relay) -> None:
        whatsapp = client.connect.whatsapp.complete_embedded_signup(
            code="code",
        )
        assert_matches_type(WhatsappCompleteEmbeddedSignupResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_embedded_signup(self, client: Relay) -> None:
        response = client.connect.whatsapp.with_raw_response.complete_embedded_signup(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = response.parse()
        assert_matches_type(WhatsappCompleteEmbeddedSignupResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_embedded_signup(self, client: Relay) -> None:
        with client.connect.whatsapp.with_streaming_response.complete_embedded_signup(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = response.parse()
            assert_matches_type(WhatsappCompleteEmbeddedSignupResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_via_credentials(self, client: Relay) -> None:
        whatsapp = client.connect.whatsapp.connect_via_credentials(
            access_token="access_token",
            phone_number_id="phone_number_id",
            waba_id="waba_id",
        )
        assert_matches_type(WhatsappConnectViaCredentialsResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect_via_credentials(self, client: Relay) -> None:
        response = client.connect.whatsapp.with_raw_response.connect_via_credentials(
            access_token="access_token",
            phone_number_id="phone_number_id",
            waba_id="waba_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = response.parse()
        assert_matches_type(WhatsappConnectViaCredentialsResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect_via_credentials(self, client: Relay) -> None:
        with client.connect.whatsapp.with_streaming_response.connect_via_credentials(
            access_token="access_token",
            phone_number_id="phone_number_id",
            waba_id="waba_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = response.parse()
            assert_matches_type(WhatsappConnectViaCredentialsResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_sdk_config(self, client: Relay) -> None:
        whatsapp = client.connect.whatsapp.get_sdk_config()
        assert_matches_type(WhatsappGetSDKConfigResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_sdk_config(self, client: Relay) -> None:
        response = client.connect.whatsapp.with_raw_response.get_sdk_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = response.parse()
        assert_matches_type(WhatsappGetSDKConfigResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_sdk_config(self, client: Relay) -> None:
        with client.connect.whatsapp.with_streaming_response.get_sdk_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = response.parse()
            assert_matches_type(WhatsappGetSDKConfigResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWhatsapp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_embedded_signup(self, async_client: AsyncRelay) -> None:
        whatsapp = await async_client.connect.whatsapp.complete_embedded_signup(
            code="code",
        )
        assert_matches_type(WhatsappCompleteEmbeddedSignupResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_embedded_signup(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.whatsapp.with_raw_response.complete_embedded_signup(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = await response.parse()
        assert_matches_type(WhatsappCompleteEmbeddedSignupResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_embedded_signup(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.whatsapp.with_streaming_response.complete_embedded_signup(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = await response.parse()
            assert_matches_type(WhatsappCompleteEmbeddedSignupResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_via_credentials(self, async_client: AsyncRelay) -> None:
        whatsapp = await async_client.connect.whatsapp.connect_via_credentials(
            access_token="access_token",
            phone_number_id="phone_number_id",
            waba_id="waba_id",
        )
        assert_matches_type(WhatsappConnectViaCredentialsResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect_via_credentials(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.whatsapp.with_raw_response.connect_via_credentials(
            access_token="access_token",
            phone_number_id="phone_number_id",
            waba_id="waba_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = await response.parse()
        assert_matches_type(WhatsappConnectViaCredentialsResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect_via_credentials(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.whatsapp.with_streaming_response.connect_via_credentials(
            access_token="access_token",
            phone_number_id="phone_number_id",
            waba_id="waba_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = await response.parse()
            assert_matches_type(WhatsappConnectViaCredentialsResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_sdk_config(self, async_client: AsyncRelay) -> None:
        whatsapp = await async_client.connect.whatsapp.get_sdk_config()
        assert_matches_type(WhatsappGetSDKConfigResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_sdk_config(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.whatsapp.with_raw_response.get_sdk_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = await response.parse()
        assert_matches_type(WhatsappGetSDKConfigResponse, whatsapp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_sdk_config(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.whatsapp.with_streaming_response.get_sdk_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = await response.parse()
            assert_matches_type(WhatsappGetSDKConfigResponse, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True
