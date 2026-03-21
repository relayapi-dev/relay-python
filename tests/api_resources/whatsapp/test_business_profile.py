# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.whatsapp import (
    BusinessProfileUpdateResponse,
    BusinessProfileRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBusinessProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        business_profile = client.whatsapp.business_profile.retrieve(
            account_id="account_id",
        )
        assert_matches_type(BusinessProfileRetrieveResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.whatsapp.business_profile.with_raw_response.retrieve(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_profile = response.parse()
        assert_matches_type(BusinessProfileRetrieveResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.whatsapp.business_profile.with_streaming_response.retrieve(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_profile = response.parse()
            assert_matches_type(BusinessProfileRetrieveResponse, business_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Relay) -> None:
        business_profile = client.whatsapp.business_profile.update(
            account_id="account_id",
        )
        assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Relay) -> None:
        business_profile = client.whatsapp.business_profile.update(
            account_id="account_id",
            about="about",
            address="address",
            description="description",
            email="email",
            websites=["string"],
        )
        assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Relay) -> None:
        response = client.whatsapp.business_profile.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_profile = response.parse()
        assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Relay) -> None:
        with client.whatsapp.business_profile.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_profile = response.parse()
            assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBusinessProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        business_profile = await async_client.whatsapp.business_profile.retrieve(
            account_id="account_id",
        )
        assert_matches_type(BusinessProfileRetrieveResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.business_profile.with_raw_response.retrieve(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_profile = await response.parse()
        assert_matches_type(BusinessProfileRetrieveResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.business_profile.with_streaming_response.retrieve(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_profile = await response.parse()
            assert_matches_type(BusinessProfileRetrieveResponse, business_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRelay) -> None:
        business_profile = await async_client.whatsapp.business_profile.update(
            account_id="account_id",
        )
        assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRelay) -> None:
        business_profile = await async_client.whatsapp.business_profile.update(
            account_id="account_id",
            about="about",
            address="address",
            description="description",
            email="email",
            websites=["string"],
        )
        assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.business_profile.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_profile = await response.parse()
        assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.business_profile.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_profile = await response.parse()
            assert_matches_type(BusinessProfileUpdateResponse, business_profile, path=["response"])

        assert cast(Any, response.is_closed) is True
