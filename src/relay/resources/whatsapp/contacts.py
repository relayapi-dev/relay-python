# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.whatsapp import (
    contact_list_params,
    contact_create_params,
    contact_import_params,
    contact_bulk_operations_params,
)
from ...types.whatsapp.contact_list_response import ContactListResponse
from ...types.whatsapp.contact_create_response import ContactCreateResponse
from ...types.whatsapp.contact_import_response import ContactImportResponse
from ...types.whatsapp.contact_retrieve_response import ContactRetrieveResponse
from ...types.whatsapp.contact_bulk_operations_response import ContactBulkOperationsResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        phone: str,
        email: str | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Create a contact

        Args:
          account_id: WhatsApp account ID

          phone: Phone number in E.164 format

          email: Email address

          name: Contact name

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/whatsapp/contacts",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "phone": phone,
                    "email": email,
                    "name": name,
                    "tags": tags,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )

    def retrieve(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveResponse:
        """
        Get contact details

        Args:
          contact_id: Contact ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            path_template("/v1/whatsapp/contacts/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        List contacts

        Args:
          account_id: WhatsApp account ID

          cursor: Pagination cursor

          limit: Number of items

          search: Search by name or phone

          tag: Filter by tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/whatsapp/contacts",
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
                        "search": search,
                        "tag": tag,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    def delete(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a contact

        Args:
          contact_id: Contact ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/whatsapp/contacts/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk_operations(
        self,
        *,
        account_id: str,
        action: Literal["add_tags", "remove_tags", "delete"],
        contact_ids: SequenceNotStr[str],
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBulkOperationsResponse:
        """
        Bulk contact operations (add/remove tags, delete)

        Args:
          account_id: WhatsApp account ID

          action: Action

          contact_ids: Contact IDs

          tags: Tags (for tag actions)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/whatsapp/contacts/bulk",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "action": action,
                    "contact_ids": contact_ids,
                    "tags": tags,
                },
                contact_bulk_operations_params.ContactBulkOperationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactBulkOperationsResponse,
        )

    def import_(
        self,
        *,
        account_id: str,
        contacts: Iterable[contact_import_params.Contact],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactImportResponse:
        """
        Bulk import contacts

        Args:
          account_id: WhatsApp account ID

          contacts: Contacts to import

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/whatsapp/contacts/import",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "contacts": contacts,
                },
                contact_import_params.ContactImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactImportResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        phone: str,
        email: str | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Create a contact

        Args:
          account_id: WhatsApp account ID

          phone: Phone number in E.164 format

          email: Email address

          name: Contact name

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/whatsapp/contacts",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "phone": phone,
                    "email": email,
                    "name": name,
                    "tags": tags,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )

    async def retrieve(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveResponse:
        """
        Get contact details

        Args:
          contact_id: Contact ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            path_template("/v1/whatsapp/contacts/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        List contacts

        Args:
          account_id: WhatsApp account ID

          cursor: Pagination cursor

          limit: Number of items

          search: Search by name or phone

          tag: Filter by tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/whatsapp/contacts",
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
                        "search": search,
                        "tag": tag,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    async def delete(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a contact

        Args:
          contact_id: Contact ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/whatsapp/contacts/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk_operations(
        self,
        *,
        account_id: str,
        action: Literal["add_tags", "remove_tags", "delete"],
        contact_ids: SequenceNotStr[str],
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBulkOperationsResponse:
        """
        Bulk contact operations (add/remove tags, delete)

        Args:
          account_id: WhatsApp account ID

          action: Action

          contact_ids: Contact IDs

          tags: Tags (for tag actions)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/whatsapp/contacts/bulk",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "action": action,
                    "contact_ids": contact_ids,
                    "tags": tags,
                },
                contact_bulk_operations_params.ContactBulkOperationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactBulkOperationsResponse,
        )

    async def import_(
        self,
        *,
        account_id: str,
        contacts: Iterable[contact_import_params.Contact],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactImportResponse:
        """
        Bulk import contacts

        Args:
          account_id: WhatsApp account ID

          contacts: Contacts to import

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/whatsapp/contacts/import",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "contacts": contacts,
                },
                contact_import_params.ContactImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactImportResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = to_raw_response_wrapper(
            contacts.delete,
        )
        self.bulk_operations = to_raw_response_wrapper(
            contacts.bulk_operations,
        )
        self.import_ = to_raw_response_wrapper(
            contacts.import_,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contacts.delete,
        )
        self.bulk_operations = async_to_raw_response_wrapper(
            contacts.bulk_operations,
        )
        self.import_ = async_to_raw_response_wrapper(
            contacts.import_,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contacts.delete,
        )
        self.bulk_operations = to_streamed_response_wrapper(
            contacts.bulk_operations,
        )
        self.import_ = to_streamed_response_wrapper(
            contacts.import_,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contacts.delete,
        )
        self.bulk_operations = async_to_streamed_response_wrapper(
            contacts.bulk_operations,
        )
        self.import_ = async_to_streamed_response_wrapper(
            contacts.import_,
        )
