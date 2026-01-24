# Security Best Practices

1. Validate and sanitize inputs - Never trust input data blindly
2. Always quote shell variables - Use "$VAR" not $VAR
3. Block path traversal - Check for .. in file paths
4. Use absolute path - Specify full paths for scripts
5. Skip sensitive files - Avoid .env, .git/, .keys, etc.
