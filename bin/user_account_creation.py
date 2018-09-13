'''
This module creates IAM users given a yaml file saying listing their name and group
'''
import boto3
from botocore.exceptions import ClientError

def create_user(client, username):
    '''Create an IAM user'''
    client.create_user(
        UserName=username
        )

def delete_user(client, username):
    '''Delete an IAM user'''
    client.delete_user(
        UserName=username
    )

def user_exists(client, username):
    '''Check if a given IAM user exists, output result'''
    try:
        resp = client.get_user(
            UserName=username
        )
        print("User {} exists".format(username))
        return True
    except ClientError as error:
        if error.response['Error']['Code'] == 'NoSuchEntity':
            print("User {} does not exist".format(username))
            return False

def main():
    '''Main function'''
    test_user = "test1"
    iam = boto3.client('iam')
    create_user(iam, test_user)
    user_exists(iam, test_user)
    delete_user(iam, test_user)
    user_exists(iam, "steve")

if __name__ == "__main__":
    main()
