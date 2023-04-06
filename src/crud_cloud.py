import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to dynamodb
dynamodb = boto3.resource(service_name = 'dynamodb',
                    region_name = os.getenv('REGION_NAME'), 
                    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'))
response = dynamodb.get_available_subresources()
print(response)


# Getting the data from table
# table = dynamodb.Table('covalent')
# all_data = table.scan()
# print(all_data)
# print(table.creation_date_time)