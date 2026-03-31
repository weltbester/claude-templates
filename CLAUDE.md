# Global CLAUDE.md - Project Guidelines for AI Assistance

This file provides guidelines for AI assistants (particularly Claude and Claude Code) working on this project. It ensures consistency, quality, and professionalism across all AI-assisted development work.

## Project Standards

### Code Quality
- **Follow SOLID design principles in all code:**
  - **S**ingle Responsibility - Each class/module has one reason to change
  - **O**pen/Closed - Open for extension, closed for modification
  - **L**iskov Substitution - Subtypes must be substitutable for their base types
  - **I**nterface Segregation - Prefer specific interfaces over general-purpose ones
  - **D**ependency Inversion - Depend on abstractions, not concrete implementations
- Write clean, readable, and maintainable code
- Use type hints / annotations for every parameter
- Follow language-specific style guides and idioms
- Add meaningful comments for complex logic only
- Prefer self-documenting code with clear variable and function names
- Implement comprehensive error handling with descriptive messages
- Validate all inputs and handle edge cases gracefully

### Testing Requirements
- Write unit tests for all core functionality
- Include integration tests for key workflows
- Test error conditions and edge cases
- Ensure tests are deterministic and reproducible
- Run all tests before marking tasks complete
- Aim for high code coverage on critical paths

### Documentation Standards
- Keep README.md current with project state
- Document all public APIs and interfaces
- Include usage examples in documentation
- Maintain CHANGELOG.md with version history
- Document non-obvious design decisions
- Add inline documentation for complex algorithms

### Version Control
- Fetch / Pull before you Push
- Always create a new branch with a meaningful name when you implement a new feature
- Write clear, descriptive commit messages
- Use conventional commit format: `type(scope): description`
  - Types: feat, fix, docs, style, refactor, test, chore
- Create logical, atomic commits
- Never commit sensitive data or credentials
- Update .gitignore appropriately

### Versioning and Tagging
- Always add a git tag when changing version numbers in code
- Tag version must match the version in the code (e.g., `__version__ = '1.0.1'` → `git tag v1.0.1`)
- Create annotated tags with meaningful release notes: `git tag -a v1.0.1 -m "Release notes"`
- Add the tag in the same commit that changes the version number

## Automated Tasks

### Before Starting Implementation
- [ ] Review existing code structure and patterns
- [ ] Check for similar existing functionality to avoid duplication
- [ ] Identify dependencies and their licenses
- [ ] Plan module/file organization
- [ ] Consider backward compatibility

### During Implementation
- [ ] Follow existing project conventions and patterns
- [ ] Write self-documenting code
- [ ] Add error handling as you code, not as an afterthought
- [ ] Create tests alongside implementation
- [ ] Update relevant documentation immediately
- [ ] Use consistent naming conventions

### After Implementation
- [ ] Run all tests and fix failures
- [ ] Verify code builds/compiles without warnings
- [ ] Check for unused imports and dead code
- [ ] Review error messages for clarity and usefulness
- [ ] Update README if functionality changed
- [ ] Update CHANGELOG with changes
- [ ] Verify all files are properly formatted

### Code Review Checklist
- [ ] No hardcoded values (use configuration)
- [ ] No exposed secrets or credentials
- [ ] Proper resource cleanup (files, connections, etc.)
- [ ] Thread-safety considered where applicable
- [ ] Performance implications evaluated
- [ ] Security implications considered
- [ ] Accessibility requirements met (for user-facing features)

## Security Practices

### General Security
- Never commit secrets, API keys, or credentials
- Use environment variables for configuration
- Validate and sanitize all external input
- Use parameterized queries for databases
- Keep dependencies updated
- Follow principle of least privilege

### Dependency Management
- Regularly check for security vulnerabilities
- Pin dependency versions for reproducibility
- Document why specific versions are required
- Review dependency licenses for compatibility
- Minimize dependency tree depth

## Performance Considerations

- Profile before optimizing
- Document performance-critical sections
- Consider memory usage for large data operations
- Implement appropriate caching strategies
- Use lazy loading where beneficial
- Avoid premature optimization

## Error Handling Philosophy

- Fail fast with clear error messages
- Provide actionable error messages to users
- Log errors with sufficient context for debugging
- Use appropriate error types/classes
- Handle errors at the appropriate level
- Never silently swallow errors

## Licensing and Legal

### Code Attribution
- Respect existing license (see LICENSE file)
- Include copyright notices where required
- Attribute third-party code properly
- Document license of all dependencies
- Ensure license compatibility

### Generated Content
- All AI-generated code is reviewed for quality
- Code snippets from training data are rewritten
- No copyrighted material is reproduced verbatim
- Licensing requirements are clearly documented

## Communication Guidelines

### When Working with Developers
- Ask clarifying questions before major decisions
- Explain trade-offs when multiple approaches exist
- Highlight potential issues or risks proactively
- Suggest improvements when appropriate
- Be honest about limitations or uncertainties

### Progress Updates
- Summarize what was accomplished
- Note any blockers or issues encountered
- Highlight decisions made and rationale
- List what remains to be done
- Keep updates concise and actionable

## Project-Specific Preferences

### Code Style
- Follow the style guide in STYLE.md (if present)
- Use project's existing formatter configuration
- Match indentation and bracket style of existing code
- Follow naming conventions used in the project

### Testing Framework
- Use the testing framework already in the project
- Follow existing test organization patterns
- Match assertion style used in existing tests
- Follow existing mock/fixture patterns

### Build and Deployment
- Follow existing build scripts and procedures
- Document any new build requirements
- Update CI/CD configuration if needed
- Test build process after changes

## Continuous Improvement

- Suggest better approaches when identified
- Refactor opportunistically when touching code
- Update documentation when understanding improves
- Share learnings that might help the project
- Question patterns that seem problematic

## AI Assistant Behavior

### Autonomy Level
- Implement straightforward tasks autonomously
- Ask before making architectural changes
- Confirm before deleting significant code
- Discuss trade-offs for non-obvious decisions
- Request clarification for ambiguous requirements

### Iteration Strategy
- Start with working MVP, then refine
- Test incrementally, not all at once
- Make atomic changes that can be verified
- Fix issues as soon as they're detected
- Commit logical units of work

## Exclusions and Restrictions

### Do Not
- Implement features not explicitly requested
- Make breaking changes without discussion
- Use deprecated APIs or libraries
- Introduce unnecessary complexity
- Deviate significantly from established patterns
- Add dependencies without justification

### Always Avoid
- Code lines longer than 80 characters
- Magic numbers and unexplained constants
- God objects or classes
- Deep nesting (>3-4 levels)
- Functions longer than one screen
- Circular dependencies
- Global mutable state

## Success Criteria

A task is complete when:
- All code compiles/runs without errors
- All tests pass
- Documentation is updated
- Code follows project conventions
- No obvious bugs or issues remain
- Changes are committed with clear messages
- Checklist items are addressed

## Notes for AI Assistants

This file is designed to make you more effective and the project more professional. When in doubt:
1. Ask the developer
2. Follow existing patterns
3. Prefer simple over clever
4. Document your reasoning
5. Test thoroughly

Remember: You're collaborating with humans to build quality software. Be helpful, be professional, and be thorough.
