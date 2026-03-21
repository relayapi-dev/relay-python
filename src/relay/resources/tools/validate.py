# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tools import (
    validate_validate_post_params,
    validate_validate_media_params,
    validate_check_post_length_params,
    validate_retrieve_subreddit_params,
)
from ..._base_client import make_request_options
from ...types.tools.validate_validate_post_response import ValidateValidatePostResponse
from ...types.tools.validate_validate_media_response import ValidateValidateMediaResponse
from ...types.tools.validate_check_post_length_response import ValidateCheckPostLengthResponse
from ...types.tools.validate_retrieve_subreddit_response import ValidateRetrieveSubredditResponse

__all__ = ["ValidateResource", "AsyncValidateResource"]


class ValidateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return ValidateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return ValidateResourceWithStreamingResponse(self)

    def check_post_length(
        self,
        *,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateCheckPostLengthResponse:
        """
        Check character counts against platform limits

        Args:
          content: Post content to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/validate/post-length",
            body=maybe_transform({"content": content}, validate_check_post_length_params.ValidateCheckPostLengthParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateCheckPostLengthResponse,
        )

    def retrieve_subreddit(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateRetrieveSubredditResponse:
        """
        Check if a subreddit exists and get its details

        Args:
          name: Subreddit name (without r/ prefix)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tools/validate/subreddit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"name": name}, validate_retrieve_subreddit_params.ValidateRetrieveSubredditParams
                ),
            ),
            cast_to=ValidateRetrieveSubredditResponse,
        )

    def validate_media(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateValidateMediaResponse:
        """
        Validate a media URL for platform compatibility

        Args:
          url: Media URL to validate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/validate/media",
            body=maybe_transform({"url": url}, validate_validate_media_params.ValidateValidateMediaParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateValidateMediaResponse,
        )

    def validate_post(
        self,
        *,
        scheduled_at: str,
        targets: SequenceNotStr[str],
        content: str | Omit = omit,
        media: Iterable[validate_validate_post_params.Media] | Omit = omit,
        target_options: Dict[str, Dict[str, Optional[object]]] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateValidatePostResponse:
        """
        Validate a post (dry-run without publishing)

        Args:
          scheduled_at: Publish intent. Use "now" to publish immediately, "draft" to save as draft, or
              an ISO 8601 timestamp to schedule.

          targets: Account IDs or platform names to publish to

          content: Post text. Optional if target_options provide per-target content.

          media: Media attachments

          target_options: Per-target customizations keyed by target value (account ID or platform name)

          timezone: IANA timezone for scheduling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/validate/post",
            body=maybe_transform(
                {
                    "scheduled_at": scheduled_at,
                    "targets": targets,
                    "content": content,
                    "media": media,
                    "target_options": target_options,
                    "timezone": timezone,
                },
                validate_validate_post_params.ValidateValidatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateValidatePostResponse,
        )


class AsyncValidateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncValidateResourceWithStreamingResponse(self)

    async def check_post_length(
        self,
        *,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateCheckPostLengthResponse:
        """
        Check character counts against platform limits

        Args:
          content: Post content to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/validate/post-length",
            body=await async_maybe_transform(
                {"content": content}, validate_check_post_length_params.ValidateCheckPostLengthParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateCheckPostLengthResponse,
        )

    async def retrieve_subreddit(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateRetrieveSubredditResponse:
        """
        Check if a subreddit exists and get its details

        Args:
          name: Subreddit name (without r/ prefix)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tools/validate/subreddit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"name": name}, validate_retrieve_subreddit_params.ValidateRetrieveSubredditParams
                ),
            ),
            cast_to=ValidateRetrieveSubredditResponse,
        )

    async def validate_media(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateValidateMediaResponse:
        """
        Validate a media URL for platform compatibility

        Args:
          url: Media URL to validate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/validate/media",
            body=await async_maybe_transform({"url": url}, validate_validate_media_params.ValidateValidateMediaParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateValidateMediaResponse,
        )

    async def validate_post(
        self,
        *,
        scheduled_at: str,
        targets: SequenceNotStr[str],
        content: str | Omit = omit,
        media: Iterable[validate_validate_post_params.Media] | Omit = omit,
        target_options: Dict[str, Dict[str, Optional[object]]] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateValidatePostResponse:
        """
        Validate a post (dry-run without publishing)

        Args:
          scheduled_at: Publish intent. Use "now" to publish immediately, "draft" to save as draft, or
              an ISO 8601 timestamp to schedule.

          targets: Account IDs or platform names to publish to

          content: Post text. Optional if target_options provide per-target content.

          media: Media attachments

          target_options: Per-target customizations keyed by target value (account ID or platform name)

          timezone: IANA timezone for scheduling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/validate/post",
            body=await async_maybe_transform(
                {
                    "scheduled_at": scheduled_at,
                    "targets": targets,
                    "content": content,
                    "media": media,
                    "target_options": target_options,
                    "timezone": timezone,
                },
                validate_validate_post_params.ValidateValidatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateValidatePostResponse,
        )


class ValidateResourceWithRawResponse:
    def __init__(self, validate: ValidateResource) -> None:
        self._validate = validate

        self.check_post_length = to_raw_response_wrapper(
            validate.check_post_length,
        )
        self.retrieve_subreddit = to_raw_response_wrapper(
            validate.retrieve_subreddit,
        )
        self.validate_media = to_raw_response_wrapper(
            validate.validate_media,
        )
        self.validate_post = to_raw_response_wrapper(
            validate.validate_post,
        )


class AsyncValidateResourceWithRawResponse:
    def __init__(self, validate: AsyncValidateResource) -> None:
        self._validate = validate

        self.check_post_length = async_to_raw_response_wrapper(
            validate.check_post_length,
        )
        self.retrieve_subreddit = async_to_raw_response_wrapper(
            validate.retrieve_subreddit,
        )
        self.validate_media = async_to_raw_response_wrapper(
            validate.validate_media,
        )
        self.validate_post = async_to_raw_response_wrapper(
            validate.validate_post,
        )


class ValidateResourceWithStreamingResponse:
    def __init__(self, validate: ValidateResource) -> None:
        self._validate = validate

        self.check_post_length = to_streamed_response_wrapper(
            validate.check_post_length,
        )
        self.retrieve_subreddit = to_streamed_response_wrapper(
            validate.retrieve_subreddit,
        )
        self.validate_media = to_streamed_response_wrapper(
            validate.validate_media,
        )
        self.validate_post = to_streamed_response_wrapper(
            validate.validate_post,
        )


class AsyncValidateResourceWithStreamingResponse:
    def __init__(self, validate: AsyncValidateResource) -> None:
        self._validate = validate

        self.check_post_length = async_to_streamed_response_wrapper(
            validate.check_post_length,
        )
        self.retrieve_subreddit = async_to_streamed_response_wrapper(
            validate.retrieve_subreddit,
        )
        self.validate_media = async_to_streamed_response_wrapper(
            validate.validate_media,
        )
        self.validate_post = async_to_streamed_response_wrapper(
            validate.validate_post,
        )
