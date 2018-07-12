import boto3
from botocore.exceptions import ClientError, ParamValidationError

def create_user(client, username):
    client.create_user(
        UserName=username
        )

def delete_user(client, username):
    client.delete_user(
        UserName=username
    )

def user_exists(client, username):
    try:
        resp = client.get_user(
        UserName=username
        )
        print("User {} successfully created".format(username))
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            print("User {} Already Exists".format(username))

def main():
    test_user = "test1"
    iam = boto3.client('iam')
    delete_user(iam, test_user)
    create_user(iam, test_user)
    user_exists(iam, test_user)
    user_exists(iam, "steve")
    

if __name__== "__main__":
  main()