# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.connect.facebook import PageListResponse, PageSelectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Relay) -> None:
        page = client.connect.facebook.pages.list()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Relay) -> None:
        response = client.connect.facebook.pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Relay) -> None:
        with client.connect.facebook.pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageListResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_select(self, client: Relay) -> None:
        page = client.connect.facebook.pages.select(
            connect_token="connect_token",
            page_id="page_id",
        )
        assert_matches_type(PageSelectResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_select(self, client: Relay) -> None:
        response = client.connect.facebook.pages.with_raw_response.select(
            connect_token="connect_token",
            page_id="page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageSelectResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_select(self, client: Relay) -> None:
        with client.connect.facebook.pages.with_streaming_response.select(
            connect_token="connect_token",
            page_id="page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageSelectResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRelay) -> None:
        page = await async_client.connect.facebook.pages.list()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.facebook.pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.facebook.pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageListResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_select(self, async_client: AsyncRelay) -> None:
        page = await async_client.connect.facebook.pages.select(
            connect_token="connect_token",
            page_id="page_id",
        )
        assert_matches_type(PageSelectResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_select(self, async_client: AsyncRelay) -> None:
        response = await async_client.connect.facebook.pages.with_raw_response.select(
            connect_token="connect_token",
            page_id="page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageSelectResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_select(self, async_client: AsyncRelay) -> None:
        async with async_client.connect.facebook.pages.with_streaming_response.select(
            connect_token="connect_token",
            page_id="page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageSelectResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True
