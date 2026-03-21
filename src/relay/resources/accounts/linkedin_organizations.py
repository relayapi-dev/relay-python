# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.accounts import linkedin_organization_switch_type_params
from ...types.accounts.linkedin_organization_retrieve_response import LinkedinOrganizationRetrieveResponse
from ...types.accounts.linkedin_organization_switch_type_response import LinkedinOrganizationSwitchTypeResponse

__all__ = ["LinkedinOrganizationsResource", "AsyncLinkedinOrganizationsResource"]


class LinkedinOrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinkedinOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return LinkedinOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkedinOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return LinkedinOrganizationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedinOrganizationRetrieveResponse:
        """
        Fetch LinkedIn organizations for an account

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/accounts/{id}/linkedin-organizations", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedinOrganizationRetrieveResponse,
        )

    def switch_type(
        self,
        id: str,
        *,
        account_type: Literal["personal", "organization"],
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedinOrganizationSwitchTypeResponse:
        """
        Switch LinkedIn account type

        Args:
          id: Resource ID

          account_type: Account type to switch to

          organization_id: LinkedIn organization ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/accounts/{id}/linkedin-organizations", id=id),
            body=maybe_transform(
                {
                    "account_type": account_type,
                    "organization_id": organization_id,
                },
                linkedin_organization_switch_type_params.LinkedinOrganizationSwitchTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedinOrganizationSwitchTypeResponse,
        )


class AsyncLinkedinOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinkedinOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkedinOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkedinOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncLinkedinOrganizationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedinOrganizationRetrieveResponse:
        """
        Fetch LinkedIn organizations for an account

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/accounts/{id}/linkedin-organizations", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedinOrganizationRetrieveResponse,
        )

    async def switch_type(
        self,
        id: str,
        *,
        account_type: Literal["personal", "organization"],
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedinOrganizationSwitchTypeResponse:
        """
        Switch LinkedIn account type

        Args:
          id: Resource ID

          account_type: Account type to switch to

          organization_id: LinkedIn organization ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/accounts/{id}/linkedin-organizations", id=id),
            body=await async_maybe_transform(
                {
                    "account_type": account_type,
                    "organization_id": organization_id,
                },
                linkedin_organization_switch_type_params.LinkedinOrganizationSwitchTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedinOrganizationSwitchTypeResponse,
        )


class LinkedinOrganizationsResourceWithRawResponse:
    def __init__(self, linkedin_organizations: LinkedinOrganizationsResource) -> None:
        self._linkedin_organizations = linkedin_organizations

        self.retrieve = to_raw_response_wrapper(
            linkedin_organizations.retrieve,
        )
        self.switch_type = to_raw_response_wrapper(
            linkedin_organizations.switch_type,
        )


class AsyncLinkedinOrganizationsResourceWithRawResponse:
    def __init__(self, linkedin_organizations: AsyncLinkedinOrganizationsResource) -> None:
        self._linkedin_organizations = linkedin_organizations

        self.retrieve = async_to_raw_response_wrapper(
            linkedin_organizations.retrieve,
        )
        self.switch_type = async_to_raw_response_wrapper(
            linkedin_organizations.switch_type,
        )


class LinkedinOrganizationsResourceWithStreamingResponse:
    def __init__(self, linkedin_organizations: LinkedinOrganizationsResource) -> None:
        self._linkedin_organizations = linkedin_organizations

        self.retrieve = to_streamed_response_wrapper(
            linkedin_organizations.retrieve,
        )
        self.switch_type = to_streamed_response_wrapper(
            linkedin_organizations.switch_type,
        )


class AsyncLinkedinOrganizationsResourceWithStreamingResponse:
    def __init__(self, linkedin_organizations: AsyncLinkedinOrganizationsResource) -> None:
        self._linkedin_organizations = linkedin_organizations

        self.retrieve = async_to_streamed_response_wrapper(
            linkedin_organizations.retrieve,
        )
        self.switch_type = async_to_streamed_response_wrapper(
            linkedin_organizations.switch_type,
        )
