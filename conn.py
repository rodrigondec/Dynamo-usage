import boto.dynamodb

conn = boto.dynamodb.connect_to_region(
        'us-west-2',
        aws_access_key_id='<YOUR_AWS_KEY_ID>',
        aws_secret_access_key='<YOUR_AWS_SECRET_KEY>')
        
print(conn) # <boto.dynamodb.layer2.Layer2 object at 0x3fb3090>
