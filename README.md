# MCP Server for EC2 Instances
## Description
A simple MCP server for interacting with AWS EC2 instances using FastMCP and boto3.

## Available MCP Tools
- list_instances — List EC2 instances in a region
- start_instance — Start an EC2 instance
- stop_instance — Stop an EC2 instance
- get_cpu_utilization — Fetch CPU metrics via CloudWatch

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
> AWS credentials must be configured via environment variables or a local AWS profile.
- Rename `.env.example` to `.env`
- Fill in the required variables

### Run MCP server
```bash
uv run python -m app.main
```
OR, for MCP inspector applications using an explicit absolute path:
```bash
uv run --directory /Absolute/path/to/ec2-mcp/ python -m app.main
```
