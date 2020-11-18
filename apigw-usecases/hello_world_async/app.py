import json
import time
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):

    #simulate a batch job
    time.sleep(2)
    
    table = dynamodb.Table('Orders')
    
    table.put_item(
       Item={
            'id': '1234',
            'description': 'Order Test',
            'price': 1000,
        }
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
