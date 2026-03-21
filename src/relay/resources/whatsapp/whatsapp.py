# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ...types import whatsapp_bulk_send_params, whatsapp_list_phone_numbers_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from .broadcasts import (
    BroadcastsResource,
    AsyncBroadcastsResource,
    BroadcastsResourceWithRawResponse,
    AsyncBroadcastsResourceWithRawResponse,
    BroadcastsResourceWithStreamingResponse,
    AsyncBroadcastsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .business_profile import (
    BusinessProfileResource,
    AsyncBusinessProfileResource,
    BusinessProfileResourceWithRawResponse,
    AsyncBusinessProfileResourceWithRawResponse,
    BusinessProfileResourceWithStreamingResponse,
    AsyncBusinessProfileResourceWithStreamingResponse,
)
from ...types.whatsapp_bulk_send_response import WhatsappBulkSendResponse
from ...types.whatsapp_list_phone_numbers_response import WhatsappListPhoneNumbersResponse

__all__ = ["WhatsappResource", "AsyncWhatsappResource"]


class WhatsappResource(SyncAPIResource):
    @cached_property
    def broadcasts(self) -> BroadcastsResource:
        return BroadcastsResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def business_profile(self) -> BusinessProfileResource:
        return BusinessProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> WhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return WhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return WhatsappResourceWithStreamingResponse(self)

    def bulk_send(
        self,
        *,
        account_id: str,
        recipients: Iterable[whatsapp_bulk_send_params.Recipient],
        template: whatsapp_bulk_send_params.Template,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappBulkSendResponse:
        """
        Send bulk WhatsApp messages via template

        Args:
          account_id: WhatsApp account ID

          recipients: Recipients

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/whatsapp/bulk-send",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "recipients": recipients,
                    "template": template,
                },
                whatsapp_bulk_send_params.WhatsappBulkSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappBulkSendResponse,
        )

    def list_phone_numbers(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappListPhoneNumbersResponse:
        """
        List registered phone numbers

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/whatsapp/phone-numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, whatsapp_list_phone_numbers_params.WhatsappListPhoneNumbersParams
                ),
            ),
            cast_to=WhatsappListPhoneNumbersResponse,
        )


class AsyncWhatsappResource(AsyncAPIResource):
    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResource:
        return AsyncBroadcastsResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def business_profile(self) -> AsyncBusinessProfileResource:
        return AsyncBusinessProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncWhatsappResourceWithStreamingResponse(self)

    async def bulk_send(
        self,
        *,
        account_id: str,
        recipients: Iterable[whatsapp_bulk_send_params.Recipient],
        template: whatsapp_bulk_send_params.Template,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappBulkSendResponse:
        """
        Send bulk WhatsApp messages via template

        Args:
          account_id: WhatsApp account ID

          recipients: Recipients

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/whatsapp/bulk-send",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "recipients": recipients,
                    "template": template,
                },
                whatsapp_bulk_send_params.WhatsappBulkSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappBulkSendResponse,
        )

    async def list_phone_numbers(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappListPhoneNumbersResponse:
        """
        List registered phone numbers

        Args:
          account_id: WhatsApp account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/whatsapp/phone-numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, whatsapp_list_phone_numbers_params.WhatsappListPhoneNumbersParams
                ),
            ),
            cast_to=WhatsappListPhoneNumbersResponse,
        )


class WhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.bulk_send = to_raw_response_wrapper(
            whatsapp.bulk_send,
        )
        self.list_phone_numbers = to_raw_response_wrapper(
            whatsapp.list_phone_numbers,
        )

    @cached_property
    def broadcasts(self) -> BroadcastsResourceWithRawResponse:
        return BroadcastsResourceWithRawResponse(self._whatsapp.broadcasts)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._whatsapp.templates)

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._whatsapp.contacts)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._whatsapp.groups)

    @cached_property
    def business_profile(self) -> BusinessProfileResourceWithRawResponse:
        return BusinessProfileResourceWithRawResponse(self._whatsapp.business_profile)


class AsyncWhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.bulk_send = async_to_raw_response_wrapper(
            whatsapp.bulk_send,
        )
        self.list_phone_numbers = async_to_raw_response_wrapper(
            whatsapp.list_phone_numbers,
        )

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResourceWithRawResponse:
        return AsyncBroadcastsResourceWithRawResponse(self._whatsapp.broadcasts)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._whatsapp.templates)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._whatsapp.contacts)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._whatsapp.groups)

    @cached_property
    def business_profile(self) -> AsyncBusinessProfileResourceWithRawResponse:
        return AsyncBusinessProfileResourceWithRawResponse(self._whatsapp.business_profile)


class WhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.bulk_send = to_streamed_response_wrapper(
            whatsapp.bulk_send,
        )
        self.list_phone_numbers = to_streamed_response_wrapper(
            whatsapp.list_phone_numbers,
        )

    @cached_property
    def broadcasts(self) -> BroadcastsResourceWithStreamingResponse:
        return BroadcastsResourceWithStreamingResponse(self._whatsapp.broadcasts)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._whatsapp.templates)

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._whatsapp.contacts)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._whatsapp.groups)

    @cached_property
    def business_profile(self) -> BusinessProfileResourceWithStreamingResponse:
        return BusinessProfileResourceWithStreamingResponse(self._whatsapp.business_profile)


class AsyncWhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.bulk_send = async_to_streamed_response_wrapper(
            whatsapp.bulk_send,
        )
        self.list_phone_numbers = async_to_streamed_response_wrapper(
            whatsapp.list_phone_numbers,
        )

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        return AsyncBroadcastsResourceWithStreamingResponse(self._whatsapp.broadcasts)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._whatsapp.templates)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._whatsapp.contacts)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._whatsapp.groups)

    @cached_property
    def business_profile(self) -> AsyncBusinessProfileResourceWithStreamingResponse:
        return AsyncBusinessProfileResourceWithStreamingResponse(self._whatsapp.business_profile)
