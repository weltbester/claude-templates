# Code documentation command

# Write a documentation for a feature named $ARGUMENT:

1. Developer Documentation - Technical specs, API details, implementation notes
2. User Documentation - Simple guide with screenshots placeholders, step-by-step instructions

## Command Structure

- Accept a feature name as input
- Analyze the relevant code files
- Generate two separate documentation files in appropriate directories
- Follow your project's existing documentation patterns
- Include placeholders for screenshots in user docs
- Add proper cross-references between the two doc types

## Example Usage

Should generate:

Implicit Example:
- docs/dev/<feature name>-implementation.md
- docs/dev/how-to-<feature name>.md

Explicit Example (feature: 'reset-password'):
- docs/dev/password-reset-implementation.md
- docs/user/how-to-reset-password.md

## Bonus Points

- Make the command detect if the feature is frontend/backend/full-stack and adjust documentation accordingly
- Make it automatically capture and insert screenshots in user-facing documentation
- Auto-link to related existing documentation
