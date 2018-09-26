import boto3
from moto import mock_iam
import user_account_creation.user_account_creation as uac





@mock_iam
def test_user_creation():
    client = boto3.client('iam')
    username = 'thephillipsequation'
    uac.create_user(client, username)
    assert uac.user_exists(client, username) is True



