import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=s3_bucket, Key=file_name)
    content = response['Body'].read().decode('utf-8')

    body="The Link to your bucket object is"+"https://"+s3_bucket+".s3.us-east-1.amazonaws.com/"+file_name+"\n \n Contents:\n"+content
    return body