## Instructions
### Clone repository
```bash
git clone https://github.com/daswata/mcp-ec2.git
cd mcp-ec2
```

### Install dependencies
```bash
pip install uv
uv install
```

### Setup .env
- rename .env.example into .env
- fill the necessary variables

### Run MCP server
```bash
uv run python -m app.main
```
for more precise command
```bash
uv run --directory /Absolute/path/to/ec2-mcp/ python -m app.main
```