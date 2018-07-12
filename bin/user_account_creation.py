import boto3
import time
from botocore.exceptions import ClientError, ParamValidationError



def main():
    test_user = "test1"
    iam = boto3.client('iam')
    iam.create_user(
        path="/test/",
        UserName=test_user

    )
    iam.get_user(
        UserName=test_user
    )
    print("Hello World")

if __name__== "__main__":
  main()