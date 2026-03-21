# Posts

Types:

```python
from relay.types import (
    PostCreateResponse,
    PostRetrieveResponse,
    PostUpdateResponse,
    PostListResponse,
    PostBulkCreateResponse,
    PostRetryResponse,
    PostUnpublishResponse,
)
```

Methods:

- <code title="post /v1/posts">client.posts.<a href="./src/relay/resources/posts/posts.py">create</a>(\*\*<a href="src/relay/types/post_create_params.py">params</a>) -> <a href="./src/relay/types/post_create_response.py">PostCreateResponse</a></code>
- <code title="get /v1/posts/{id}">client.posts.<a href="./src/relay/resources/posts/posts.py">retrieve</a>(id) -> <a href="./src/relay/types/post_retrieve_response.py">PostRetrieveResponse</a></code>
- <code title="patch /v1/posts/{id}">client.posts.<a href="./src/relay/resources/posts/posts.py">update</a>(id, \*\*<a href="src/relay/types/post_update_params.py">params</a>) -> <a href="./src/relay/types/post_update_response.py">PostUpdateResponse</a></code>
- <code title="get /v1/posts">client.posts.<a href="./src/relay/resources/posts/posts.py">list</a>(\*\*<a href="src/relay/types/post_list_params.py">params</a>) -> <a href="./src/relay/types/post_list_response.py">PostListResponse</a></code>
- <code title="delete /v1/posts/{id}">client.posts.<a href="./src/relay/resources/posts/posts.py">delete</a>(id) -> None</code>
- <code title="post /v1/posts/bulk">client.posts.<a href="./src/relay/resources/posts/posts.py">bulk_create</a>(\*\*<a href="src/relay/types/post_bulk_create_params.py">params</a>) -> <a href="./src/relay/types/post_bulk_create_response.py">PostBulkCreateResponse</a></code>
- <code title="post /v1/posts/{id}/retry">client.posts.<a href="./src/relay/resources/posts/posts.py">retry</a>(id) -> <a href="./src/relay/types/post_retry_response.py">PostRetryResponse</a></code>
- <code title="post /v1/posts/{id}/unpublish">client.posts.<a href="./src/relay/resources/posts/posts.py">unpublish</a>(id) -> <a href="./src/relay/types/post_unpublish_response.py">PostUnpublishResponse</a></code>

## Logs

Types:

```python
from relay.types.posts import LogRetrieveResponse, LogListResponse
```

Methods:

- <code title="get /v1/posts/{id}/logs">client.posts.logs.<a href="./src/relay/resources/posts/logs.py">retrieve</a>(id) -> <a href="./src/relay/types/posts/log_retrieve_response.py">LogRetrieveResponse</a></code>
- <code title="get /v1/posts/logs">client.posts.logs.<a href="./src/relay/resources/posts/logs.py">list</a>(\*\*<a href="src/relay/types/posts/log_list_params.py">params</a>) -> <a href="./src/relay/types/posts/log_list_response.py">LogListResponse</a></code>

# Accounts

Types:

```python
from relay.types import AccountRetrieveResponse, AccountUpdateResponse, AccountListResponse
```

Methods:

- <code title="get /v1/accounts/{id}">client.accounts.<a href="./src/relay/resources/accounts/accounts.py">retrieve</a>(id) -> <a href="./src/relay/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="patch /v1/accounts/{id}">client.accounts.<a href="./src/relay/resources/accounts/accounts.py">update</a>(id, \*\*<a href="src/relay/types/account_update_params.py">params</a>) -> <a href="./src/relay/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="get /v1/accounts">client.accounts.<a href="./src/relay/resources/accounts/accounts.py">list</a>(\*\*<a href="src/relay/types/account_list_params.py">params</a>) -> <a href="./src/relay/types/account_list_response.py">AccountListResponse</a></code>
- <code title="delete /v1/accounts/{id}">client.accounts.<a href="./src/relay/resources/accounts/accounts.py">delete</a>(id) -> None</code>

## Health

Types:

```python
from relay.types.accounts import HealthRetrieveResponse, HealthListResponse
```

Methods:

- <code title="get /v1/accounts/{id}/health">client.accounts.health.<a href="./src/relay/resources/accounts/health.py">retrieve</a>(id) -> <a href="./src/relay/types/accounts/health_retrieve_response.py">HealthRetrieveResponse</a></code>
- <code title="get /v1/accounts/health">client.accounts.health.<a href="./src/relay/resources/accounts/health.py">list</a>() -> <a href="./src/relay/types/accounts/health_list_response.py">HealthListResponse</a></code>

## RedditFlairs

Types:

```python
from relay.types.accounts import RedditFlairRetrieveResponse
```

Methods:

- <code title="get /v1/accounts/{id}/reddit-flairs">client.accounts.reddit_flairs.<a href="./src/relay/resources/accounts/reddit_flairs.py">retrieve</a>(id, \*\*<a href="src/relay/types/accounts/reddit_flair_retrieve_params.py">params</a>) -> <a href="./src/relay/types/accounts/reddit_flair_retrieve_response.py">RedditFlairRetrieveResponse</a></code>

## FacebookPages

Types:

```python
from relay.types.accounts import FacebookPageRetrieveResponse, FacebookPageSetDefaultResponse
```

Methods:

- <code title="get /v1/accounts/{id}/facebook-pages">client.accounts.facebook_pages.<a href="./src/relay/resources/accounts/facebook_pages.py">retrieve</a>(id) -> <a href="./src/relay/types/accounts/facebook_page_retrieve_response.py">FacebookPageRetrieveResponse</a></code>
- <code title="put /v1/accounts/{id}/facebook-pages">client.accounts.facebook_pages.<a href="./src/relay/resources/accounts/facebook_pages.py">set_default</a>(id, \*\*<a href="src/relay/types/accounts/facebook_page_set_default_params.py">params</a>) -> <a href="./src/relay/types/accounts/facebook_page_set_default_response.py">FacebookPageSetDefaultResponse</a></code>

## LinkedinOrganizations

Types:

```python
from relay.types.accounts import (
    LinkedinOrganizationRetrieveResponse,
    LinkedinOrganizationSwitchTypeResponse,
)
```

Methods:

- <code title="get /v1/accounts/{id}/linkedin-organizations">client.accounts.linkedin_organizations.<a href="./src/relay/resources/accounts/linkedin_organizations.py">retrieve</a>(id) -> <a href="./src/relay/types/accounts/linkedin_organization_retrieve_response.py">LinkedinOrganizationRetrieveResponse</a></code>
- <code title="put /v1/accounts/{id}/linkedin-organizations">client.accounts.linkedin_organizations.<a href="./src/relay/resources/accounts/linkedin_organizations.py">switch_type</a>(id, \*\*<a href="src/relay/types/accounts/linkedin_organization_switch_type_params.py">params</a>) -> <a href="./src/relay/types/accounts/linkedin_organization_switch_type_response.py">LinkedinOrganizationSwitchTypeResponse</a></code>

## PinterestBoards

Types:

```python
from relay.types.accounts import PinterestBoardRetrieveResponse, PinterestBoardSetDefaultResponse
```

Methods:

- <code title="get /v1/accounts/{id}/pinterest-boards">client.accounts.pinterest_boards.<a href="./src/relay/resources/accounts/pinterest_boards.py">retrieve</a>(id) -> <a href="./src/relay/types/accounts/pinterest_board_retrieve_response.py">PinterestBoardRetrieveResponse</a></code>
- <code title="put /v1/accounts/{id}/pinterest-boards">client.accounts.pinterest_boards.<a href="./src/relay/resources/accounts/pinterest_boards.py">set_default</a>(id, \*\*<a href="src/relay/types/accounts/pinterest_board_set_default_params.py">params</a>) -> <a href="./src/relay/types/accounts/pinterest_board_set_default_response.py">PinterestBoardSetDefaultResponse</a></code>

## RedditSubreddits

Types:

```python
from relay.types.accounts import RedditSubredditRetrieveResponse, RedditSubredditSetDefaultResponse
```

Methods:

- <code title="get /v1/accounts/{id}/reddit-subreddits">client.accounts.reddit_subreddits.<a href="./src/relay/resources/accounts/reddit_subreddits.py">retrieve</a>(id) -> <a href="./src/relay/types/accounts/reddit_subreddit_retrieve_response.py">RedditSubredditRetrieveResponse</a></code>
- <code title="put /v1/accounts/{id}/reddit-subreddits">client.accounts.reddit_subreddits.<a href="./src/relay/resources/accounts/reddit_subreddits.py">set_default</a>(id, \*\*<a href="src/relay/types/accounts/reddit_subreddit_set_default_params.py">params</a>) -> <a href="./src/relay/types/accounts/reddit_subreddit_set_default_response.py">RedditSubredditSetDefaultResponse</a></code>

## GmbLocations

Types:

```python
from relay.types.accounts import GmbLocationRetrieveResponse, GmbLocationSetDefaultResponse
```

Methods:

- <code title="get /v1/accounts/{id}/gmb-locations">client.accounts.gmb_locations.<a href="./src/relay/resources/accounts/gmb_locations.py">retrieve</a>(id) -> <a href="./src/relay/types/accounts/gmb_location_retrieve_response.py">GmbLocationRetrieveResponse</a></code>
- <code title="put /v1/accounts/{id}/gmb-locations">client.accounts.gmb_locations.<a href="./src/relay/resources/accounts/gmb_locations.py">set_default</a>(id, \*\*<a href="src/relay/types/accounts/gmb_location_set_default_params.py">params</a>) -> <a href="./src/relay/types/accounts/gmb_location_set_default_response.py">GmbLocationSetDefaultResponse</a></code>

# Media

Types:

```python
from relay.types import MediaRetrieveResponse, MediaGetPresignURLResponse, MediaUploadResponse
```

Methods:

- <code title="get /v1/media/{id}">client.media.<a href="./src/relay/resources/media.py">retrieve</a>(id) -> <a href="./src/relay/types/media_retrieve_response.py">MediaRetrieveResponse</a></code>
- <code title="delete /v1/media/{id}">client.media.<a href="./src/relay/resources/media.py">delete</a>(id) -> None</code>
- <code title="post /v1/media/presign">client.media.<a href="./src/relay/resources/media.py">get_presign_url</a>(\*\*<a href="src/relay/types/media_get_presign_url_params.py">params</a>) -> <a href="./src/relay/types/media_get_presign_url_response.py">MediaGetPresignURLResponse</a></code>
- <code title="post /v1/media/upload">client.media.<a href="./src/relay/resources/media.py">upload</a>(body, \*\*<a href="src/relay/types/media_upload_params.py">params</a>) -> <a href="./src/relay/types/media_upload_response.py">MediaUploadResponse</a></code>

# Webhooks

Types:

```python
from relay.types import (
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookListLogsResponse,
    WebhookSendTestResponse,
)
```

Methods:

- <code title="post /v1/webhooks">client.webhooks.<a href="./src/relay/resources/webhooks.py">create</a>(\*\*<a href="src/relay/types/webhook_create_params.py">params</a>) -> <a href="./src/relay/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="patch /v1/webhooks/{id}">client.webhooks.<a href="./src/relay/resources/webhooks.py">update</a>(id, \*\*<a href="src/relay/types/webhook_update_params.py">params</a>) -> <a href="./src/relay/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /v1/webhooks">client.webhooks.<a href="./src/relay/resources/webhooks.py">list</a>(\*\*<a href="src/relay/types/webhook_list_params.py">params</a>) -> <a href="./src/relay/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v1/webhooks/{id}">client.webhooks.<a href="./src/relay/resources/webhooks.py">delete</a>(id) -> None</code>
- <code title="get /v1/webhooks/logs">client.webhooks.<a href="./src/relay/resources/webhooks.py">list_logs</a>(\*\*<a href="src/relay/types/webhook_list_logs_params.py">params</a>) -> <a href="./src/relay/types/webhook_list_logs_response.py">WebhookListLogsResponse</a></code>
- <code title="post /v1/webhooks/test">client.webhooks.<a href="./src/relay/resources/webhooks.py">send_test</a>(\*\*<a href="src/relay/types/webhook_send_test_params.py">params</a>) -> <a href="./src/relay/types/webhook_send_test_response.py">WebhookSendTestResponse</a></code>

# APIKeys

Types:

```python
from relay.types import APIKeyCreateResponse, APIKeyListResponse
```

Methods:

- <code title="post /v1/api-keys">client.api_keys.<a href="./src/relay/resources/api_keys.py">create</a>(\*\*<a href="src/relay/types/api_key_create_params.py">params</a>) -> <a href="./src/relay/types/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /v1/api-keys">client.api_keys.<a href="./src/relay/resources/api_keys.py">list</a>(\*\*<a href="src/relay/types/api_key_list_params.py">params</a>) -> <a href="./src/relay/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v1/api-keys/{id}">client.api_keys.<a href="./src/relay/resources/api_keys.py">delete</a>(id) -> None</code>

# Usage

Types:

```python
from relay.types import UsageRetrieveResponse
```

Methods:

- <code title="get /v1/usage">client.usage.<a href="./src/relay/resources/usage.py">retrieve</a>() -> <a href="./src/relay/types/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

# AccountGroups

Types:

```python
from relay.types import (
    AccountGroupCreateResponse,
    AccountGroupUpdateResponse,
    AccountGroupListResponse,
)
```

Methods:

- <code title="post /v1/account-groups">client.account_groups.<a href="./src/relay/resources/account_groups.py">create</a>(\*\*<a href="src/relay/types/account_group_create_params.py">params</a>) -> <a href="./src/relay/types/account_group_create_response.py">AccountGroupCreateResponse</a></code>
- <code title="put /v1/account-groups/{id}">client.account_groups.<a href="./src/relay/resources/account_groups.py">update</a>(id, \*\*<a href="src/relay/types/account_group_update_params.py">params</a>) -> <a href="./src/relay/types/account_group_update_response.py">AccountGroupUpdateResponse</a></code>
- <code title="get /v1/account-groups">client.account_groups.<a href="./src/relay/resources/account_groups.py">list</a>() -> <a href="./src/relay/types/account_group_list_response.py">AccountGroupListResponse</a></code>
- <code title="delete /v1/account-groups/{id}">client.account_groups.<a href="./src/relay/resources/account_groups.py">delete</a>(id) -> None</code>

# Connect

Types:

```python
from relay.types import (
    ConnectCompleteOAuthCallbackResponse,
    ConnectCreateBlueskyConnectionResponse,
    ConnectFetchPendingDataResponse,
    ConnectStartOAuthFlowResponse,
)
```

Methods:

- <code title="post /v1/connect/{platform}">client.connect.<a href="./src/relay/resources/connect/connect.py">complete_oauth_callback</a>(platform, \*\*<a href="src/relay/types/connect_complete_oauth_callback_params.py">params</a>) -> <a href="./src/relay/types/connect_complete_oauth_callback_response.py">ConnectCompleteOAuthCallbackResponse</a></code>
- <code title="post /v1/connect/bluesky">client.connect.<a href="./src/relay/resources/connect/connect.py">create_bluesky_connection</a>(\*\*<a href="src/relay/types/connect_create_bluesky_connection_params.py">params</a>) -> <a href="./src/relay/types/connect_create_bluesky_connection_response.py">ConnectCreateBlueskyConnectionResponse</a></code>
- <code title="get /v1/connect/pending-data">client.connect.<a href="./src/relay/resources/connect/connect.py">fetch_pending_data</a>(\*\*<a href="src/relay/types/connect_fetch_pending_data_params.py">params</a>) -> <a href="./src/relay/types/connect_fetch_pending_data_response.py">ConnectFetchPendingDataResponse</a></code>
- <code title="get /v1/connect/{platform}">client.connect.<a href="./src/relay/resources/connect/connect.py">start_oauth_flow</a>(platform, \*\*<a href="src/relay/types/connect_start_oauth_flow_params.py">params</a>) -> <a href="./src/relay/types/connect_start_oauth_flow_response.py">ConnectStartOAuthFlowResponse</a></code>

## Telegram

Types:

```python
from relay.types.connect import (
    TelegramConnectDirectlyResponse,
    TelegramInitiateConnectionResponse,
    TelegramPollConnectionStatusResponse,
)
```

Methods:

- <code title="post /v1/connect/telegram/direct">client.connect.telegram.<a href="./src/relay/resources/connect/telegram.py">connect_directly</a>(\*\*<a href="src/relay/types/connect/telegram_connect_directly_params.py">params</a>) -> <a href="./src/relay/types/connect/telegram_connect_directly_response.py">TelegramConnectDirectlyResponse</a></code>
- <code title="post /v1/connect/telegram">client.connect.telegram.<a href="./src/relay/resources/connect/telegram.py">initiate_connection</a>() -> <a href="./src/relay/types/connect/telegram_initiate_connection_response.py">TelegramInitiateConnectionResponse</a></code>
- <code title="get /v1/connect/telegram">client.connect.telegram.<a href="./src/relay/resources/connect/telegram.py">poll_connection_status</a>(\*\*<a href="src/relay/types/connect/telegram_poll_connection_status_params.py">params</a>) -> <a href="./src/relay/types/connect/telegram_poll_connection_status_response.py">TelegramPollConnectionStatusResponse</a></code>

## Whatsapp

Types:

```python
from relay.types.connect import (
    WhatsappCompleteEmbeddedSignupResponse,
    WhatsappConnectViaCredentialsResponse,
    WhatsappGetSDKConfigResponse,
)
```

Methods:

- <code title="post /v1/connect/whatsapp/embedded-signup">client.connect.whatsapp.<a href="./src/relay/resources/connect/whatsapp.py">complete_embedded_signup</a>(\*\*<a href="src/relay/types/connect/whatsapp_complete_embedded_signup_params.py">params</a>) -> <a href="./src/relay/types/connect/whatsapp_complete_embedded_signup_response.py">WhatsappCompleteEmbeddedSignupResponse</a></code>
- <code title="post /v1/connect/whatsapp/credentials">client.connect.whatsapp.<a href="./src/relay/resources/connect/whatsapp.py">connect_via_credentials</a>(\*\*<a href="src/relay/types/connect/whatsapp_connect_via_credentials_params.py">params</a>) -> <a href="./src/relay/types/connect/whatsapp_connect_via_credentials_response.py">WhatsappConnectViaCredentialsResponse</a></code>
- <code title="get /v1/connect/whatsapp/sdk-config">client.connect.whatsapp.<a href="./src/relay/resources/connect/whatsapp.py">get_sdk_config</a>() -> <a href="./src/relay/types/connect/whatsapp_get_sdk_config_response.py">WhatsappGetSDKConfigResponse</a></code>

## Facebook

### Pages

Types:

```python
from relay.types.connect.facebook import PageListResponse, PageSelectResponse
```

Methods:

- <code title="get /v1/connect/facebook/pages">client.connect.facebook.pages.<a href="./src/relay/resources/connect/facebook/pages.py">list</a>() -> <a href="./src/relay/types/connect/facebook/page_list_response.py">PageListResponse</a></code>
- <code title="post /v1/connect/facebook/pages">client.connect.facebook.pages.<a href="./src/relay/resources/connect/facebook/pages.py">select</a>(\*\*<a href="src/relay/types/connect/facebook/page_select_params.py">params</a>) -> <a href="./src/relay/types/connect/facebook/page_select_response.py">PageSelectResponse</a></code>

## Linkedin

### Organizations

Types:

```python
from relay.types.connect.linkedin import OrganizationListResponse, OrganizationSelectResponse
```

Methods:

- <code title="get /v1/connect/linkedin/organizations">client.connect.linkedin.organizations.<a href="./src/relay/resources/connect/linkedin/organizations.py">list</a>() -> <a href="./src/relay/types/connect/linkedin/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="post /v1/connect/linkedin/organizations">client.connect.linkedin.organizations.<a href="./src/relay/resources/connect/linkedin/organizations.py">select</a>(\*\*<a href="src/relay/types/connect/linkedin/organization_select_params.py">params</a>) -> <a href="./src/relay/types/connect/linkedin/organization_select_response.py">OrganizationSelectResponse</a></code>

## Pinterest

### Boards

Types:

```python
from relay.types.connect.pinterest import BoardListResponse, BoardSelectResponse
```

Methods:

- <code title="get /v1/connect/pinterest/boards">client.connect.pinterest.boards.<a href="./src/relay/resources/connect/pinterest/boards.py">list</a>() -> <a href="./src/relay/types/connect/pinterest/board_list_response.py">BoardListResponse</a></code>
- <code title="post /v1/connect/pinterest/boards">client.connect.pinterest.boards.<a href="./src/relay/resources/connect/pinterest/boards.py">select</a>(\*\*<a href="src/relay/types/connect/pinterest/board_select_params.py">params</a>) -> <a href="./src/relay/types/connect/pinterest/board_select_response.py">BoardSelectResponse</a></code>

## Googlebusiness

### Locations

Types:

```python
from relay.types.connect.googlebusiness import LocationListResponse, LocationSelectResponse
```

Methods:

- <code title="get /v1/connect/googlebusiness/locations">client.connect.googlebusiness.locations.<a href="./src/relay/resources/connect/googlebusiness/locations.py">list</a>() -> <a href="./src/relay/types/connect/googlebusiness/location_list_response.py">LocationListResponse</a></code>
- <code title="post /v1/connect/googlebusiness/locations">client.connect.googlebusiness.locations.<a href="./src/relay/resources/connect/googlebusiness/locations.py">select</a>(\*\*<a href="src/relay/types/connect/googlebusiness/location_select_params.py">params</a>) -> <a href="./src/relay/types/connect/googlebusiness/location_select_response.py">LocationSelectResponse</a></code>

## Snapchat

### Profiles

Types:

```python
from relay.types.connect.snapchat import ProfileListResponse, ProfileSelectResponse
```

Methods:

- <code title="get /v1/connect/snapchat/profiles">client.connect.snapchat.profiles.<a href="./src/relay/resources/connect/snapchat/profiles.py">list</a>() -> <a href="./src/relay/types/connect/snapchat/profile_list_response.py">ProfileListResponse</a></code>
- <code title="post /v1/connect/snapchat/profiles">client.connect.snapchat.profiles.<a href="./src/relay/resources/connect/snapchat/profiles.py">select</a>(\*\*<a href="src/relay/types/connect/snapchat/profile_select_params.py">params</a>) -> <a href="./src/relay/types/connect/snapchat/profile_select_response.py">ProfileSelectResponse</a></code>

# Connections

Types:

```python
from relay.types import ConnectionListLogsResponse
```

Methods:

- <code title="get /v1/connections/logs">client.connections.<a href="./src/relay/resources/connections.py">list_logs</a>(\*\*<a href="src/relay/types/connection_list_logs_params.py">params</a>) -> <a href="./src/relay/types/connection_list_logs_response.py">ConnectionListLogsResponse</a></code>

# Analytics

Types:

```python
from relay.types import (
    AnalyticsRetrieveResponse,
    AnalyticsGetBestTimeResponse,
    AnalyticsGetContentDecayResponse,
    AnalyticsGetPostTimelineResponse,
    AnalyticsGetPostingFrequencyResponse,
    AnalyticsListDailyMetricsResponse,
)
```

Methods:

- <code title="get /v1/analytics">client.analytics.<a href="./src/relay/resources/analytics/analytics.py">retrieve</a>(\*\*<a href="src/relay/types/analytics_retrieve_params.py">params</a>) -> <a href="./src/relay/types/analytics_retrieve_response.py">AnalyticsRetrieveResponse</a></code>
- <code title="get /v1/analytics/best-time">client.analytics.<a href="./src/relay/resources/analytics/analytics.py">get_best_time</a>(\*\*<a href="src/relay/types/analytics_get_best_time_params.py">params</a>) -> <a href="./src/relay/types/analytics_get_best_time_response.py">AnalyticsGetBestTimeResponse</a></code>
- <code title="get /v1/analytics/content-decay">client.analytics.<a href="./src/relay/resources/analytics/analytics.py">get_content_decay</a>(\*\*<a href="src/relay/types/analytics_get_content_decay_params.py">params</a>) -> <a href="./src/relay/types/analytics_get_content_decay_response.py">AnalyticsGetContentDecayResponse</a></code>
- <code title="get /v1/analytics/post-timeline">client.analytics.<a href="./src/relay/resources/analytics/analytics.py">get_post_timeline</a>(\*\*<a href="src/relay/types/analytics_get_post_timeline_params.py">params</a>) -> <a href="./src/relay/types/analytics_get_post_timeline_response.py">AnalyticsGetPostTimelineResponse</a></code>
- <code title="get /v1/analytics/posting-frequency">client.analytics.<a href="./src/relay/resources/analytics/analytics.py">get_posting_frequency</a>(\*\*<a href="src/relay/types/analytics_get_posting_frequency_params.py">params</a>) -> <a href="./src/relay/types/analytics_get_posting_frequency_response.py">AnalyticsGetPostingFrequencyResponse</a></code>
- <code title="get /v1/analytics/daily-metrics">client.analytics.<a href="./src/relay/resources/analytics/analytics.py">list_daily_metrics</a>(\*\*<a href="src/relay/types/analytics_list_daily_metrics_params.py">params</a>) -> <a href="./src/relay/types/analytics_list_daily_metrics_response.py">AnalyticsListDailyMetricsResponse</a></code>

## Youtube

Types:

```python
from relay.types.analytics import YoutubeGetDailyViewsResponse
```

Methods:

- <code title="get /v1/analytics/youtube/daily-views">client.analytics.youtube.<a href="./src/relay/resources/analytics/youtube.py">get_daily_views</a>(\*\*<a href="src/relay/types/analytics/youtube_get_daily_views_params.py">params</a>) -> <a href="./src/relay/types/analytics/youtube_get_daily_views_response.py">YoutubeGetDailyViewsResponse</a></code>

# Tools

## Validate

Types:

```python
from relay.types.tools import (
    ValidateCheckPostLengthResponse,
    ValidateRetrieveSubredditResponse,
    ValidateValidateMediaResponse,
    ValidateValidatePostResponse,
)
```

Methods:

- <code title="post /v1/tools/validate/post-length">client.tools.validate.<a href="./src/relay/resources/tools/validate.py">check_post_length</a>(\*\*<a href="src/relay/types/tools/validate_check_post_length_params.py">params</a>) -> <a href="./src/relay/types/tools/validate_check_post_length_response.py">ValidateCheckPostLengthResponse</a></code>
- <code title="get /v1/tools/validate/subreddit">client.tools.validate.<a href="./src/relay/resources/tools/validate.py">retrieve_subreddit</a>(\*\*<a href="src/relay/types/tools/validate_retrieve_subreddit_params.py">params</a>) -> <a href="./src/relay/types/tools/validate_retrieve_subreddit_response.py">ValidateRetrieveSubredditResponse</a></code>
- <code title="post /v1/tools/validate/media">client.tools.validate.<a href="./src/relay/resources/tools/validate.py">validate_media</a>(\*\*<a href="src/relay/types/tools/validate_validate_media_params.py">params</a>) -> <a href="./src/relay/types/tools/validate_validate_media_response.py">ValidateValidateMediaResponse</a></code>
- <code title="post /v1/tools/validate/post">client.tools.validate.<a href="./src/relay/resources/tools/validate.py">validate_post</a>(\*\*<a href="src/relay/types/tools/validate_validate_post_params.py">params</a>) -> <a href="./src/relay/types/tools/validate_validate_post_response.py">ValidateValidatePostResponse</a></code>

## Instagram

Types:

```python
from relay.types.tools import InstagramCheckHashtagSafetyResponse
```

Methods:

- <code title="post /v1/tools/instagram/hashtag-checker">client.tools.instagram.<a href="./src/relay/resources/tools/instagram.py">check_hashtag_safety</a>(\*\*<a href="src/relay/types/tools/instagram_check_hashtag_safety_params.py">params</a>) -> <a href="./src/relay/types/tools/instagram_check_hashtag_safety_response.py">InstagramCheckHashtagSafetyResponse</a></code>

# Queue

Types:

```python
from relay.types import QueueGetNextSlotResponse, QueuePreviewResponse
```

Methods:

- <code title="get /v1/queue/next-slot">client.queue.<a href="./src/relay/resources/queue/queue.py">get_next_slot</a>() -> <a href="./src/relay/types/queue_get_next_slot_response.py">QueueGetNextSlotResponse</a></code>
- <code title="get /v1/queue/preview">client.queue.<a href="./src/relay/resources/queue/queue.py">preview</a>(\*\*<a href="src/relay/types/queue_preview_params.py">params</a>) -> <a href="./src/relay/types/queue_preview_response.py">QueuePreviewResponse</a></code>

## Slots

Types:

```python
from relay.types.queue import SlotCreateResponse, SlotUpdateResponse, SlotListResponse
```

Methods:

- <code title="post /v1/queue/slots">client.queue.slots.<a href="./src/relay/resources/queue/slots.py">create</a>(\*\*<a href="src/relay/types/queue/slot_create_params.py">params</a>) -> <a href="./src/relay/types/queue/slot_create_response.py">SlotCreateResponse</a></code>
- <code title="put /v1/queue/slots">client.queue.slots.<a href="./src/relay/resources/queue/slots.py">update</a>(\*\*<a href="src/relay/types/queue/slot_update_params.py">params</a>) -> <a href="./src/relay/types/queue/slot_update_response.py">SlotUpdateResponse</a></code>
- <code title="get /v1/queue/slots">client.queue.slots.<a href="./src/relay/resources/queue/slots.py">list</a>() -> <a href="./src/relay/types/queue/slot_list_response.py">SlotListResponse</a></code>
- <code title="delete /v1/queue/slots">client.queue.slots.<a href="./src/relay/resources/queue/slots.py">delete</a>() -> None</code>

# Twitter

## Retweet

Types:

```python
from relay.types.twitter import RetweetCreateResponse, RetweetUndoResponse
```

Methods:

- <code title="post /v1/twitter/retweet">client.twitter.retweet.<a href="./src/relay/resources/twitter/retweet.py">create</a>(\*\*<a href="src/relay/types/twitter/retweet_create_params.py">params</a>) -> <a href="./src/relay/types/twitter/retweet_create_response.py">RetweetCreateResponse</a></code>
- <code title="delete /v1/twitter/retweet">client.twitter.retweet.<a href="./src/relay/resources/twitter/retweet.py">undo</a>(\*\*<a href="src/relay/types/twitter/retweet_undo_params.py">params</a>) -> <a href="./src/relay/types/twitter/retweet_undo_response.py">RetweetUndoResponse</a></code>

## Bookmark

Types:

```python
from relay.types.twitter import BookmarkCreateResponse, BookmarkRemoveResponse
```

Methods:

- <code title="post /v1/twitter/bookmark">client.twitter.bookmark.<a href="./src/relay/resources/twitter/bookmark.py">create</a>(\*\*<a href="src/relay/types/twitter/bookmark_create_params.py">params</a>) -> <a href="./src/relay/types/twitter/bookmark_create_response.py">BookmarkCreateResponse</a></code>
- <code title="delete /v1/twitter/bookmark">client.twitter.bookmark.<a href="./src/relay/resources/twitter/bookmark.py">remove</a>(\*\*<a href="src/relay/types/twitter/bookmark_remove_params.py">params</a>) -> <a href="./src/relay/types/twitter/bookmark_remove_response.py">BookmarkRemoveResponse</a></code>

## Follow

Types:

```python
from relay.types.twitter import FollowCreateResponse, FollowUnfollowResponse
```

Methods:

- <code title="post /v1/twitter/follow">client.twitter.follow.<a href="./src/relay/resources/twitter/follow.py">create</a>(\*\*<a href="src/relay/types/twitter/follow_create_params.py">params</a>) -> <a href="./src/relay/types/twitter/follow_create_response.py">FollowCreateResponse</a></code>
- <code title="delete /v1/twitter/follow">client.twitter.follow.<a href="./src/relay/resources/twitter/follow.py">unfollow</a>(\*\*<a href="src/relay/types/twitter/follow_unfollow_params.py">params</a>) -> <a href="./src/relay/types/twitter/follow_unfollow_response.py">FollowUnfollowResponse</a></code>

# Inbox

## Comments

Types:

```python
from relay.types.inbox import (
    CommentRetrieveResponse,
    CommentListResponse,
    CommentDeleteResponse,
    CommentPrivateReplyResponse,
    CommentReplyResponse,
)
```

Methods:

- <code title="get /v1/inbox/comments/{post_id}">client.inbox.comments.<a href="./src/relay/resources/inbox/comments/comments.py">retrieve</a>(post_id, \*\*<a href="src/relay/types/inbox/comment_retrieve_params.py">params</a>) -> <a href="./src/relay/types/inbox/comment_retrieve_response.py">CommentRetrieveResponse</a></code>
- <code title="get /v1/inbox/comments">client.inbox.comments.<a href="./src/relay/resources/inbox/comments/comments.py">list</a>(\*\*<a href="src/relay/types/inbox/comment_list_params.py">params</a>) -> <a href="./src/relay/types/inbox/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /v1/inbox/comments/{comment_id}">client.inbox.comments.<a href="./src/relay/resources/inbox/comments/comments.py">delete</a>(comment_id) -> <a href="./src/relay/types/inbox/comment_delete_response.py">CommentDeleteResponse</a></code>
- <code title="post /v1/inbox/comments/{comment_id}/private-reply">client.inbox.comments.<a href="./src/relay/resources/inbox/comments/comments.py">private_reply</a>(comment_id, \*\*<a href="src/relay/types/inbox/comment_private_reply_params.py">params</a>) -> <a href="./src/relay/types/inbox/comment_private_reply_response.py">CommentPrivateReplyResponse</a></code>
- <code title="post /v1/inbox/comments/{post_id}/reply">client.inbox.comments.<a href="./src/relay/resources/inbox/comments/comments.py">reply</a>(post_id, \*\*<a href="src/relay/types/inbox/comment_reply_params.py">params</a>) -> <a href="./src/relay/types/inbox/comment_reply_response.py">CommentReplyResponse</a></code>

### Hide

Types:

```python
from relay.types.inbox.comments import HideCreateResponse, HideDeleteResponse
```

Methods:

- <code title="post /v1/inbox/comments/{comment_id}/hide">client.inbox.comments.hide.<a href="./src/relay/resources/inbox/comments/hide.py">create</a>(comment_id) -> <a href="./src/relay/types/inbox/comments/hide_create_response.py">HideCreateResponse</a></code>
- <code title="delete /v1/inbox/comments/{comment_id}/hide">client.inbox.comments.hide.<a href="./src/relay/resources/inbox/comments/hide.py">delete</a>(comment_id) -> <a href="./src/relay/types/inbox/comments/hide_delete_response.py">HideDeleteResponse</a></code>

### Like

Types:

```python
from relay.types.inbox.comments import LikeCreateResponse, LikeDeleteResponse
```

Methods:

- <code title="post /v1/inbox/comments/{comment_id}/like">client.inbox.comments.like.<a href="./src/relay/resources/inbox/comments/like.py">create</a>(comment_id) -> <a href="./src/relay/types/inbox/comments/like_create_response.py">LikeCreateResponse</a></code>
- <code title="delete /v1/inbox/comments/{comment_id}/like">client.inbox.comments.like.<a href="./src/relay/resources/inbox/comments/like.py">delete</a>(comment_id) -> <a href="./src/relay/types/inbox/comments/like_delete_response.py">LikeDeleteResponse</a></code>

## Messages

Types:

```python
from relay.types.inbox import (
    MessageRetrieveResponse,
    MessageListResponse,
    MessageArchiveResponse,
    MessageEditResponse,
    MessageSendResponse,
)
```

Methods:

- <code title="get /v1/inbox/messages/{conversation_id}">client.inbox.messages.<a href="./src/relay/resources/inbox/messages.py">retrieve</a>(conversation_id) -> <a href="./src/relay/types/inbox/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /v1/inbox/messages">client.inbox.messages.<a href="./src/relay/resources/inbox/messages.py">list</a>(\*\*<a href="src/relay/types/inbox/message_list_params.py">params</a>) -> <a href="./src/relay/types/inbox/message_list_response.py">MessageListResponse</a></code>
- <code title="put /v1/inbox/messages/{conversation_id}/archive">client.inbox.messages.<a href="./src/relay/resources/inbox/messages.py">archive</a>(conversation_id) -> <a href="./src/relay/types/inbox/message_archive_response.py">MessageArchiveResponse</a></code>
- <code title="patch /v1/inbox/messages/{conversation_id}/{message_id}">client.inbox.messages.<a href="./src/relay/resources/inbox/messages.py">edit</a>(message_id, \*, conversation_id, \*\*<a href="src/relay/types/inbox/message_edit_params.py">params</a>) -> <a href="./src/relay/types/inbox/message_edit_response.py">MessageEditResponse</a></code>
- <code title="post /v1/inbox/messages/{conversation_id}">client.inbox.messages.<a href="./src/relay/resources/inbox/messages.py">send</a>(conversation_id, \*\*<a href="src/relay/types/inbox/message_send_params.py">params</a>) -> <a href="./src/relay/types/inbox/message_send_response.py">MessageSendResponse</a></code>

## Reviews

Types:

```python
from relay.types.inbox import ReviewListResponse
```

Methods:

- <code title="get /v1/inbox/reviews">client.inbox.reviews.<a href="./src/relay/resources/inbox/reviews/reviews.py">list</a>(\*\*<a href="src/relay/types/inbox/review_list_params.py">params</a>) -> <a href="./src/relay/types/inbox/review_list_response.py">ReviewListResponse</a></code>

### Reply

Types:

```python
from relay.types.inbox.reviews import ReplyCreateResponse, ReplyDeleteResponse
```

Methods:

- <code title="post /v1/inbox/reviews/{review_id}/reply">client.inbox.reviews.reply.<a href="./src/relay/resources/inbox/reviews/reply.py">create</a>(review_id, \*\*<a href="src/relay/types/inbox/reviews/reply_create_params.py">params</a>) -> <a href="./src/relay/types/inbox/reviews/reply_create_response.py">ReplyCreateResponse</a></code>
- <code title="delete /v1/inbox/reviews/{review_id}/reply">client.inbox.reviews.reply.<a href="./src/relay/resources/inbox/reviews/reply.py">delete</a>(review_id) -> <a href="./src/relay/types/inbox/reviews/reply_delete_response.py">ReplyDeleteResponse</a></code>

# Reddit

Types:

```python
from relay.types import RedditGetFeedResponse, RedditSearchResponse
```

Methods:

- <code title="get /v1/reddit/feed">client.reddit.<a href="./src/relay/resources/reddit.py">get_feed</a>(\*\*<a href="src/relay/types/reddit_get_feed_params.py">params</a>) -> <a href="./src/relay/types/reddit_get_feed_response.py">RedditGetFeedResponse</a></code>
- <code title="get /v1/reddit/search">client.reddit.<a href="./src/relay/resources/reddit.py">search</a>(\*\*<a href="src/relay/types/reddit_search_params.py">params</a>) -> <a href="./src/relay/types/reddit_search_response.py">RedditSearchResponse</a></code>

# Whatsapp

Types:

```python
from relay.types import WhatsappBulkSendResponse, WhatsappListPhoneNumbersResponse
```

Methods:

- <code title="post /v1/whatsapp/bulk-send">client.whatsapp.<a href="./src/relay/resources/whatsapp/whatsapp.py">bulk_send</a>(\*\*<a href="src/relay/types/whatsapp_bulk_send_params.py">params</a>) -> <a href="./src/relay/types/whatsapp_bulk_send_response.py">WhatsappBulkSendResponse</a></code>
- <code title="get /v1/whatsapp/phone-numbers">client.whatsapp.<a href="./src/relay/resources/whatsapp/whatsapp.py">list_phone_numbers</a>(\*\*<a href="src/relay/types/whatsapp_list_phone_numbers_params.py">params</a>) -> <a href="./src/relay/types/whatsapp_list_phone_numbers_response.py">WhatsappListPhoneNumbersResponse</a></code>

## Broadcasts

Types:

```python
from relay.types.whatsapp import (
    BroadcastCreateResponse,
    BroadcastRetrieveResponse,
    BroadcastListResponse,
    BroadcastScheduleResponse,
    BroadcastSendResponse,
)
```

Methods:

- <code title="post /v1/whatsapp/broadcasts">client.whatsapp.broadcasts.<a href="./src/relay/resources/whatsapp/broadcasts.py">create</a>(\*\*<a href="src/relay/types/whatsapp/broadcast_create_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/broadcast_create_response.py">BroadcastCreateResponse</a></code>
- <code title="get /v1/whatsapp/broadcasts/{broadcast_id}">client.whatsapp.broadcasts.<a href="./src/relay/resources/whatsapp/broadcasts.py">retrieve</a>(broadcast_id) -> <a href="./src/relay/types/whatsapp/broadcast_retrieve_response.py">BroadcastRetrieveResponse</a></code>
- <code title="get /v1/whatsapp/broadcasts">client.whatsapp.broadcasts.<a href="./src/relay/resources/whatsapp/broadcasts.py">list</a>(\*\*<a href="src/relay/types/whatsapp/broadcast_list_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/broadcast_list_response.py">BroadcastListResponse</a></code>
- <code title="delete /v1/whatsapp/broadcasts/{broadcast_id}">client.whatsapp.broadcasts.<a href="./src/relay/resources/whatsapp/broadcasts.py">delete</a>(broadcast_id) -> None</code>
- <code title="post /v1/whatsapp/broadcasts/{broadcast_id}/schedule">client.whatsapp.broadcasts.<a href="./src/relay/resources/whatsapp/broadcasts.py">schedule</a>(broadcast_id) -> <a href="./src/relay/types/whatsapp/broadcast_schedule_response.py">BroadcastScheduleResponse</a></code>
- <code title="post /v1/whatsapp/broadcasts/{broadcast_id}/send">client.whatsapp.broadcasts.<a href="./src/relay/resources/whatsapp/broadcasts.py">send</a>(broadcast_id) -> <a href="./src/relay/types/whatsapp/broadcast_send_response.py">BroadcastSendResponse</a></code>

## Templates

Types:

```python
from relay.types.whatsapp import (
    TemplateCreateResponse,
    TemplateRetrieveResponse,
    TemplateListResponse,
)
```

Methods:

- <code title="post /v1/whatsapp/templates">client.whatsapp.templates.<a href="./src/relay/resources/whatsapp/templates.py">create</a>(\*\*<a href="src/relay/types/whatsapp/template_create_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /v1/whatsapp/templates/{template_name}">client.whatsapp.templates.<a href="./src/relay/resources/whatsapp/templates.py">retrieve</a>(template_name, \*\*<a href="src/relay/types/whatsapp/template_retrieve_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="get /v1/whatsapp/templates">client.whatsapp.templates.<a href="./src/relay/resources/whatsapp/templates.py">list</a>(\*\*<a href="src/relay/types/whatsapp/template_list_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /v1/whatsapp/templates/{template_name}">client.whatsapp.templates.<a href="./src/relay/resources/whatsapp/templates.py">delete</a>(template_name, \*\*<a href="src/relay/types/whatsapp/template_delete_params.py">params</a>) -> None</code>

## Contacts

Types:

```python
from relay.types.whatsapp import (
    ContactCreateResponse,
    ContactRetrieveResponse,
    ContactListResponse,
    ContactBulkOperationsResponse,
    ContactImportResponse,
)
```

Methods:

- <code title="post /v1/whatsapp/contacts">client.whatsapp.contacts.<a href="./src/relay/resources/whatsapp/contacts.py">create</a>(\*\*<a href="src/relay/types/whatsapp/contact_create_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="get /v1/whatsapp/contacts/{contact_id}">client.whatsapp.contacts.<a href="./src/relay/resources/whatsapp/contacts.py">retrieve</a>(contact_id) -> <a href="./src/relay/types/whatsapp/contact_retrieve_response.py">ContactRetrieveResponse</a></code>
- <code title="get /v1/whatsapp/contacts">client.whatsapp.contacts.<a href="./src/relay/resources/whatsapp/contacts.py">list</a>(\*\*<a href="src/relay/types/whatsapp/contact_list_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /v1/whatsapp/contacts/{contact_id}">client.whatsapp.contacts.<a href="./src/relay/resources/whatsapp/contacts.py">delete</a>(contact_id) -> None</code>
- <code title="post /v1/whatsapp/contacts/bulk">client.whatsapp.contacts.<a href="./src/relay/resources/whatsapp/contacts.py">bulk_operations</a>(\*\*<a href="src/relay/types/whatsapp/contact_bulk_operations_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/contact_bulk_operations_response.py">ContactBulkOperationsResponse</a></code>
- <code title="post /v1/whatsapp/contacts/import">client.whatsapp.contacts.<a href="./src/relay/resources/whatsapp/contacts.py">import\_</a>(\*\*<a href="src/relay/types/whatsapp/contact_import_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/contact_import_response.py">ContactImportResponse</a></code>

## Groups

Types:

```python
from relay.types.whatsapp import GroupCreateResponse, GroupListResponse
```

Methods:

- <code title="post /v1/whatsapp/groups">client.whatsapp.groups.<a href="./src/relay/resources/whatsapp/groups.py">create</a>(\*\*<a href="src/relay/types/whatsapp/group_create_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/group_create_response.py">GroupCreateResponse</a></code>
- <code title="get /v1/whatsapp/groups">client.whatsapp.groups.<a href="./src/relay/resources/whatsapp/groups.py">list</a>(\*\*<a href="src/relay/types/whatsapp/group_list_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /v1/whatsapp/groups/{group_id}">client.whatsapp.groups.<a href="./src/relay/resources/whatsapp/groups.py">delete</a>(group_id) -> None</code>

## BusinessProfile

Types:

```python
from relay.types.whatsapp import BusinessProfileRetrieveResponse, BusinessProfileUpdateResponse
```

Methods:

- <code title="get /v1/whatsapp/business-profile">client.whatsapp.business_profile.<a href="./src/relay/resources/whatsapp/business_profile.py">retrieve</a>(\*\*<a href="src/relay/types/whatsapp/business_profile_retrieve_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/business_profile_retrieve_response.py">BusinessProfileRetrieveResponse</a></code>
- <code title="put /v1/whatsapp/business-profile">client.whatsapp.business_profile.<a href="./src/relay/resources/whatsapp/business_profile.py">update</a>(\*\*<a href="src/relay/types/whatsapp/business_profile_update_params.py">params</a>) -> <a href="./src/relay/types/whatsapp/business_profile_update_response.py">BusinessProfileUpdateResponse</a></code>
