# Changelog

All notable changes to this project will be documented in this section.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased][]

## [1.0.0][] - 2024-06-15

### Added

- Added {class}`bedrock.exceptions.CommandRequestError` which replaces
  `bedrock.response.CommandResponseError`.
- Added {class}`bedrock.context.GameContext.data` property.


### Changed

- Significant performance improvement by providing `wait=False` to
  {meth}`bedrock.server.Server.send` and {meth}`bedrock.server.Server.run`.
- The response of a command request cannot be an exception anymore. Instead
  an exception may be raised by calling
  {meth}`bedrock.response.CommandResponse.raise_for_status`.
- {meth}`bedrock.response.CommandResponse.ok` is now a property.
- Improvement of documentation.


## [1.0.0a0.post1][] - 2023-05-20

### Added

- Typing is now supported.


## [1.0.0a0][] - 2023-05-20

### Added

- Initial release
- Prerelease

[Unreleased]: https://github.com/bedrock-ws/bedrockpy/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/bedrock-ws/bedrockpy/compare/v1.0.0a0.pos1...v1.0.0
[1.0.0a0.post1]: https://github.com/bedrock-ws/bedrockpy/compare/v1.0.0a0...v1.0.0a0.post1
[1.0.0a0]: https://github.com/bedrock-ws/bedrockpy/releases/v1.0.0a0
