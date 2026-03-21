# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import account_group_create_params, account_group_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.account_group_list_response import AccountGroupListResponse
from ..types.account_group_create_response import AccountGroupCreateResponse
from ..types.account_group_update_response import AccountGroupUpdateResponse

__all__ = ["AccountGroupsResource", "AsyncAccountGroupsResource"]


class AccountGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AccountGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AccountGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_ids: SequenceNotStr[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGroupCreateResponse:
        """
        Create an account group

        Args:
          account_ids: Account IDs to include in the group

          name: Group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/account-groups",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "name": name,
                },
                account_group_create_params.AccountGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGroupCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGroupUpdateResponse:
        """
        Update an account group

        Args:
          id: Resource ID

          account_ids: Account IDs to include in the group

          name: Group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/account-groups/{id}", id=id),
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "name": name,
                },
                account_group_update_params.AccountGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGroupUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGroupListResponse:
        """List account groups"""
        return self._get(
            "/v1/account-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGroupListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an account group

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/account-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccountGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncAccountGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_ids: SequenceNotStr[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGroupCreateResponse:
        """
        Create an account group

        Args:
          account_ids: Account IDs to include in the group

          name: Group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/account-groups",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "name": name,
                },
                account_group_create_params.AccountGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGroupCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGroupUpdateResponse:
        """
        Update an account group

        Args:
          id: Resource ID

          account_ids: Account IDs to include in the group

          name: Group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/account-groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "name": name,
                },
                account_group_update_params.AccountGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGroupUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGroupListResponse:
        """List account groups"""
        return await self._get(
            "/v1/account-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGroupListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an account group

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/account-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccountGroupsResourceWithRawResponse:
    def __init__(self, account_groups: AccountGroupsResource) -> None:
        self._account_groups = account_groups

        self.create = to_raw_response_wrapper(
            account_groups.create,
        )
        self.update = to_raw_response_wrapper(
            account_groups.update,
        )
        self.list = to_raw_response_wrapper(
            account_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            account_groups.delete,
        )


class AsyncAccountGroupsResourceWithRawResponse:
    def __init__(self, account_groups: AsyncAccountGroupsResource) -> None:
        self._account_groups = account_groups

        self.create = async_to_raw_response_wrapper(
            account_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            account_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            account_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            account_groups.delete,
        )


class AccountGroupsResourceWithStreamingResponse:
    def __init__(self, account_groups: AccountGroupsResource) -> None:
        self._account_groups = account_groups

        self.create = to_streamed_response_wrapper(
            account_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            account_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            account_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            account_groups.delete,
        )


class AsyncAccountGroupsResourceWithStreamingResponse:
    def __init__(self, account_groups: AsyncAccountGroupsResource) -> None:
        self._account_groups = account_groups

        self.create = async_to_streamed_response_wrapper(
            account_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            account_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            account_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_groups.delete,
        )
