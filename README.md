# claude-templates

Templates and workflows for Claude Code. The `claude/` folder mirrors
`~/.claude`; everything else is reference material or per-project templates.

## Layout

| Path                 | Purpose                                              |
|----------------------|------------------------------------------------------|
| `claude/`            | Global config, mirrors `~/.claude` (copy or symlink) |
| `claude/CLAUDE.md`   | Global guidelines loaded in every session            |
| `claude/settings.json` | Generic permissions example (no model/plugin data) |
| `claude/commands/`   | Generic slash commands usable in any project         |
| `claude/skills/`     | Skills and a guide for writing descriptions          |
| `claude/agents/`     | Subagent definitions (empty for now)                 |
| `claude/output-styles/` | Output styles, e.g. `minimal-bullets`             |
| `project-templates/` | Per-project `CLAUDE_*.md`, STYLE, PLANNING, etc.     |
| `project-templates/commands-examples/` | Domain-specific command examples   |
| `docs/`              | Best practices, hooks, worktree and workflow guides  |
| `prompts/`           | Analysis prompts and general prompt templates        |
| `examples/evals/`    | Example Python evaluation scripts                    |

## Usage

Global setup (review existing files in `~/.claude` first, do not overwrite
blindly):

```sh
cp -R claude/commands claude/skills claude/agents claude/output-styles ~/.claude/
cp -n claude/CLAUDE.md claude/settings.json ~/.claude/
```

Per project: copy the matching `project-templates/CLAUDE_*.md` to the
project root as `CLAUDE.md`, and any wanted command from
`project-templates/commands-examples/` to `<project>/.claude/commands/`.

Note: four example commands (`deploy-prod`, `impl-api`, `plan-feature`,
`test-unit`) are empty placeholders.
