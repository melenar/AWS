import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=s3_bucket, Key=file_name)
    email_ids = response['Body'].read().decode('utf-8').splitlines()

    ses = boto3.client('ses')

    subject = 'Congratulations! You are verified member now'
    sender = 'shubhmanav2@gmail.com'
    msg_body = 'There you go now that you are a member of our organisation lets start with the tutorial.'

    for email_id in email_ids:
        response = ses.send_email(
            Source=sender,
            Destination={'ToAddresses': [email_id]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': msg_body}}    }   )

    return {
        'statusCode': 200,
        'body': json.dumps('All mails sent.')
    }