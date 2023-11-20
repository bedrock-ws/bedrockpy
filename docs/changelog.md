# Changelog

All notable changes to this project will be documented in this section.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added

- Added {class}`bedrock.exceptions.CommandRequestError` which replaces
  `bedrock.response.CommandResponseError`


### Changed

- The response of a command request cannot be an exception anymore. Instead
     an exception may be raised by calling
    {meth}`bedrock.response.CommandResponse.raise_for_status`.
- {meth}`bedrock.response.CommandResponse.ok` is now a property.
- Improvement of documentation.


## [1.0.0a0.post1] - 2023-05-20

### Added

- Typing is now supported.


## [1.0.0a0] - 2023-05-20

### Added

- Initial release
- Prerelease

[unreleased]: https://github.com/bedrock-ws/bedrockpy/compare/v1.0.0a0.post1...HEAD
[1.0.0a0.post1]: https://github.com/bedrock-ws/bedrockpy/compare/v1.0.0a0...v1.0.0a0.post1
[1.0.0a0]: https://github.com/bedrock-ws/bedrockpy/releases/v1.0.0a0
