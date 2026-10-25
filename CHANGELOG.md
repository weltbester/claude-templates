# Changelog

## Unreleased
### Added
- `claude/settings.example.json`: reference copy of personal settings,
  without account-synced plugin entries.

### Changed
- Restructured repo: `claude/` mirrors `~/.claude`; project templates,
  docs, prompts and eval examples moved into their own folders.
- Domain-specific commands moved to `project-templates/commands-examples/`.

### Removed
- `02_CODE_ANALYSIS.md` (byte-identical duplicate of `CODE_ANALYSIS.md`).
- Tracked-free `.claude/settings.local.json` (machine-local).
