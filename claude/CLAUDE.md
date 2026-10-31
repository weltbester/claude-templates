# Global CLAUDE.md

## Code
- Follow SOLID principles
- Type hints / annotations on every parameter
- Max line length 80 characters
- No magic numbers, global mutable state, or nesting deeper than 3-4 levels
- Follow STYLE.md if the project has one
- Don't add dependencies without justification; pin versions and note why
  a specific version is required

## Testing
- Write unit tests for core functionality and integration tests for key
  workflows, including error cases
- Run all tests before marking a task complete and before committing

## Documentation
- Keep README.md current when functionality changes
- Maintain CHANGELOG.md with every change

## Version Control
- Fetch / pull before you push
- Create a new branch with a meaningful name for each new feature
- Conventional commits: `type(scope): description`
  (feat, fix, docs, style, refactor, test, chore); atomic commits
- Never commit secrets or credentials

## Versioning and Tagging
- When a version number in code changes, add an annotated tag in the same
  commit, matching the code version (`__version__ = '1.0.1'` →
  `git tag -a v1.0.1 -m "Release notes"`)

## Autonomy
- Implement straightforward tasks autonomously
- Ask before architectural changes, breaking changes, or deleting
  significant code
- Don't implement features that weren't explicitly requested

## Debugging
- These rules override autonomy and "fix issues immediately" while debugging
- If very sure of the fix, say so and explain why
- If unsure, rank possible causes by probability
- Let the user choose which one to tackle
- Read-only investigation is fine; make no changes yet
- Start fixing only once the solution path is clear
- First give a brief plan overview, information only
- Then do exactly one troubleshooting step at a time
- Wait for the user to finish each step before the next
- Confirm the fix with the user at the end
- Why: one step at a time beats scrolling back through a list of several steps
