# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .health import (
    HealthResource,
    AsyncHealthResource,
    HealthResourceWithRawResponse,
    AsyncHealthResourceWithRawResponse,
    HealthResourceWithStreamingResponse,
    AsyncHealthResourceWithStreamingResponse,
)
from ...types import account_list_params, account_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .gmb_locations import (
    GmbLocationsResource,
    AsyncGmbLocationsResource,
    GmbLocationsResourceWithRawResponse,
    AsyncGmbLocationsResourceWithRawResponse,
    GmbLocationsResourceWithStreamingResponse,
    AsyncGmbLocationsResourceWithStreamingResponse,
)
from .reddit_flairs import (
    RedditFlairsResource,
    AsyncRedditFlairsResource,
    RedditFlairsResourceWithRawResponse,
    AsyncRedditFlairsResourceWithRawResponse,
    RedditFlairsResourceWithStreamingResponse,
    AsyncRedditFlairsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .facebook_pages import (
    FacebookPagesResource,
    AsyncFacebookPagesResource,
    FacebookPagesResourceWithRawResponse,
    AsyncFacebookPagesResourceWithRawResponse,
    FacebookPagesResourceWithStreamingResponse,
    AsyncFacebookPagesResourceWithStreamingResponse,
)
from .pinterest_boards import (
    PinterestBoardsResource,
    AsyncPinterestBoardsResource,
    PinterestBoardsResourceWithRawResponse,
    AsyncPinterestBoardsResourceWithRawResponse,
    PinterestBoardsResourceWithStreamingResponse,
    AsyncPinterestBoardsResourceWithStreamingResponse,
)
from .reddit_subreddits import (
    RedditSubredditsResource,
    AsyncRedditSubredditsResource,
    RedditSubredditsResourceWithRawResponse,
    AsyncRedditSubredditsResourceWithRawResponse,
    RedditSubredditsResourceWithStreamingResponse,
    AsyncRedditSubredditsResourceWithStreamingResponse,
)
from .linkedin_organizations import (
    LinkedinOrganizationsResource,
    AsyncLinkedinOrganizationsResource,
    LinkedinOrganizationsResourceWithRawResponse,
    AsyncLinkedinOrganizationsResourceWithRawResponse,
    LinkedinOrganizationsResourceWithStreamingResponse,
    AsyncLinkedinOrganizationsResourceWithStreamingResponse,
)
from ...types.account_list_response import AccountListResponse
from ...types.account_update_response import AccountUpdateResponse
from ...types.account_retrieve_response import AccountRetrieveResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def health(self) -> HealthResource:
        return HealthResource(self._client)

    @cached_property
    def reddit_flairs(self) -> RedditFlairsResource:
        return RedditFlairsResource(self._client)

    @cached_property
    def facebook_pages(self) -> FacebookPagesResource:
        return FacebookPagesResource(self._client)

    @cached_property
    def linkedin_organizations(self) -> LinkedinOrganizationsResource:
        return LinkedinOrganizationsResource(self._client)

    @cached_property
    def pinterest_boards(self) -> PinterestBoardsResource:
        return PinterestBoardsResource(self._client)

    @cached_property
    def reddit_subreddits(self) -> RedditSubredditsResource:
        return RedditSubredditsResource(self._client)

    @cached_property
    def gmb_locations(self) -> GmbLocationsResource:
        return GmbLocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

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
    ) -> AccountRetrieveResponse:
        """
        Get a connected account

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
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        display_name: str | Omit = omit,
        metadata: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUpdateResponse:
        """
        Update account metadata

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/accounts/{id}", id=id),
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "metadata": metadata,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListResponse:
        """
        List connected accounts

        Args:
          cursor: Pagination cursor

          limit: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
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
        Disconnect a social account

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
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def health(self) -> AsyncHealthResource:
        return AsyncHealthResource(self._client)

    @cached_property
    def reddit_flairs(self) -> AsyncRedditFlairsResource:
        return AsyncRedditFlairsResource(self._client)

    @cached_property
    def facebook_pages(self) -> AsyncFacebookPagesResource:
        return AsyncFacebookPagesResource(self._client)

    @cached_property
    def linkedin_organizations(self) -> AsyncLinkedinOrganizationsResource:
        return AsyncLinkedinOrganizationsResource(self._client)

    @cached_property
    def pinterest_boards(self) -> AsyncPinterestBoardsResource:
        return AsyncPinterestBoardsResource(self._client)

    @cached_property
    def reddit_subreddits(self) -> AsyncRedditSubredditsResource:
        return AsyncRedditSubredditsResource(self._client)

    @cached_property
    def gmb_locations(self) -> AsyncGmbLocationsResource:
        return AsyncGmbLocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

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
    ) -> AccountRetrieveResponse:
        """
        Get a connected account

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
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        display_name: str | Omit = omit,
        metadata: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUpdateResponse:
        """
        Update account metadata

        Args:
          id: Resource ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/accounts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "metadata": metadata,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListResponse:
        """
        List connected accounts

        Args:
          cursor: Pagination cursor

          limit: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
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
        Disconnect a social account

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
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            accounts.delete,
        )

    @cached_property
    def health(self) -> HealthResourceWithRawResponse:
        return HealthResourceWithRawResponse(self._accounts.health)

    @cached_property
    def reddit_flairs(self) -> RedditFlairsResourceWithRawResponse:
        return RedditFlairsResourceWithRawResponse(self._accounts.reddit_flairs)

    @cached_property
    def facebook_pages(self) -> FacebookPagesResourceWithRawResponse:
        return FacebookPagesResourceWithRawResponse(self._accounts.facebook_pages)

    @cached_property
    def linkedin_organizations(self) -> LinkedinOrganizationsResourceWithRawResponse:
        return LinkedinOrganizationsResourceWithRawResponse(self._accounts.linkedin_organizations)

    @cached_property
    def pinterest_boards(self) -> PinterestBoardsResourceWithRawResponse:
        return PinterestBoardsResourceWithRawResponse(self._accounts.pinterest_boards)

    @cached_property
    def reddit_subreddits(self) -> RedditSubredditsResourceWithRawResponse:
        return RedditSubredditsResourceWithRawResponse(self._accounts.reddit_subreddits)

    @cached_property
    def gmb_locations(self) -> GmbLocationsResourceWithRawResponse:
        return GmbLocationsResourceWithRawResponse(self._accounts.gmb_locations)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            accounts.delete,
        )

    @cached_property
    def health(self) -> AsyncHealthResourceWithRawResponse:
        return AsyncHealthResourceWithRawResponse(self._accounts.health)

    @cached_property
    def reddit_flairs(self) -> AsyncRedditFlairsResourceWithRawResponse:
        return AsyncRedditFlairsResourceWithRawResponse(self._accounts.reddit_flairs)

    @cached_property
    def facebook_pages(self) -> AsyncFacebookPagesResourceWithRawResponse:
        return AsyncFacebookPagesResourceWithRawResponse(self._accounts.facebook_pages)

    @cached_property
    def linkedin_organizations(self) -> AsyncLinkedinOrganizationsResourceWithRawResponse:
        return AsyncLinkedinOrganizationsResourceWithRawResponse(self._accounts.linkedin_organizations)

    @cached_property
    def pinterest_boards(self) -> AsyncPinterestBoardsResourceWithRawResponse:
        return AsyncPinterestBoardsResourceWithRawResponse(self._accounts.pinterest_boards)

    @cached_property
    def reddit_subreddits(self) -> AsyncRedditSubredditsResourceWithRawResponse:
        return AsyncRedditSubredditsResourceWithRawResponse(self._accounts.reddit_subreddits)

    @cached_property
    def gmb_locations(self) -> AsyncGmbLocationsResourceWithRawResponse:
        return AsyncGmbLocationsResourceWithRawResponse(self._accounts.gmb_locations)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            accounts.delete,
        )

    @cached_property
    def health(self) -> HealthResourceWithStreamingResponse:
        return HealthResourceWithStreamingResponse(self._accounts.health)

    @cached_property
    def reddit_flairs(self) -> RedditFlairsResourceWithStreamingResponse:
        return RedditFlairsResourceWithStreamingResponse(self._accounts.reddit_flairs)

    @cached_property
    def facebook_pages(self) -> FacebookPagesResourceWithStreamingResponse:
        return FacebookPagesResourceWithStreamingResponse(self._accounts.facebook_pages)

    @cached_property
    def linkedin_organizations(self) -> LinkedinOrganizationsResourceWithStreamingResponse:
        return LinkedinOrganizationsResourceWithStreamingResponse(self._accounts.linkedin_organizations)

    @cached_property
    def pinterest_boards(self) -> PinterestBoardsResourceWithStreamingResponse:
        return PinterestBoardsResourceWithStreamingResponse(self._accounts.pinterest_boards)

    @cached_property
    def reddit_subreddits(self) -> RedditSubredditsResourceWithStreamingResponse:
        return RedditSubredditsResourceWithStreamingResponse(self._accounts.reddit_subreddits)

    @cached_property
    def gmb_locations(self) -> GmbLocationsResourceWithStreamingResponse:
        return GmbLocationsResourceWithStreamingResponse(self._accounts.gmb_locations)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            accounts.delete,
        )

    @cached_property
    def health(self) -> AsyncHealthResourceWithStreamingResponse:
        return AsyncHealthResourceWithStreamingResponse(self._accounts.health)

    @cached_property
    def reddit_flairs(self) -> AsyncRedditFlairsResourceWithStreamingResponse:
        return AsyncRedditFlairsResourceWithStreamingResponse(self._accounts.reddit_flairs)

    @cached_property
    def facebook_pages(self) -> AsyncFacebookPagesResourceWithStreamingResponse:
        return AsyncFacebookPagesResourceWithStreamingResponse(self._accounts.facebook_pages)

    @cached_property
    def linkedin_organizations(self) -> AsyncLinkedinOrganizationsResourceWithStreamingResponse:
        return AsyncLinkedinOrganizationsResourceWithStreamingResponse(self._accounts.linkedin_organizations)

    @cached_property
    def pinterest_boards(self) -> AsyncPinterestBoardsResourceWithStreamingResponse:
        return AsyncPinterestBoardsResourceWithStreamingResponse(self._accounts.pinterest_boards)

    @cached_property
    def reddit_subreddits(self) -> AsyncRedditSubredditsResourceWithStreamingResponse:
        return AsyncRedditSubredditsResourceWithStreamingResponse(self._accounts.reddit_subreddits)

    @cached_property
    def gmb_locations(self) -> AsyncGmbLocationsResourceWithStreamingResponse:
        return AsyncGmbLocationsResourceWithStreamingResponse(self._accounts.gmb_locations)
