'''
This module creates IAM users given a yaml file saying listing their name and group
'''
import boto3
import string
from botocore.exceptions import ClientError
from pathlib import Path
from secrets import choice


def generate_password(dict_file='/usr/share/dict/words'):
    try:
        with open(dict_file) as f:
            words = [word.strip() for word in f]
            password = password = '_'.join(choice(words) for i in range(4))
        return password
    except IOError as error:
        print('The dictionary file {} could not be found, please ensure this file is present on your system'.format(dict_file))
        return error
     

def create_login_profile(client, username, password, reset=True):
    '''
        Provide console access for a user
        resource: i.e: `iam = boto3.resource('iam)`
        username: must be a valid IAM username
        password: must comply with the IAM password policy
        reset: boolean value denoting if a password reset is required
    '''
    response = client.create_login_profile(
        UserName=username,
        Password=password,
        PasswordResetRequired=reset
    )
    print(response)
    return 

def delete_user(client, username):
    '''
        Delete an IAM user
    '''
    response = client.delete_user(
        UserName=username
    )
    print(response)

def user_exists(client, username):
    '''
        Check if a given IAM user exists, output result
    '''
    try:
        resp = client.get_user(
            UserName=username
        )
        print("Username {} already exists. Please provide a unique username".format(username))
        return True
    except ClientError as error:
        if error.response['Error']['Code'] == 'NoSuchEntity':
            print("User {} does not exist".format(username))
            return False
        else:
            print(error)


def create_user(client, username, password):
    '''Create an IAM user'''
    if user_exists(client, username) == True:
        return
    elif user_exists(client, username) == False:
        response = client.create_user(
            UserName=username
            )
        create_login_profile(client, username, password)
        print()
        return
        


def main(test=True):
    '''Main function'''
    if test == True:
        test_password = generate_password()
        test_client =  boto3.client('iam')
        test_username = 'test123'
        if user_exists(test_client, test_username):
            delete_user(test_client, test_username)
        print(test_password)
        print(test_client.get_account_password_policy())
        create_user(test_client, test_username, test_password)
if __name__ == "__main__":
    main()
