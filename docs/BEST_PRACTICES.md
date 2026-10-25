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
