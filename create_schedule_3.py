import boto3

events = boto3.client("events")
lam = boto3.client("lambda")

rule = events.put_rule(
    Name="DailyCostOptimizer",
    ScheduleExpression="rate(1 day)",
    State="ENABLED"
)

events.put_targets(
    Rule="DailyCostOptimizer",
    Targets=[
        {
            "Id": "1",
            "Arn": "arn:aws:lambda:ap-south-1:475432297908:function:CostOptimizer"
        }
    ]
)

lam.add_permission(
    FunctionName="CostOptimizer",
    StatementId="AllowEventBridgeInvoke",
    Action="lambda:InvokeFunction",
    Principal="events.amazonaws.com",
    SourceArn=rule["RuleArn"]
)

print("Daily Schedule Created")