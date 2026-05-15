import boto3

lam = boto3.client("lambda")

with open("lambda.zip", "rb") as f:
    zipped = f.read()

response = lam.create_function(
    FunctionName="CostOptimizer",
    Runtime="python3.12",
    Role="arn:aws:iam::475432297908:role/CostOptimizerLambdaRole",
    Handler="lambda_function.lambda_handler",
    Code={"ZipFile": zipped},
    Timeout=30
)

print("Lambda Created")
print(response["FunctionArn"])