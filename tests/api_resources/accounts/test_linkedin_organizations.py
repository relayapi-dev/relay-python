# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.accounts import (
    LinkedinOrganizationRetrieveResponse,
    LinkedinOrganizationSwitchTypeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinkedinOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        linkedin_organization = client.accounts.linkedin_organizations.retrieve(
            "id",
        )
        assert_matches_type(LinkedinOrganizationRetrieveResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.accounts.linkedin_organizations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linkedin_organization = response.parse()
        assert_matches_type(LinkedinOrganizationRetrieveResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.accounts.linkedin_organizations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linkedin_organization = response.parse()
            assert_matches_type(LinkedinOrganizationRetrieveResponse, linkedin_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.linkedin_organizations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_switch_type(self, client: Relay) -> None:
        linkedin_organization = client.accounts.linkedin_organizations.switch_type(
            id="id",
            account_type="personal",
            organization_id="organization_id",
        )
        assert_matches_type(LinkedinOrganizationSwitchTypeResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_switch_type(self, client: Relay) -> None:
        response = client.accounts.linkedin_organizations.with_raw_response.switch_type(
            id="id",
            account_type="personal",
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linkedin_organization = response.parse()
        assert_matches_type(LinkedinOrganizationSwitchTypeResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_switch_type(self, client: Relay) -> None:
        with client.accounts.linkedin_organizations.with_streaming_response.switch_type(
            id="id",
            account_type="personal",
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linkedin_organization = response.parse()
            assert_matches_type(LinkedinOrganizationSwitchTypeResponse, linkedin_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_switch_type(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.linkedin_organizations.with_raw_response.switch_type(
                id="",
                account_type="personal",
                organization_id="organization_id",
            )


class TestAsyncLinkedinOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        linkedin_organization = await async_client.accounts.linkedin_organizations.retrieve(
            "id",
        )
        assert_matches_type(LinkedinOrganizationRetrieveResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.accounts.linkedin_organizations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linkedin_organization = await response.parse()
        assert_matches_type(LinkedinOrganizationRetrieveResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.accounts.linkedin_organizations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linkedin_organization = await response.parse()
            assert_matches_type(LinkedinOrganizationRetrieveResponse, linkedin_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.linkedin_organizations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_switch_type(self, async_client: AsyncRelay) -> None:
        linkedin_organization = await async_client.accounts.linkedin_organizations.switch_type(
            id="id",
            account_type="personal",
            organization_id="organization_id",
        )
        assert_matches_type(LinkedinOrganizationSwitchTypeResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_switch_type(self, async_client: AsyncRelay) -> None:
        response = await async_client.accounts.linkedin_organizations.with_raw_response.switch_type(
            id="id",
            account_type="personal",
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linkedin_organization = await response.parse()
        assert_matches_type(LinkedinOrganizationSwitchTypeResponse, linkedin_organization, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_switch_type(self, async_client: AsyncRelay) -> None:
        async with async_client.accounts.linkedin_organizations.with_streaming_response.switch_type(
            id="id",
            account_type="personal",
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linkedin_organization = await response.parse()
            assert_matches_type(LinkedinOrganizationSwitchTypeResponse, linkedin_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_switch_type(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.linkedin_organizations.with_raw_response.switch_type(
                id="",
                account_type="personal",
                organization_id="organization_id",
            )
