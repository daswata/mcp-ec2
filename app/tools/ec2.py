from dotenv import load_dotenv
load_dotenv()

from app.services.ec2_service import EC2Service

ec2_service = EC2Service()

def list_instances():
    """
    List all EC2 instances.
    """
    instances = ec2_service.list_instances()

    return {
        "count": len(instances),
        "instances": instances
    }

def start_instance_tool(instance_id: str):
    """
    Start an EC2 instance.
    """
    response = ec2_service.start_instance(instance_id)
    return response["StartingInstances"]

def stop_instance_tool(instance_id: str):
    """
    Stop an EC2 instance.
    """
    response = ec2_service.stop_instance(instance_id)
    return response["StoppingInstances"]




