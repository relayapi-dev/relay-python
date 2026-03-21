# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)

__all__ = ["LinkedinResource", "AsyncLinkedinResource"]


class LinkedinResource(SyncAPIResource):
    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LinkedinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return LinkedinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkedinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return LinkedinResourceWithStreamingResponse(self)


class AsyncLinkedinResource(AsyncAPIResource):
    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLinkedinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkedinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkedinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncLinkedinResourceWithStreamingResponse(self)


class LinkedinResourceWithRawResponse:
    def __init__(self, linkedin: LinkedinResource) -> None:
        self._linkedin = linkedin

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._linkedin.organizations)


class AsyncLinkedinResourceWithRawResponse:
    def __init__(self, linkedin: AsyncLinkedinResource) -> None:
        self._linkedin = linkedin

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._linkedin.organizations)


class LinkedinResourceWithStreamingResponse:
    def __init__(self, linkedin: LinkedinResource) -> None:
        self._linkedin = linkedin

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._linkedin.organizations)


class AsyncLinkedinResourceWithStreamingResponse:
    def __init__(self, linkedin: AsyncLinkedinResource) -> None:
        self._linkedin = linkedin

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._linkedin.organizations)
