import boto3

class EC2Service:
    def __init__(self):
        self.client = boto3.client("ec2")

    def list_instances(self):
        response = self.client.describe_instances()
        instances = []
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "InstanceId": instance["InstanceId"],
                    "State": instance["State"]["Name"],
                    "InstanceType": instance["InstanceType"]
                })
        return instances

    def start_instance(self, instance_id: str):
        response = self.client.start_instances(InstanceIds=[instance_id])
        return response
    
    def stop_instance(self, instance_id: str):
        response = self.client.stop_instances(InstanceIds=[instance_id])
        return response
