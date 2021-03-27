import boto3
import json

def lambda_handler(event, context):
    db = boto3.resource('dynamodb')

    db_tb=db.Table("portfolio-viewcount")


    
    val = db_tb.get_item(
    Key={
        'id' : 1
    }
    )

    if 'Item' not in val:
        db_tb.put_item(
        Item={
            'id' : 1,
            'count' : 0
        }
    )
       
    print(val)
    print(val['Item']['count'])

    value = val['Item']['count']

    addval=value+1
    

    db_tb.put_item(
        Item={
            'id' : 1,
            'count' : addval
        }
    )

    return{
        "statusCode":200,
        "headers":{
            "Content-Type" : "application/json",
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        "body":  str(addval),
        "isBase64Encoded": False
    }
