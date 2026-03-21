# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from relay import Relay, AsyncRelay
from tests.utils import assert_matches_type
from relay.types.tools import (
    ValidateValidatePostResponse,
    ValidateValidateMediaResponse,
    ValidateCheckPostLengthResponse,
    ValidateRetrieveSubredditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_post_length(self, client: Relay) -> None:
        validate = client.tools.validate.check_post_length(
            content="content",
        )
        assert_matches_type(ValidateCheckPostLengthResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_post_length(self, client: Relay) -> None:
        response = client.tools.validate.with_raw_response.check_post_length(
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateCheckPostLengthResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_post_length(self, client: Relay) -> None:
        with client.tools.validate.with_streaming_response.check_post_length(
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateCheckPostLengthResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_subreddit(self, client: Relay) -> None:
        validate = client.tools.validate.retrieve_subreddit(
            name="name",
        )
        assert_matches_type(ValidateRetrieveSubredditResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_subreddit(self, client: Relay) -> None:
        response = client.tools.validate.with_raw_response.retrieve_subreddit(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateRetrieveSubredditResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_subreddit(self, client: Relay) -> None:
        with client.tools.validate.with_streaming_response.retrieve_subreddit(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateRetrieveSubredditResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_media(self, client: Relay) -> None:
        validate = client.tools.validate.validate_media(
            url="https://example.com",
        )
        assert_matches_type(ValidateValidateMediaResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_media(self, client: Relay) -> None:
        response = client.tools.validate.with_raw_response.validate_media(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateValidateMediaResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_media(self, client: Relay) -> None:
        with client.tools.validate.with_streaming_response.validate_media(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateValidateMediaResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_post(self, client: Relay) -> None:
        validate = client.tools.validate.validate_post(
            scheduled_at="now",
            targets=["string"],
        )
        assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_post_with_all_params(self, client: Relay) -> None:
        validate = client.tools.validate.validate_post(
            scheduled_at="now",
            targets=["string"],
            content="content",
            media=[
                {
                    "url": "https://example.com",
                    "type": "image",
                }
            ],
            target_options={"foo": {"foo": "bar"}},
            timezone="timezone",
        )
        assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_post(self, client: Relay) -> None:
        response = client.tools.validate.with_raw_response.validate_post(
            scheduled_at="now",
            targets=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_post(self, client: Relay) -> None:
        with client.tools.validate.with_streaming_response.validate_post(
            scheduled_at="now",
            targets=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_post_length(self, async_client: AsyncRelay) -> None:
        validate = await async_client.tools.validate.check_post_length(
            content="content",
        )
        assert_matches_type(ValidateCheckPostLengthResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_post_length(self, async_client: AsyncRelay) -> None:
        response = await async_client.tools.validate.with_raw_response.check_post_length(
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateCheckPostLengthResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_post_length(self, async_client: AsyncRelay) -> None:
        async with async_client.tools.validate.with_streaming_response.check_post_length(
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateCheckPostLengthResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_subreddit(self, async_client: AsyncRelay) -> None:
        validate = await async_client.tools.validate.retrieve_subreddit(
            name="name",
        )
        assert_matches_type(ValidateRetrieveSubredditResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_subreddit(self, async_client: AsyncRelay) -> None:
        response = await async_client.tools.validate.with_raw_response.retrieve_subreddit(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateRetrieveSubredditResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_subreddit(self, async_client: AsyncRelay) -> None:
        async with async_client.tools.validate.with_streaming_response.retrieve_subreddit(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateRetrieveSubredditResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_media(self, async_client: AsyncRelay) -> None:
        validate = await async_client.tools.validate.validate_media(
            url="https://example.com",
        )
        assert_matches_type(ValidateValidateMediaResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_media(self, async_client: AsyncRelay) -> None:
        response = await async_client.tools.validate.with_raw_response.validate_media(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateValidateMediaResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_media(self, async_client: AsyncRelay) -> None:
        async with async_client.tools.validate.with_streaming_response.validate_media(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateValidateMediaResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_post(self, async_client: AsyncRelay) -> None:
        validate = await async_client.tools.validate.validate_post(
            scheduled_at="now",
            targets=["string"],
        )
        assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_post_with_all_params(self, async_client: AsyncRelay) -> None:
        validate = await async_client.tools.validate.validate_post(
            scheduled_at="now",
            targets=["string"],
            content="content",
            media=[
                {
                    "url": "https://example.com",
                    "type": "image",
                }
            ],
            target_options={"foo": {"foo": "bar"}},
            timezone="timezone",
        )
        assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_post(self, async_client: AsyncRelay) -> None:
        response = await async_client.tools.validate.with_raw_response.validate_post(
            scheduled_at="now",
            targets=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_post(self, async_client: AsyncRelay) -> None:
        async with async_client.tools.validate.with_streaming_response.validate_post(
            scheduled_at="now",
            targets=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateValidatePostResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True
