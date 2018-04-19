import boto3
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('users')

response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print(items)

response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print(items)

response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print(items)

response = table.scan(
    FilterExpression=Attr('address.state').eq('CA')
)
items = response['Items']
print(items)

