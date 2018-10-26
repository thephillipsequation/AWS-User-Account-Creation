import boto3
import user_account_creation.main as uac
import os.path
from moto import mock_iam


# def test_password_generation():
#     assert 

@mock_iam
def test_delete_user():
    client = boto3.client('iam')
    username = 'thephillipsequation'
    uac.create_user(client, username, password="test1234")
    uac.delete_user(client, username)
    assert uac.user_exists(client, username) is False

@mock_iam
def test_user_creation():
    client = boto3.client('iam')
    username = 'thephillipsequation'
    uac.create_user(client, username, password="test1234")
    assert uac.user_exists(client, username) is True





    