import sys
import boto3
import os

def argument_1_has_been_provided():
    try:
        sys.argv[1]
        return True
    except IndexError:
        return False


def argument_2_has_been_provided():
    try:
        sys.argv[2]
        return True
    except IndexError:
        return False


def not_all_argument_provided(argument1, argument2):
    if not argument_1_has_been_provided():
        print("Please, provides a reagion to fetch result as the first argument.")
    if not argument_2_has_been_provided():
        print("Please, provides the user profile name as the second argument.")


def get_instances_data(region, user_profile):
    os.environ['AWS_PROFILE'] = user_profile
    ec2 = boto3.client('ec2', region_name = region)
    instances = ec2.describe_instances()["Reservations"]
    print(instances)
