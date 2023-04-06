from venv import logger
import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError
# Import the module
import json

load_dotenv()


# For a Boto3 client. Connect to dynamodb
dynamodb_resource = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
response = dynamodb_resource.list_tables()
# print(response)

# For a Boto3 resource. Connect to dynamodb
dynamodb_resource = boto3.resource(service_name = 'dynamodb',
                    region_name = os.getenv('LOCAL_REGION_NAME'),
                    aws_access_key_id = os.getenv('LOCAL_AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key = os.getenv('LOCAL_AWS_SECRET_ACCESS_KEY'),
                    endpoint_url='http://localhost:8000')


"""
Encapsulates a DynamoDB resource to run PartiQL statements.
"""

def __init__(self, dynamodb_resource):
    """
    :param dynamodb_resource: A Boto3 DynamoDB resource.
    """
    self.dynamodb_resource = dynamodb_resource

"""
Get all tables
"""

def get_table_count(self):
    tables = list(self.dynamodb_resource.tables.all())
    print(tables)

"""
Load json data 
"""

def load_json_data():
    try:
        """
        Open the orders.json file
        """
        with open("C:\\Code\\Agnostiq\\Dynamodb\\data\\data.json") as file:
            """
            Load its content and make a new dictionary
            """
            data = json.load(file)
            
    except Exception as e:
        print(e)
    else:
        return data

"""
Create the DynamoDB table.
"""

def create_table():
    try:
        table = dynamodb_resource.create_table(
            TableName='covalent',
            KeySchema=[
                {
                    'AttributeName': 'userId',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': '_id',
                    'KeyType': 'RANGE'
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
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        """
        Wait until the table exists.
        """
        table.wait_until_exists()
        """
        Print out some data about the table.
        """
        print(table.item_count)

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
"""
Execute a statement from DynamoDB table
"""
def execute_statement(statement, params):
    
    try:
        output = dynamodb_resource.meta.client.execute_statement(
                Statement=statement, Parameters=params)
    
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            logger.error("Couldn't execute PartiQL '%s' because the table does not exist.", statement)
        else:
            logger.error("Couldn't execute PartiQL '%s'. Here's why: %s: %s", statement,
                    err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        return output

"""
Execute batch of statement from DynamoDB table
"""

def batch_execute_statement(statements, param_list):

    try:
        output = dynamodb_resource.meta.client.batch_execute_statement(
            Statements=[{
                'Statement': statement, 'Parameters': params
            } for statement, params in zip(statements, param_list)])
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            logger.error("Couldn't execute batch of PartiQL statements because the table does not exist.")
        else:
            logger.error("Couldn't execute batch of PartiQL statements. Here's why: %s: %s",
                err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        return output

"""
Delete DynamoDB table
"""

def get_count(items):
    try:
        count = len(items)
    except Exception as e:
        print(e.response['Error']['Message'])
    else:
        return count


"""
Delete DynamoDB table
"""
def delete_table(table_name):
    try:
        table = dynamodb_resource.Table(table_name)
        table.delete()
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response 


if __name__ == '__main__':
    # Create table in DynamoDB
    # isTableCreated = create_table()
    # if isTableCreated:
    #     print("Table creation in DynamoDB succeeded...!!!")
    #     print(isTableCreated)

    """
    Load data
    """
    items = load_json_data()

    """
    Batch execute
    """
    # print(f"Insert data in batch")
    # statements = [f"INSERT INTO covalent VALUE {{'userId': ?, '_id': ?}}"] * len(items)
    # param_list =  [list(item.values()) for item in items]
    # isBatchExecuted = batch_execute_statement(statements=statements, param_list=param_list)
    # if isBatchExecuted:
    #     print("Batch execute in DynamoDB succeeded...!!!")
    #     print(isBatchExecuted)

    """
    Insert a item from DynamoDB
    """
    # print(f"Insert a item from DynamoDB.")
    # userId = "sampleUser2"
    # _id = "sampleId2"
    # insertItem = execute_statement(
    #     f"INSERT INTO covalent VALUE {{'userId': ?, '_id': ?}}",[userId, _id])
    # # insertItem = execute_statement(f"INSERT INTO covalent VALUE {{'userId': ?, '_id': ?, 'info': ?}}",[userId, _id, {'x': userId, 'y': _id}])
    # if insertItem:
    #    print("Insert a item from DynamoDB succeeded...!!!")
    #    print(insertItem)

    """
    Get batch of items from DynamoDB
    """
    # print(f"Getting data for a batch of items.")
    # statements = [f"SELECT * FROM covalent WHERE userId=? AND _id=?"] * len(items)
    # params = [[item['userId'], item['_id']] for item in items]    
    # getBatchItems = batch_execute_statement(statements=statements, param_list=param_list)
    # if getBatchItems:
    #    print("Get batch item from DynamoDB succeeded...!!!")
    #    print(getBatchItems)

    """
    Get a item from DynamoDB
    """
    # print(f"Get a item from DynamoDB.")
    # userId = "sampleUser"
    # _id = "sampleId"
    # getItem = execute_statement(f"SELECT * FROM covalent WHERE userId=? AND _id=?", [userId, _id])
    # print(getItem['Items'])
    # if getItem:
    #    print("Get a item from DynamoDB succeeded...!!!")
    #    print(getItem)

    """
    Count and Sort items in DynamoDB
    """
    print(f"Get a item from DynamoDB.")
    userId = "sampleUser"
    _id = "sampleId"
    getItem = execute_statement(f"SELECT * FROM covalent WHERE userId=? AND _id=? ORDER BY _id ASC", [userId, _id])
    print(getItem['Items'])
    print("Count :", get_count(getItem))
    if getItem:
       print("Get a item from DynamoDB succeeded...!!!")
       print(getItem)
    

    """
    search and filter items in DynamoDB
    """
    print(f"Get a item from DynamoDB.")
    userId = "y"
    _id = "yy"
    getItem = execute_statement(f"SELECT * FROM covalent WHERE userId=? AND _id=? ORDER BY _id ASC", [userId, _id])
    print(getItem['Items'])
    print("Count :", get_count(getItem))
    if getItem:
       print("Get a item from DynamoDB succeeded...!!!")
       print(getItem)

    """
    Delete batch of items in table from DynamoDB
    """
    # print(f"Delete data for a batch of items.")
    # statements = [f"DELETE FROM covalent WHERE userId=? AND _id=?"] * len(items)
    # param_list = [[item['userId'], item['_id']] for item in items]    
    # deleteBatchItems = batch_execute_statement(statements=statements, param_list=param_list)
    # if deleteBatchItems:
    #    print("Delete batch of items from table in DynamoDB succeeded...!!!")
    #    print(deleteBatchItems)

    """
    Delete a item from DynamoDB
    """
    # print(f"Delete a item from DynamoDB.")
    # userId = "sampleUser"
    # _id = "sampleId"
    # deleteItem = execute_statement(
    #     f"DELETE FROM covalent WHERE userId': ?, '_id': ?",[{userId, _id}])
    # if deleteItem:
    #    print("Delete a item from DynamoDB succeeded...!!!")
    #    print(deleteItem)

    """
    Delete table from DynamoDB
    """
    # isDeleted = delete_table("covalent")
    # if isDeleted:
    #    print("Delete table from DynamoDB succeeded...!!!")
    #    print(isDeleted)