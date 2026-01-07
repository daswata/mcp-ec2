from mcp.server.fastmcp import FastMCP
from app.tools.ec2 import list_instances, start_instance_tool, stop_instance_tool
from app.tools.cloudwatch import get_cpu_utilization_tool

mcp = FastMCP("simple-mcp-server")

@mcp.tool()
def get_instances() -> dict:
    """
    Get a list of all EC2 instances.

    Returns:
        dict: A dictionary containing the count and details of each EC2 instances.
    """
    return list_instances()

@mcp.tool()
def start_instance(instance_id: str) -> dict:
    """
    Start an EC2 instance.

    Args:
        instance_id (str): The ID of the EC2 instance to start.

    Returns:
        List: A list of dictionaries containing the details of the starting instance.
    """
    return start_instance_tool(instance_id)

@mcp.tool()
def stop_instance(instance_id: str) -> dict:
    """
    Stop an EC2 instance.

    Args:
        instance_id (str): The ID of the EC2 instance to stop.

    Returns:
        List: A list of dictionaries containing the details of the stopping instance.
    """
    return stop_instance_tool(instance_id)

@mcp.tool()
def get_cpu_utilization(instance_id: str) -> dict:
    """
    Get CPU utilization for an EC2 instance.

    Args:
        instance_id (str): The ID of the EC2 instance.

    Returns:
        dict: A dictionary containing the timestamp and CPU utilization in % of the EC2 instance.
    """
    return get_cpu_utilization_tool(instance_id)
