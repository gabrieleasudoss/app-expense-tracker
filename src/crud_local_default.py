import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

# Get all tables

# For a Boto3 client. Connect to dynamodb
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
response = dynamodb.list_tables()
# print(response)

# For a Boto3 resource. Connect to dynamodb
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

#Create DynamoDB table
def create_table():
    try:
        table = dynamodb.create_table(
            TableName='covalent-3',
            KeySchema=[
                {
                    'AttributeName': 'userId',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': '_id',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'userId',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': '_id',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return table

#Get a record in from DynamoDB table
def get_dispatch(userId, _id):
    try:
        response = dynamodb.get_item(       
                TableName='covalent-1',
                Key={
                        'userId': {
                                'S': "{}".format(userId),
                        },
                        '_id': {
                                'S': "{}".format(_id),
                        }
                    },
                # ProjectionExpression='experiment_desc,experiment_name',
                )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


#Delete DynamoDB table
def delete_table(table_name):
    try:
        table = dynamodb.Table(table_name)
        table.delete()
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response 




if __name__ == '__main__':

    # Create DynamoDB
    table = create_table()
    print("Create DynamoDB succeeded...!!!")
    print("Table status:{}".format(table))


    # Get an item from DynamoDB
    # getDispatch = get_dispatch("user1", "1001",)
    # if getDispatch:
    #    print("Get an item from DynamoDB succeeded...!!!")
    #    print(getDispatch)
    
    # Delete a table from DynamoDB
    # isDeleted = delete_table("Movies")
    # if isDeleted:
    #    print("Delete table from DynamoDB succeeded...!!!")
    #    print(isDeleted)