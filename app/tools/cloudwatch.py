from dotenv import load_dotenv
load_dotenv()

from app.services.cloudwatch_service import CloudWatchService

cloudwatch_service = CloudWatchService()

def get_cpu_utilization_tool(instance_id: str):
    """
    Get CPU utilization for an EC2 instance.
    """
    return cloudwatch_service.get_cpu_utilization(instance_id)

if __name__ == "__main__":
    print(get_cpu_utilization_tool("i-0986abcaab95e0317"))