# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import RelayError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        inbox,
        media,
        posts,
        queue,
        tools,
        usage,
        reddit,
        connect,
        twitter,
        accounts,
        api_keys,
        webhooks,
        whatsapp,
        analytics,
        connections,
        account_groups,
    )
    from .resources.media import MediaResource, AsyncMediaResource
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.reddit import RedditResource, AsyncRedditResource
    from .resources.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.connections import ConnectionsResource, AsyncConnectionsResource
    from .resources.inbox.inbox import InboxResource, AsyncInboxResource
    from .resources.posts.posts import PostsResource, AsyncPostsResource
    from .resources.queue.queue import QueueResource, AsyncQueueResource
    from .resources.tools.tools import ToolsResource, AsyncToolsResource
    from .resources.account_groups import AccountGroupsResource, AsyncAccountGroupsResource
    from .resources.connect.connect import ConnectResource, AsyncConnectResource
    from .resources.twitter.twitter import TwitterResource, AsyncTwitterResource
    from .resources.accounts.accounts import AccountsResource, AsyncAccountsResource
    from .resources.whatsapp.whatsapp import WhatsappResource, AsyncWhatsappResource
    from .resources.analytics.analytics import AnalyticsResource, AsyncAnalyticsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Relay", "AsyncRelay", "Client", "AsyncClient"]


class Relay(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Relay client instance.

        This automatically infers the `api_key` argument from the `RELAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RELAY_API_KEY")
        if api_key is None:
            raise RelayError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RELAY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("RELAY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.relayapi.dev"

        custom_headers_env = os.environ.get("RELAY_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def posts(self) -> PostsResource:
        from .resources.posts import PostsResource

        return PostsResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def media(self) -> MediaResource:
        from .resources.media import MediaResource

        return MediaResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def account_groups(self) -> AccountGroupsResource:
        from .resources.account_groups import AccountGroupsResource

        return AccountGroupsResource(self)

    @cached_property
    def connect(self) -> ConnectResource:
        from .resources.connect import ConnectResource

        return ConnectResource(self)

    @cached_property
    def connections(self) -> ConnectionsResource:
        from .resources.connections import ConnectionsResource

        return ConnectionsResource(self)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        from .resources.analytics import AnalyticsResource

        return AnalyticsResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def queue(self) -> QueueResource:
        from .resources.queue import QueueResource

        return QueueResource(self)

    @cached_property
    def twitter(self) -> TwitterResource:
        from .resources.twitter import TwitterResource

        return TwitterResource(self)

    @cached_property
    def inbox(self) -> InboxResource:
        from .resources.inbox import InboxResource

        return InboxResource(self)

    @cached_property
    def reddit(self) -> RedditResource:
        from .resources.reddit import RedditResource

        return RedditResource(self)

    @cached_property
    def whatsapp(self) -> WhatsappResource:
        from .resources.whatsapp import WhatsappResource

        return WhatsappResource(self)

    @cached_property
    def with_raw_response(self) -> RelayWithRawResponse:
        return RelayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelayWithStreamedResponse:
        return RelayWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer if security.get("bearer", False) else {}),
        }

    @property
    def _bearer(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRelay(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRelay client instance.

        This automatically infers the `api_key` argument from the `RELAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RELAY_API_KEY")
        if api_key is None:
            raise RelayError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RELAY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("RELAY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.relayapi.dev"

        custom_headers_env = os.environ.get("RELAY_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def posts(self) -> AsyncPostsResource:
        from .resources.posts import AsyncPostsResource

        return AsyncPostsResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def media(self) -> AsyncMediaResource:
        from .resources.media import AsyncMediaResource

        return AsyncMediaResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def account_groups(self) -> AsyncAccountGroupsResource:
        from .resources.account_groups import AsyncAccountGroupsResource

        return AsyncAccountGroupsResource(self)

    @cached_property
    def connect(self) -> AsyncConnectResource:
        from .resources.connect import AsyncConnectResource

        return AsyncConnectResource(self)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        from .resources.connections import AsyncConnectionsResource

        return AsyncConnectionsResource(self)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        from .resources.analytics import AsyncAnalyticsResource

        return AsyncAnalyticsResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def queue(self) -> AsyncQueueResource:
        from .resources.queue import AsyncQueueResource

        return AsyncQueueResource(self)

    @cached_property
    def twitter(self) -> AsyncTwitterResource:
        from .resources.twitter import AsyncTwitterResource

        return AsyncTwitterResource(self)

    @cached_property
    def inbox(self) -> AsyncInboxResource:
        from .resources.inbox import AsyncInboxResource

        return AsyncInboxResource(self)

    @cached_property
    def reddit(self) -> AsyncRedditResource:
        from .resources.reddit import AsyncRedditResource

        return AsyncRedditResource(self)

    @cached_property
    def whatsapp(self) -> AsyncWhatsappResource:
        from .resources.whatsapp import AsyncWhatsappResource

        return AsyncWhatsappResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRelayWithRawResponse:
        return AsyncRelayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelayWithStreamedResponse:
        return AsyncRelayWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer if security.get("bearer", False) else {}),
        }

    @property
    def _bearer(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RelayWithRawResponse:
    _client: Relay

    def __init__(self, client: Relay) -> None:
        self._client = client

    @cached_property
    def posts(self) -> posts.PostsResourceWithRawResponse:
        from .resources.posts import PostsResourceWithRawResponse

        return PostsResourceWithRawResponse(self._client.posts)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def media(self) -> media.MediaResourceWithRawResponse:
        from .resources.media import MediaResourceWithRawResponse

        return MediaResourceWithRawResponse(self._client.media)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def account_groups(self) -> account_groups.AccountGroupsResourceWithRawResponse:
        from .resources.account_groups import AccountGroupsResourceWithRawResponse

        return AccountGroupsResourceWithRawResponse(self._client.account_groups)

    @cached_property
    def connect(self) -> connect.ConnectResourceWithRawResponse:
        from .resources.connect import ConnectResourceWithRawResponse

        return ConnectResourceWithRawResponse(self._client.connect)

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithRawResponse:
        from .resources.connections import ConnectionsResourceWithRawResponse

        return ConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithRawResponse:
        from .resources.analytics import AnalyticsResourceWithRawResponse

        return AnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def queue(self) -> queue.QueueResourceWithRawResponse:
        from .resources.queue import QueueResourceWithRawResponse

        return QueueResourceWithRawResponse(self._client.queue)

    @cached_property
    def twitter(self) -> twitter.TwitterResourceWithRawResponse:
        from .resources.twitter import TwitterResourceWithRawResponse

        return TwitterResourceWithRawResponse(self._client.twitter)

    @cached_property
    def inbox(self) -> inbox.InboxResourceWithRawResponse:
        from .resources.inbox import InboxResourceWithRawResponse

        return InboxResourceWithRawResponse(self._client.inbox)

    @cached_property
    def reddit(self) -> reddit.RedditResourceWithRawResponse:
        from .resources.reddit import RedditResourceWithRawResponse

        return RedditResourceWithRawResponse(self._client.reddit)

    @cached_property
    def whatsapp(self) -> whatsapp.WhatsappResourceWithRawResponse:
        from .resources.whatsapp import WhatsappResourceWithRawResponse

        return WhatsappResourceWithRawResponse(self._client.whatsapp)


class AsyncRelayWithRawResponse:
    _client: AsyncRelay

    def __init__(self, client: AsyncRelay) -> None:
        self._client = client

    @cached_property
    def posts(self) -> posts.AsyncPostsResourceWithRawResponse:
        from .resources.posts import AsyncPostsResourceWithRawResponse

        return AsyncPostsResourceWithRawResponse(self._client.posts)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithRawResponse:
        from .resources.media import AsyncMediaResourceWithRawResponse

        return AsyncMediaResourceWithRawResponse(self._client.media)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def account_groups(self) -> account_groups.AsyncAccountGroupsResourceWithRawResponse:
        from .resources.account_groups import AsyncAccountGroupsResourceWithRawResponse

        return AsyncAccountGroupsResourceWithRawResponse(self._client.account_groups)

    @cached_property
    def connect(self) -> connect.AsyncConnectResourceWithRawResponse:
        from .resources.connect import AsyncConnectResourceWithRawResponse

        return AsyncConnectResourceWithRawResponse(self._client.connect)

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithRawResponse:
        from .resources.connections import AsyncConnectionsResourceWithRawResponse

        return AsyncConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithRawResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithRawResponse

        return AsyncAnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def queue(self) -> queue.AsyncQueueResourceWithRawResponse:
        from .resources.queue import AsyncQueueResourceWithRawResponse

        return AsyncQueueResourceWithRawResponse(self._client.queue)

    @cached_property
    def twitter(self) -> twitter.AsyncTwitterResourceWithRawResponse:
        from .resources.twitter import AsyncTwitterResourceWithRawResponse

        return AsyncTwitterResourceWithRawResponse(self._client.twitter)

    @cached_property
    def inbox(self) -> inbox.AsyncInboxResourceWithRawResponse:
        from .resources.inbox import AsyncInboxResourceWithRawResponse

        return AsyncInboxResourceWithRawResponse(self._client.inbox)

    @cached_property
    def reddit(self) -> reddit.AsyncRedditResourceWithRawResponse:
        from .resources.reddit import AsyncRedditResourceWithRawResponse

        return AsyncRedditResourceWithRawResponse(self._client.reddit)

    @cached_property
    def whatsapp(self) -> whatsapp.AsyncWhatsappResourceWithRawResponse:
        from .resources.whatsapp import AsyncWhatsappResourceWithRawResponse

        return AsyncWhatsappResourceWithRawResponse(self._client.whatsapp)


class RelayWithStreamedResponse:
    _client: Relay

    def __init__(self, client: Relay) -> None:
        self._client = client

    @cached_property
    def posts(self) -> posts.PostsResourceWithStreamingResponse:
        from .resources.posts import PostsResourceWithStreamingResponse

        return PostsResourceWithStreamingResponse(self._client.posts)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def media(self) -> media.MediaResourceWithStreamingResponse:
        from .resources.media import MediaResourceWithStreamingResponse

        return MediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def account_groups(self) -> account_groups.AccountGroupsResourceWithStreamingResponse:
        from .resources.account_groups import AccountGroupsResourceWithStreamingResponse

        return AccountGroupsResourceWithStreamingResponse(self._client.account_groups)

    @cached_property
    def connect(self) -> connect.ConnectResourceWithStreamingResponse:
        from .resources.connect import ConnectResourceWithStreamingResponse

        return ConnectResourceWithStreamingResponse(self._client.connect)

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithStreamingResponse:
        from .resources.connections import ConnectionsResourceWithStreamingResponse

        return ConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AnalyticsResourceWithStreamingResponse

        return AnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def queue(self) -> queue.QueueResourceWithStreamingResponse:
        from .resources.queue import QueueResourceWithStreamingResponse

        return QueueResourceWithStreamingResponse(self._client.queue)

    @cached_property
    def twitter(self) -> twitter.TwitterResourceWithStreamingResponse:
        from .resources.twitter import TwitterResourceWithStreamingResponse

        return TwitterResourceWithStreamingResponse(self._client.twitter)

    @cached_property
    def inbox(self) -> inbox.InboxResourceWithStreamingResponse:
        from .resources.inbox import InboxResourceWithStreamingResponse

        return InboxResourceWithStreamingResponse(self._client.inbox)

    @cached_property
    def reddit(self) -> reddit.RedditResourceWithStreamingResponse:
        from .resources.reddit import RedditResourceWithStreamingResponse

        return RedditResourceWithStreamingResponse(self._client.reddit)

    @cached_property
    def whatsapp(self) -> whatsapp.WhatsappResourceWithStreamingResponse:
        from .resources.whatsapp import WhatsappResourceWithStreamingResponse

        return WhatsappResourceWithStreamingResponse(self._client.whatsapp)


class AsyncRelayWithStreamedResponse:
    _client: AsyncRelay

    def __init__(self, client: AsyncRelay) -> None:
        self._client = client

    @cached_property
    def posts(self) -> posts.AsyncPostsResourceWithStreamingResponse:
        from .resources.posts import AsyncPostsResourceWithStreamingResponse

        return AsyncPostsResourceWithStreamingResponse(self._client.posts)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithStreamingResponse:
        from .resources.media import AsyncMediaResourceWithStreamingResponse

        return AsyncMediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def account_groups(self) -> account_groups.AsyncAccountGroupsResourceWithStreamingResponse:
        from .resources.account_groups import AsyncAccountGroupsResourceWithStreamingResponse

        return AsyncAccountGroupsResourceWithStreamingResponse(self._client.account_groups)

    @cached_property
    def connect(self) -> connect.AsyncConnectResourceWithStreamingResponse:
        from .resources.connect import AsyncConnectResourceWithStreamingResponse

        return AsyncConnectResourceWithStreamingResponse(self._client.connect)

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithStreamingResponse:
        from .resources.connections import AsyncConnectionsResourceWithStreamingResponse

        return AsyncConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithStreamingResponse

        return AsyncAnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def queue(self) -> queue.AsyncQueueResourceWithStreamingResponse:
        from .resources.queue import AsyncQueueResourceWithStreamingResponse

        return AsyncQueueResourceWithStreamingResponse(self._client.queue)

    @cached_property
    def twitter(self) -> twitter.AsyncTwitterResourceWithStreamingResponse:
        from .resources.twitter import AsyncTwitterResourceWithStreamingResponse

        return AsyncTwitterResourceWithStreamingResponse(self._client.twitter)

    @cached_property
    def inbox(self) -> inbox.AsyncInboxResourceWithStreamingResponse:
        from .resources.inbox import AsyncInboxResourceWithStreamingResponse

        return AsyncInboxResourceWithStreamingResponse(self._client.inbox)

    @cached_property
    def reddit(self) -> reddit.AsyncRedditResourceWithStreamingResponse:
        from .resources.reddit import AsyncRedditResourceWithStreamingResponse

        return AsyncRedditResourceWithStreamingResponse(self._client.reddit)

    @cached_property
    def whatsapp(self) -> whatsapp.AsyncWhatsappResourceWithStreamingResponse:
        from .resources.whatsapp import AsyncWhatsappResourceWithStreamingResponse

        return AsyncWhatsappResourceWithStreamingResponse(self._client.whatsapp)


Client = Relay

AsyncClient = AsyncRelay
