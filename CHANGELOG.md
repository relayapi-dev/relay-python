# Changelog

## 0.2.0 (2026-07-18)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/relayapi-dev/relay-python/compare/v0.1.0...v0.2.0)

### Features

* **internal/types:** support eagerly validating pydantic iterators ([336e6b8](https://github.com/relayapi-dev/relay-python/commit/336e6b86e0b9e41c97f56647114d016651fe5ed1))
* **stlc:** configurable CI runner and private-production-repo support in workflow templates ([34708d5](https://github.com/relayapi-dev/relay-python/commit/34708d5077aff948d060b71a0e121594bcc4f2fb))
* support setting headers via env ([0ee0af8](https://github.com/relayapi-dev/relay-python/commit/0ee0af8f50b414882bb522197f89ca8b619afde6))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([a8e7622](https://github.com/relayapi-dev/relay-python/commit/a8e76225bf71fc9220c359d722cbe92a41d465c4))
* **client:** preserve hardcoded query params when merging with user params ([9cb4bb2](https://github.com/relayapi-dev/relay-python/commit/9cb4bb294a028e5140429b451e6f140f60c87295))
* ensure file data are only sent as 1 parameter ([f34cae1](https://github.com/relayapi-dev/relay-python/commit/f34cae18bc35e5d810f193a72103545641ee9d79))
* use correct field name format for multipart file arrays ([8303c53](https://github.com/relayapi-dev/relay-python/commit/8303c53dcc138a67390f811857db84c1232d2dc2))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([4110cd5](https://github.com/relayapi-dev/relay-python/commit/4110cd50cbf45c0ae1127ed5fb67d6a74dfa9835))


### Chores

* **internal:** codegen related update ([81ede60](https://github.com/relayapi-dev/relay-python/commit/81ede606381a25d7226cb1996fe0dc199f845d9e))
* **internal:** more robust bootstrap script ([2f37ee9](https://github.com/relayapi-dev/relay-python/commit/2f37ee9252f6da2a4cf0add59fadc534c1dcc26b))
* **internal:** reformat pyproject.toml ([6320153](https://github.com/relayapi-dev/relay-python/commit/632015308a62755b6fef5ad41c08759c30a73ed9))

## 0.1.0 (2026-03-31)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/relayapi-dev/relay-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([452a6b4](https://github.com/relayapi-dev/relay-python/commit/452a6b4e0d2fce5b575436332b9ece62ef6fae0b))
* **internal:** implement indices array format for query and form serialization ([6cabe1d](https://github.com/relayapi-dev/relay-python/commit/6cabe1dfa5f17f4bd5485d1db52d1b5f87a48b44))


### Chores

* **ci:** skip lint on metadata-only changes ([749b71c](https://github.com/relayapi-dev/relay-python/commit/749b71c9517bbf2736d3cf9e921d1e7e225e5248))
* **internal:** update gitignore ([21e1930](https://github.com/relayapi-dev/relay-python/commit/21e193069ba5f9b1314cf11ee1c72b21166b2400))
