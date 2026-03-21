# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.inbox import message_edit_params, message_list_params, message_send_params
from ..._base_client import make_request_options
from ...types.inbox.message_edit_response import MessageEditResponse
from ...types.inbox.message_list_response import MessageListResponse
from ...types.inbox.message_send_response import MessageSendResponse
from ...types.inbox.message_archive_response import MessageArchiveResponse
from ...types.inbox.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Get messages in a conversation

        Args:
          conversation_id: Conversation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/v1/inbox/messages/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        List message conversations

        Args:
          account_id: Filter by account ID

          cursor: Pagination cursor

          limit: Number of items

          platform: Filter by platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/inbox/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                        "platform": platform,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def archive(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageArchiveResponse:
        """
        Archive a conversation

        Args:
          conversation_id: Conversation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._put(
            path_template("/v1/inbox/messages/{conversation_id}/archive", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageArchiveResponse,
        )

    def edit(
        self,
        message_id: str,
        *,
        conversation_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageEditResponse:
        """
        Edit a sent message

        Args:
          conversation_id: Conversation ID

          message_id: Message ID

          text: Updated message text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            path_template(
                "/v1/inbox/messages/{conversation_id}/{message_id}",
                conversation_id=conversation_id,
                message_id=message_id,
            ),
            body=maybe_transform({"text": text}, message_edit_params.MessageEditParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageEditResponse,
        )

    def send(
        self,
        conversation_id: str,
        *,
        account_id: str,
        text: str,
        attachments: Iterable[message_send_params.Attachment] | Omit = omit,
        message_tag: str | Omit = omit,
        reply_to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """
        Send a message in a conversation

        Args:
          conversation_id: Conversation ID

          account_id: Account ID to send from

          text: Message text

          attachments: Attachments

          message_tag: Message tag (e.g. for Facebook outside 24h window)

          reply_to: Message ID to reply to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            path_template("/v1/inbox/messages/{conversation_id}", conversation_id=conversation_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                    "attachments": attachments,
                    "message_tag": message_tag,
                    "reply_to": reply_to,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Get messages in a conversation

        Args:
          conversation_id: Conversation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/v1/inbox/messages/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "bluesky",
            "threads",
            "telegram",
            "snapchat",
            "googlebusiness",
            "whatsapp",
            "mastodon",
            "discord",
            "sms",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        List message conversations

        Args:
          account_id: Filter by account ID

          cursor: Pagination cursor

          limit: Number of items

          platform: Filter by platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/inbox/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                        "platform": platform,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def archive(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageArchiveResponse:
        """
        Archive a conversation

        Args:
          conversation_id: Conversation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._put(
            path_template("/v1/inbox/messages/{conversation_id}/archive", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageArchiveResponse,
        )

    async def edit(
        self,
        message_id: str,
        *,
        conversation_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageEditResponse:
        """
        Edit a sent message

        Args:
          conversation_id: Conversation ID

          message_id: Message ID

          text: Updated message text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            path_template(
                "/v1/inbox/messages/{conversation_id}/{message_id}",
                conversation_id=conversation_id,
                message_id=message_id,
            ),
            body=await async_maybe_transform({"text": text}, message_edit_params.MessageEditParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageEditResponse,
        )

    async def send(
        self,
        conversation_id: str,
        *,
        account_id: str,
        text: str,
        attachments: Iterable[message_send_params.Attachment] | Omit = omit,
        message_tag: str | Omit = omit,
        reply_to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """
        Send a message in a conversation

        Args:
          conversation_id: Conversation ID

          account_id: Account ID to send from

          text: Message text

          attachments: Attachments

          message_tag: Message tag (e.g. for Facebook outside 24h window)

          reply_to: Message ID to reply to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            path_template("/v1/inbox/messages/{conversation_id}", conversation_id=conversation_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                    "attachments": attachments,
                    "message_tag": message_tag,
                    "reply_to": reply_to,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.archive = to_raw_response_wrapper(
            messages.archive,
        )
        self.edit = to_raw_response_wrapper(
            messages.edit,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.archive = async_to_raw_response_wrapper(
            messages.archive,
        )
        self.edit = async_to_raw_response_wrapper(
            messages.edit,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.archive = to_streamed_response_wrapper(
            messages.archive,
        )
        self.edit = to_streamed_response_wrapper(
            messages.edit,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            messages.archive,
        )
        self.edit = async_to_streamed_response_wrapper(
            messages.edit,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
