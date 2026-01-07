import boto3
from datetime import datetime, timedelta

class CloudWatchService:
    def __init__(self):
        self.client = boto3.client('cloudwatch')

    def get_cpu_utilization(self, instance_id: str) -> dict:
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(hours=1)
        response = self.client.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'cpu_usage',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/EC2',
                            'MetricName': 'CPUUtilization',
                            'Dimensions': [
                                {'Name': 'InstanceId', 'Value': instance_id}
                            ]
                        },
                        'Period': 300,
                        'Stat': 'Average'
                    },
                    'ReturnData': True
                }
            ],
            StartTime=start_time,
            EndTime=end_time
        )
        result = response['MetricDataResults'][0]
        cpu_utilization = {}
        for ts, val in zip(result['Timestamps'], result['Values']):
            cpu_utilization[f'{ts}'] = val
        return cpu_utilization
