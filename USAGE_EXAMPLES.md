# Usage Examples for MCP GitHub Server

## Interactive Mode Examples

### Example 1: List All Repositories
```
> list my repositories

Executing: list_repositories
Parameters: {
  "type": "all",
  "sort": "updated",
  "limit": 50
}

REPOSITORIES (Total: 23)
1. weltbester/calendar-app 🌐 Public
   ⭐ 0 stars | 🍴 0 forks | 💻 JavaScript
   ...
```

### Example 2: List Only Public Repositories
```
> list public repositories

Executing: list_repositories
Parameters: {
  "type": "public",
  "sort": "updated",
  "limit": 50
}
```

### Example 3: List First 5 Repositories Sorted by Name
```
> list 5 repositories sorted by name

Executing: list_repositories
Parameters: {
  "type": "all",
  "sort": "full_name",
  "limit": 5
}
```

### Example 4: Get Repository Details
```
> get info about weltbester/calendar-app

Executing: get_repository
Parameters: {
  "full_name": "weltbester/calendar-app"
}

REPOSITORY: weltbester/calendar-app
Visibility: 🌐 Public
Statistics:
  ⭐ Stars: 0
  👀 Watchers: 0
  🍴 Forks: 0
  ...
```

### Example 5: Get Help
```
> help

Available commands:
  - 'list my repositories' - List all your repos
  - 'list public repositories' - List only public repos
  - 'list 10 repositories' - List first 10 repos
  - 'get info about owner/repo' - Get details about specific repo
  - 'exit' or 'quit' - Exit the CLI
```

### Example 6: Exit
```
> exit
Goodbye!
```

## Command-Line Mode (Single Queries)

Run one query and exit:

```bash
# List all repositories
python main.py "list my repositories"

# List private repositories only
python main.py "list private repositories"

# List 10 newest repositories
python main.py "list 10 repositories"

# Get specific repository info
python main.py "get info about weltbester/ai-educational-website"

# List repos sorted by creation date
python main.py "list repositories sorted by created"
```

## Direct Client Usage (Programmatic)

If you want to use the MCP client directly in your own Python scripts:

```python
import asyncio
from mcp_client import MCPClient
import os

async def main():
    # Path to server
    server_path = "mcp_server.py"

    # Use the client
    async with MCPClient(server_path) as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[t['name'] for t in tools]}")

        # Call list_repositories
        repos = await client.call_tool("list_repositories", {
            "type": "public",
            "sort": "updated",
            "limit": 10
        })
        print(f"Found {repos['total_count']} repositories")

        # Call get_repository
        repo_info = await client.call_tool("get_repository", {
            "full_name": "weltbester/calendar-app"
        })
        print(f"Stars: {repo_info['stars']}")

if __name__ == "__main__":
    asyncio.run(main())
```

## MCP Inspector Usage

Test your server visually with the MCP Inspector:

```bash
# Set token
source .env

# Start inspector
npx @modelcontextprotocol/inspector python mcp_server.py
```

Then open http://localhost:6274 in your browser.

**In the Inspector:**
1. Click "Connect" to connect to the server
2. Click on "Tools" tab to see available tools
3. Click "list_repositories" and try:
   - Set "type": "public"
   - Set "sort": "created"
   - Set "limit": 10
   - Click "Execute"
4. Click "get_repository" and try:
   - Set "full_name": "weltbester/calendar-app"
   - Click "Execute"

## Testing Different Scenarios

### Scenario 1: Find Your Most Recent Projects
```
> list 5 repositories sorted by updated
```

### Scenario 2: List Only Private Repos
```
> list private repositories
```

### Scenario 3: Explore a Specific Project
```
> get info about weltbester/rust-programming-masterclass
```

### Scenario 4: List All Projects Alphabetically
```
> list repositories sorted by name
```

## Understanding the Natural Language Parser

The CLI recognizes these patterns:

**For listing repositories:**
- Trigger words: "list", "show", "my"
- Type filters: "private", "public", "owner"
- Sort options: "created", "newest", "name", "alphabetical", "pushed", "recent"
- Limit: "5 repositories", "10 repos", "first 20"

**For getting repository info:**
- Trigger words: "get", "show", "info", "about", "details"
- Repository format: Must include "owner/repo" (e.g., "weltbester/calendar-app")

## Error Handling Examples

### Invalid Repository Name
```
> get info about weltbester/nonexistent-repo-12345

ERROR
Type: GitHub API Error
Message: 404 Not Found
```

### Missing Repository Name
```
> get info about myrepo

Error: Could not find repository name in format 'owner/repo'.
Example: 'get info about octocat/Hello-World'
```

### Unclear Request
```
> show me something

Error: Could not understand your request.
Try:
  - 'list my repositories'
  - 'list public repositories sorted by name'
  - 'get info about owner/repo'
  - 'help' for more examples
```

## Advanced Usage: Running Tests

```bash
# Run all integration tests
source venv/bin/activate
source .env
pytest tests/ -v

# Run specific test
pytest tests/test_integration.py::test_list_repositories_tool -v

# Run with detailed output
pytest tests/ -v -s
```

## Tips & Tricks

1. **Quick access**: Create an alias in your `~/.zshrc` or `~/.bashrc`:
   ```bash
   alias github-mcp='cd /path/to/my_mcp && source venv/bin/activate && source .env && python main.py'
   ```

2. **Check token expiry**: GitHub PATs can expire. If you get auth errors, check your token at https://github.com/settings/tokens

3. **Rate limits**: GitHub API has rate limits. If you get 403 errors, you may have exceeded limits. Check with:
   ```python
   python main.py "list my repositories"  # Check stderr for rate limit info
   ```

4. **Debugging**: Check server logs in stderr output for detailed error information

5. **Multiple queries**: In interactive mode, you can run as many queries as you want without restarting
