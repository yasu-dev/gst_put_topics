import sys
import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'Topic'
table = dynamodb.Table(table_name)

def handler(event, context):

    logger.info('PUT topics')

    body = json.loads(event['body'])

    response = table.update_item(
        Key={
            'topicId': int(event['pathParameters']['topicID'])
        },
        UpdateExpression="set topicTitle = :val1, topicBody = :val2, topicImageUrl = :val3, publish = :val4",
        ExpressionAttributeValues={
            ':val1': body['topicTitle'],
            ':val2': body['topicBody'],
            ':val3': body['topicImageUrl'],
            ':val4': body['publish']
        }
    )

    return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'headers': {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
            },
            'body': json.dumps(body)
            }
