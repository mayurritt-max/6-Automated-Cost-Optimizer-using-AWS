import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            if state == 'running':
                ec2.stop_instances(InstanceIds=[instance_id])
                print("Stopping:", instance_id)

    return "Done"
