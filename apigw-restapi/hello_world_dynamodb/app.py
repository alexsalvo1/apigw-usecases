import json
import boto3
from botocore.exceptions import ClientError

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table('Orders')

    try:
        response = table.get_item(Key={'id': '1234'})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
