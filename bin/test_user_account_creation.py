import pytest
import boto3
from user_account_creation import *


client = boto3.client('iam')

def test_user_does_exit(client):
    assert user_exists(client, 'thephillipsequation') is True



