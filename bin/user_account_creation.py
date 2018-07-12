import boto3
from botocore.exceptions import ClientError, ParamValidationError

def create_user(client, username, path="\"):
    client.create_user(
        UserName=username,
        Path=path
        )

def main():
    test_user = "test1"
    iam = boto3.client('iam')
    create_user(iam, test_user)
    print(iam.get_user(
        UserName=test_user
    ))
    print({}).format(test_user)

if __name__== "__main__":
  main()