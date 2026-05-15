import boto3

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")

    instances = ec2.describe_instances()

    stopped = []

    for r in instances["Reservations"]:
        for i in r["Instances"]:
            if i["State"]["Name"] == "running":
                ec2.stop_instances(
                    InstanceIds=[i["InstanceId"]]
                )
                stopped.append(i["InstanceId"])

    return {
        "message": "Stopped instances",
        "instances": stopped
    }