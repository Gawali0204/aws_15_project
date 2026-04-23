import json

def lambda_handler(event, context):
    print("Pipeline Triggered!")
    return {
        'statusCode': 200,
        'body': json.dumps('Deployment Successful')
    }
