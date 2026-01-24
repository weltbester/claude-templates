# CLI Project Development Workflow with Claude Tools

## Phase 1: Planning (Claude Web/App)

### 1. Initial Requirements Discussion
- Describe your CLI tool's purpose and target users
- Define core functionality and stretch goals
- Discuss input/output formats, error handling philosophy

### 2. Design the Interface
- Plan command structure and subcommands
- Define flags and arguments (useful for clap configuration in Rust)
- Sketch expected user workflows
- Consider configuration file needs

### 3. Architecture Planning
- Break down into modules/components
- Identify external dependencies
- Plan data structures and flow
- Discuss error handling strategy

### 4. Create Implementation Roadmap
- Prioritize features (MVP first)
- Identify technical risks
- Plan testing approach

## Phase 2: Setup (Claude Code)

### 5. Project Initialization
- Ask Claude Code to create project structure
- Initialize version control
- Set up basic Cargo.toml (for Rust) or requirements.txt (for Python)
- Create README with planned features

### 6. Scaffold Core Structure
- Create main entry point
- Set up argument parsing (e.g., clap for Rust)
- Implement basic logging/error types
- Create placeholder modules for main features

## Phase 3: Iterative Development (Claude Code)

### 7. Feature-by-Feature Implementation
- Implement one complete feature at a time
- Test each feature as you go
- Let Claude Code run the program to verify functionality
- Keep features isolated in separate modules

### 8. Incremental Refinement
- Ask Claude Code to refactor as complexity grows
- Add error handling and validation
- Improve user feedback and messages
- Add progress indicators for long operations

## Phase 4: Testing & Polish (Both Tools)

### 9. Testing (Claude Code)
- Write unit tests for core logic
- Create integration tests for CLI workflows
- Test edge cases and error conditions
- Run and fix issues iteratively

### 10. Documentation Review (Claude Web)
- Review generated code documentation
- Improve README with examples
- Add inline comments for complex logic
- Create usage documentation

## Phase 5: Release Preparation (Both Tools)

### 11. Final Polish (Claude Code)
- Performance optimization if needed
- Final bug fixes
- Build release binaries
- Test installation process

### 12. Documentation & Licensing (Claude)
- Finalize LICENSE file
- Complete CHANGELOG
- Review dependencies' licenses
- Create contribution guidelines if open-sourcing

# Best Practices for CLI Development with Claude Tools

## Do's

- Start with a clear specification before coding
- Use Claude (web) for "what should I do?" and Claude Code for "do this"
- Implement MVP first, then iterate
- Keep Claude Code sessions focused on specific features
- Commit frequently to version control
- Let Claude Code run your tests—it can fix issues autonomously

## Don'ts

- Don't jump into coding without a plan
- Don't try to implement everything at once
- Don't use Claude (web) for actual file operations—it can't modify your filesystem
- Don't skip error handling in your initial implementation

## Tool-Specific Tips

### Claude Code Strengths

- Autonomous iteration: "implement X, test it, and fix any issues"
- Multi-file operations: creates, edits, and organizes project files
- Direct execution: runs your code and responds to actual errors
- Filesystem awareness: understands your project structure

### Claude (Web) Strengths

- Strategic thinking and architecture advice
- Explaining concepts and trade-offs
- Reviewing complex design decisions
- Learning support for new technologies (like your Rust journey)
