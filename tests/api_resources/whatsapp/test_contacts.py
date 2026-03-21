# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.whatsapp import (
    ContactListResponse,
    ContactCreateResponse,
    ContactImportResponse,
    ContactRetrieveResponse,
    ContactBulkOperationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.create(
            account_id="account_id",
            phone="phone",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.create(
            account_id="account_id",
            phone="phone",
            email="email",
            name="name",
            tags=["string"],
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Relay) -> None:
        response = client.whatsapp.contacts.with_raw_response.create(
            account_id="account_id",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Relay) -> None:
        with client.whatsapp.contacts.with_streaming_response.create(
            account_id="account_id",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.retrieve(
            "contact_id",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Relay) -> None:
        response = client.whatsapp.contacts.with_raw_response.retrieve(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Relay) -> None:
        with client.whatsapp.contacts.with_streaming_response.retrieve(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.whatsapp.contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.list(
            account_id="account_id",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
            search="search",
            tag="tag",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.whatsapp.contacts.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.whatsapp.contacts.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.delete(
            "contact_id",
        )
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Relay) -> None:
        response = client.whatsapp.contacts.with_raw_response.delete(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Relay) -> None:
        with client.whatsapp.contacts.with_streaming_response.delete(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Relay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.whatsapp.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_operations(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
        )
        assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_operations_with_all_params(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
            tags=["string"],
        )
        assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_operations(self, client: Relay) -> None:
        response = client.whatsapp.contacts.with_raw_response.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_operations(self, client: Relay) -> None:
        with client.whatsapp.contacts.with_streaming_response.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import(self, client: Relay) -> None:
        contact = client.whatsapp.contacts.import_(
            account_id="account_id",
            contacts=[{"phone": "phone"}],
        )
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: Relay) -> None:
        response = client.whatsapp.contacts.with_raw_response.import_(
            account_id="account_id",
            contacts=[{"phone": "phone"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: Relay) -> None:
        with client.whatsapp.contacts.with_streaming_response.import_(
            account_id="account_id",
            contacts=[{"phone": "phone"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactImportResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.create(
            account_id="account_id",
            phone="phone",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.create(
            account_id="account_id",
            phone="phone",
            email="email",
            name="name",
            tags=["string"],
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.contacts.with_raw_response.create(
            account_id="account_id",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.contacts.with_streaming_response.create(
            account_id="account_id",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.retrieve(
            "contact_id",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.contacts.with_raw_response.retrieve(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.contacts.with_streaming_response.retrieve(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.whatsapp.contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.list(
            account_id="account_id",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
            search="search",
            tag="tag",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.contacts.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.contacts.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.delete(
            "contact_id",
        )
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.contacts.with_raw_response.delete(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.contacts.with_streaming_response.delete(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRelay) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.whatsapp.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_operations(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
        )
        assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_operations_with_all_params(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
            tags=["string"],
        )
        assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_operations(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.contacts.with_raw_response.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_operations(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.contacts.with_streaming_response.bulk_operations(
            account_id="account_id",
            action="add_tags",
            contact_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactBulkOperationsResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncRelay) -> None:
        contact = await async_client.whatsapp.contacts.import_(
            account_id="account_id",
            contacts=[{"phone": "phone"}],
        )
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncRelay) -> None:
        response = await async_client.whatsapp.contacts.with_raw_response.import_(
            account_id="account_id",
            contacts=[{"phone": "phone"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncRelay) -> None:
        async with async_client.whatsapp.contacts.with_streaming_response.import_(
            account_id="account_id",
            contacts=[{"phone": "phone"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactImportResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
