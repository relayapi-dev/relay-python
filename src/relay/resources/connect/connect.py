# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    connect_start_oauth_flow_params,
    connect_fetch_pending_data_params,
    connect_complete_oauth_callback_params,
    connect_create_bluesky_connection_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .telegram import (
    TelegramResource,
    AsyncTelegramResource,
    TelegramResourceWithRawResponse,
    AsyncTelegramResourceWithRawResponse,
    TelegramResourceWithStreamingResponse,
    AsyncTelegramResourceWithStreamingResponse,
)
from .whatsapp import (
    WhatsappResource,
    AsyncWhatsappResource,
    WhatsappResourceWithRawResponse,
    AsyncWhatsappResourceWithRawResponse,
    WhatsappResourceWithStreamingResponse,
    AsyncWhatsappResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .facebook.facebook import (
    FacebookResource,
    AsyncFacebookResource,
    FacebookResourceWithRawResponse,
    AsyncFacebookResourceWithRawResponse,
    FacebookResourceWithStreamingResponse,
    AsyncFacebookResourceWithStreamingResponse,
)
from .linkedin.linkedin import (
    LinkedinResource,
    AsyncLinkedinResource,
    LinkedinResourceWithRawResponse,
    AsyncLinkedinResourceWithRawResponse,
    LinkedinResourceWithStreamingResponse,
    AsyncLinkedinResourceWithStreamingResponse,
)
from .snapchat.snapchat import (
    SnapchatResource,
    AsyncSnapchatResource,
    SnapchatResourceWithRawResponse,
    AsyncSnapchatResourceWithRawResponse,
    SnapchatResourceWithStreamingResponse,
    AsyncSnapchatResourceWithStreamingResponse,
)
from .pinterest.pinterest import (
    PinterestResource,
    AsyncPinterestResource,
    PinterestResourceWithRawResponse,
    AsyncPinterestResourceWithRawResponse,
    PinterestResourceWithStreamingResponse,
    AsyncPinterestResourceWithStreamingResponse,
)
from .googlebusiness.googlebusiness import (
    GooglebusinessResource,
    AsyncGooglebusinessResource,
    GooglebusinessResourceWithRawResponse,
    AsyncGooglebusinessResourceWithRawResponse,
    GooglebusinessResourceWithStreamingResponse,
    AsyncGooglebusinessResourceWithStreamingResponse,
)
from ...types.connect_start_oauth_flow_response import ConnectStartOAuthFlowResponse
from ...types.connect_fetch_pending_data_response import ConnectFetchPendingDataResponse
from ...types.connect_complete_oauth_callback_response import ConnectCompleteOAuthCallbackResponse
from ...types.connect_create_bluesky_connection_response import ConnectCreateBlueskyConnectionResponse

__all__ = ["ConnectResource", "AsyncConnectResource"]


class ConnectResource(SyncAPIResource):
    @cached_property
    def telegram(self) -> TelegramResource:
        return TelegramResource(self._client)

    @cached_property
    def whatsapp(self) -> WhatsappResource:
        return WhatsappResource(self._client)

    @cached_property
    def facebook(self) -> FacebookResource:
        return FacebookResource(self._client)

    @cached_property
    def linkedin(self) -> LinkedinResource:
        return LinkedinResource(self._client)

    @cached_property
    def pinterest(self) -> PinterestResource:
        return PinterestResource(self._client)

    @cached_property
    def googlebusiness(self) -> GooglebusinessResource:
        return GooglebusinessResource(self._client)

    @cached_property
    def snapchat(self) -> SnapchatResource:
        return SnapchatResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return ConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return ConnectResourceWithStreamingResponse(self)

    def complete_oauth_callback(
        self,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "threads",
            "snapchat",
            "googlebusiness",
            "mastodon",
        ],
        *,
        code: str,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectCompleteOAuthCallbackResponse:
        """
        Exchange OAuth code for tokens and save the account.

        Args:
          platform: OAuth platform to complete

          code: OAuth authorization code

          redirect_url: Redirect URL used during the OAuth flow (must match)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not platform:
            raise ValueError(f"Expected a non-empty value for `platform` but received {platform!r}")
        return self._post(
            path_template("/v1/connect/{platform}", platform=platform),
            body=maybe_transform(
                {
                    "code": code,
                    "redirect_url": redirect_url,
                },
                connect_complete_oauth_callback_params.ConnectCompleteOAuthCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectCompleteOAuthCallbackResponse,
        )

    def create_bluesky_connection(
        self,
        *,
        app_password: str,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectCreateBlueskyConnectionResponse:
        """
        Connect Bluesky via app password

        Args:
          app_password: Bluesky app password

          handle: Bluesky handle (e.g. user.bsky.social)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connect/bluesky",
            body=maybe_transform(
                {
                    "app_password": app_password,
                    "handle": handle,
                },
                connect_create_bluesky_connection_params.ConnectCreateBlueskyConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectCreateBlueskyConnectionResponse,
        )

    def fetch_pending_data(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectFetchPendingDataResponse:
        """One-time use, expires after 10 minutes.

        For headless OAuth flows.

        Args:
          token: Temporary token from headless OAuth flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connect/pending-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"token": token}, connect_fetch_pending_data_params.ConnectFetchPendingDataParams
                ),
            ),
            cast_to=ConnectFetchPendingDataResponse,
        )

    def start_oauth_flow(
        self,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "threads",
            "snapchat",
            "googlebusiness",
            "mastodon",
        ],
        *,
        headless: str | Omit = omit,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectStartOAuthFlowResponse:
        """
        Returns an auth_url to redirect the user for OAuth authorization.

        Args:
          platform: OAuth platform to connect

          headless: Set to "true" for headless mode (returns data instead of redirecting)

          redirect_url: URL to redirect after OAuth completes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not platform:
            raise ValueError(f"Expected a non-empty value for `platform` but received {platform!r}")
        return self._get(
            path_template("/v1/connect/{platform}", platform=platform),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "headless": headless,
                        "redirect_url": redirect_url,
                    },
                    connect_start_oauth_flow_params.ConnectStartOAuthFlowParams,
                ),
            ),
            cast_to=ConnectStartOAuthFlowResponse,
        )


class AsyncConnectResource(AsyncAPIResource):
    @cached_property
    def telegram(self) -> AsyncTelegramResource:
        return AsyncTelegramResource(self._client)

    @cached_property
    def whatsapp(self) -> AsyncWhatsappResource:
        return AsyncWhatsappResource(self._client)

    @cached_property
    def facebook(self) -> AsyncFacebookResource:
        return AsyncFacebookResource(self._client)

    @cached_property
    def linkedin(self) -> AsyncLinkedinResource:
        return AsyncLinkedinResource(self._client)

    @cached_property
    def pinterest(self) -> AsyncPinterestResource:
        return AsyncPinterestResource(self._client)

    @cached_property
    def googlebusiness(self) -> AsyncGooglebusinessResource:
        return AsyncGooglebusinessResource(self._client)

    @cached_property
    def snapchat(self) -> AsyncSnapchatResource:
        return AsyncSnapchatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relayapi-dev/relay-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relayapi-dev/relay-python#with_streaming_response
        """
        return AsyncConnectResourceWithStreamingResponse(self)

    async def complete_oauth_callback(
        self,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "threads",
            "snapchat",
            "googlebusiness",
            "mastodon",
        ],
        *,
        code: str,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectCompleteOAuthCallbackResponse:
        """
        Exchange OAuth code for tokens and save the account.

        Args:
          platform: OAuth platform to complete

          code: OAuth authorization code

          redirect_url: Redirect URL used during the OAuth flow (must match)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not platform:
            raise ValueError(f"Expected a non-empty value for `platform` but received {platform!r}")
        return await self._post(
            path_template("/v1/connect/{platform}", platform=platform),
            body=await async_maybe_transform(
                {
                    "code": code,
                    "redirect_url": redirect_url,
                },
                connect_complete_oauth_callback_params.ConnectCompleteOAuthCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectCompleteOAuthCallbackResponse,
        )

    async def create_bluesky_connection(
        self,
        *,
        app_password: str,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectCreateBlueskyConnectionResponse:
        """
        Connect Bluesky via app password

        Args:
          app_password: Bluesky app password

          handle: Bluesky handle (e.g. user.bsky.social)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connect/bluesky",
            body=await async_maybe_transform(
                {
                    "app_password": app_password,
                    "handle": handle,
                },
                connect_create_bluesky_connection_params.ConnectCreateBlueskyConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectCreateBlueskyConnectionResponse,
        )

    async def fetch_pending_data(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectFetchPendingDataResponse:
        """One-time use, expires after 10 minutes.

        For headless OAuth flows.

        Args:
          token: Temporary token from headless OAuth flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connect/pending-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"token": token}, connect_fetch_pending_data_params.ConnectFetchPendingDataParams
                ),
            ),
            cast_to=ConnectFetchPendingDataResponse,
        )

    async def start_oauth_flow(
        self,
        platform: Literal[
            "twitter",
            "instagram",
            "facebook",
            "linkedin",
            "tiktok",
            "youtube",
            "pinterest",
            "reddit",
            "threads",
            "snapchat",
            "googlebusiness",
            "mastodon",
        ],
        *,
        headless: str | Omit = omit,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectStartOAuthFlowResponse:
        """
        Returns an auth_url to redirect the user for OAuth authorization.

        Args:
          platform: OAuth platform to connect

          headless: Set to "true" for headless mode (returns data instead of redirecting)

          redirect_url: URL to redirect after OAuth completes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not platform:
            raise ValueError(f"Expected a non-empty value for `platform` but received {platform!r}")
        return await self._get(
            path_template("/v1/connect/{platform}", platform=platform),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "headless": headless,
                        "redirect_url": redirect_url,
                    },
                    connect_start_oauth_flow_params.ConnectStartOAuthFlowParams,
                ),
            ),
            cast_to=ConnectStartOAuthFlowResponse,
        )


class ConnectResourceWithRawResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.complete_oauth_callback = to_raw_response_wrapper(
            connect.complete_oauth_callback,
        )
        self.create_bluesky_connection = to_raw_response_wrapper(
            connect.create_bluesky_connection,
        )
        self.fetch_pending_data = to_raw_response_wrapper(
            connect.fetch_pending_data,
        )
        self.start_oauth_flow = to_raw_response_wrapper(
            connect.start_oauth_flow,
        )

    @cached_property
    def telegram(self) -> TelegramResourceWithRawResponse:
        return TelegramResourceWithRawResponse(self._connect.telegram)

    @cached_property
    def whatsapp(self) -> WhatsappResourceWithRawResponse:
        return WhatsappResourceWithRawResponse(self._connect.whatsapp)

    @cached_property
    def facebook(self) -> FacebookResourceWithRawResponse:
        return FacebookResourceWithRawResponse(self._connect.facebook)

    @cached_property
    def linkedin(self) -> LinkedinResourceWithRawResponse:
        return LinkedinResourceWithRawResponse(self._connect.linkedin)

    @cached_property
    def pinterest(self) -> PinterestResourceWithRawResponse:
        return PinterestResourceWithRawResponse(self._connect.pinterest)

    @cached_property
    def googlebusiness(self) -> GooglebusinessResourceWithRawResponse:
        return GooglebusinessResourceWithRawResponse(self._connect.googlebusiness)

    @cached_property
    def snapchat(self) -> SnapchatResourceWithRawResponse:
        return SnapchatResourceWithRawResponse(self._connect.snapchat)


class AsyncConnectResourceWithRawResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.complete_oauth_callback = async_to_raw_response_wrapper(
            connect.complete_oauth_callback,
        )
        self.create_bluesky_connection = async_to_raw_response_wrapper(
            connect.create_bluesky_connection,
        )
        self.fetch_pending_data = async_to_raw_response_wrapper(
            connect.fetch_pending_data,
        )
        self.start_oauth_flow = async_to_raw_response_wrapper(
            connect.start_oauth_flow,
        )

    @cached_property
    def telegram(self) -> AsyncTelegramResourceWithRawResponse:
        return AsyncTelegramResourceWithRawResponse(self._connect.telegram)

    @cached_property
    def whatsapp(self) -> AsyncWhatsappResourceWithRawResponse:
        return AsyncWhatsappResourceWithRawResponse(self._connect.whatsapp)

    @cached_property
    def facebook(self) -> AsyncFacebookResourceWithRawResponse:
        return AsyncFacebookResourceWithRawResponse(self._connect.facebook)

    @cached_property
    def linkedin(self) -> AsyncLinkedinResourceWithRawResponse:
        return AsyncLinkedinResourceWithRawResponse(self._connect.linkedin)

    @cached_property
    def pinterest(self) -> AsyncPinterestResourceWithRawResponse:
        return AsyncPinterestResourceWithRawResponse(self._connect.pinterest)

    @cached_property
    def googlebusiness(self) -> AsyncGooglebusinessResourceWithRawResponse:
        return AsyncGooglebusinessResourceWithRawResponse(self._connect.googlebusiness)

    @cached_property
    def snapchat(self) -> AsyncSnapchatResourceWithRawResponse:
        return AsyncSnapchatResourceWithRawResponse(self._connect.snapchat)


class ConnectResourceWithStreamingResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.complete_oauth_callback = to_streamed_response_wrapper(
            connect.complete_oauth_callback,
        )
        self.create_bluesky_connection = to_streamed_response_wrapper(
            connect.create_bluesky_connection,
        )
        self.fetch_pending_data = to_streamed_response_wrapper(
            connect.fetch_pending_data,
        )
        self.start_oauth_flow = to_streamed_response_wrapper(
            connect.start_oauth_flow,
        )

    @cached_property
    def telegram(self) -> TelegramResourceWithStreamingResponse:
        return TelegramResourceWithStreamingResponse(self._connect.telegram)

    @cached_property
    def whatsapp(self) -> WhatsappResourceWithStreamingResponse:
        return WhatsappResourceWithStreamingResponse(self._connect.whatsapp)

    @cached_property
    def facebook(self) -> FacebookResourceWithStreamingResponse:
        return FacebookResourceWithStreamingResponse(self._connect.facebook)

    @cached_property
    def linkedin(self) -> LinkedinResourceWithStreamingResponse:
        return LinkedinResourceWithStreamingResponse(self._connect.linkedin)

    @cached_property
    def pinterest(self) -> PinterestResourceWithStreamingResponse:
        return PinterestResourceWithStreamingResponse(self._connect.pinterest)

    @cached_property
    def googlebusiness(self) -> GooglebusinessResourceWithStreamingResponse:
        return GooglebusinessResourceWithStreamingResponse(self._connect.googlebusiness)

    @cached_property
    def snapchat(self) -> SnapchatResourceWithStreamingResponse:
        return SnapchatResourceWithStreamingResponse(self._connect.snapchat)


class AsyncConnectResourceWithStreamingResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.complete_oauth_callback = async_to_streamed_response_wrapper(
            connect.complete_oauth_callback,
        )
        self.create_bluesky_connection = async_to_streamed_response_wrapper(
            connect.create_bluesky_connection,
        )
        self.fetch_pending_data = async_to_streamed_response_wrapper(
            connect.fetch_pending_data,
        )
        self.start_oauth_flow = async_to_streamed_response_wrapper(
            connect.start_oauth_flow,
        )

    @cached_property
    def telegram(self) -> AsyncTelegramResourceWithStreamingResponse:
        return AsyncTelegramResourceWithStreamingResponse(self._connect.telegram)

    @cached_property
    def whatsapp(self) -> AsyncWhatsappResourceWithStreamingResponse:
        return AsyncWhatsappResourceWithStreamingResponse(self._connect.whatsapp)

    @cached_property
    def facebook(self) -> AsyncFacebookResourceWithStreamingResponse:
        return AsyncFacebookResourceWithStreamingResponse(self._connect.facebook)

    @cached_property
    def linkedin(self) -> AsyncLinkedinResourceWithStreamingResponse:
        return AsyncLinkedinResourceWithStreamingResponse(self._connect.linkedin)

    @cached_property
    def pinterest(self) -> AsyncPinterestResourceWithStreamingResponse:
        return AsyncPinterestResourceWithStreamingResponse(self._connect.pinterest)

    @cached_property
    def googlebusiness(self) -> AsyncGooglebusinessResourceWithStreamingResponse:
        return AsyncGooglebusinessResourceWithStreamingResponse(self._connect.googlebusiness)

    @cached_property
    def snapchat(self) -> AsyncSnapchatResourceWithStreamingResponse:
        return AsyncSnapchatResourceWithStreamingResponse(self._connect.snapchat)
