import boto3
import json
import time

iam = boto3.client("iam")

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "lambda.amazonaws.com"},
        "Action": "sts:AssumeRole"
    }]
}

role = iam.create_role(
    RoleName="CostOptimizerLambdaRole",
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)

iam.attach_role_policy(
    RoleName="CostOptimizerLambdaRole",
    PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

iam.attach_role_policy(
    RoleName="CostOptimizerLambdaRole",
    PolicyArn="arn:aws:iam::aws:policy/AmazonEC2FullAccess"
)

print("Role Created")
print(role["Role"]["Arn"])