The TARGETED Framework for Command Design

Use this acronym to create effective commands:

T-ask-Specific Instructions
A-rguments and Placeholders
R-eusable Process Steps
G-uided Examples and References
E-xplicit Output Requirements
T-emplate-Based Naming
E-rror Handling and Edge Cases
D-ocumentation and Context

Core Principles

1. Right Context at the Right Time

Commands solve the "400-page manual" problem by providing only the relevant context needed for a specific task, avoiding information overload.

2. Reusable Consistency

Commands ensure the same high-quality process is followed every time a task is performed, scaling your best practices across your AI labor.

3. Template-Driven Automation

Use placeholders and templates to make commands flexible while maintaining structure and naming conventions.

Command Structure and Location

Commands are stored as markdown files in .claude/commands/ directory:

Project-specific: .claude/commands/ (versioned with your project)
Global commands: ~/.claude/commands/ (available across all projects)
Command Management Tips

Organization Strategies

By Function: plan-feature.md, impl-api.md, test-unit.md, deploy-prod.md, ...
By Domain: auth-login.md, user-profile.md, payment-process.md, order-create.md, ...
By Role: dev-review.md, qa-automation.md, ops-deploy.md, pm-requirements.md, ...
Version Control

Store project commands in .claude/commands/ for team sharing
Use descriptive commit messages when updating commands
Review command changes as part of code review process
Command Evolution

Regularly review and update commands based on team feedback
Archive outdated commands rather than deleting them
Document command changes in project changelog
Commands transform Claude Code from a general assistant into a specialized team member with deep knowledge of your specific workflows. They ensure consistent, high-quality execution of repetitive tasks while providing the targeted context needed for complex operations.


Examples of Commands

File: .claude/commands/code-review.md
File: .claude/commands/api-test
