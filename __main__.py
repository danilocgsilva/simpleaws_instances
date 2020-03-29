import boto3
import os
from src import get_profile, get_all_regions, get_instances_from_region

os.environ['AWS_PROFILE'] = get_profile()

ec2 = boto3.client('ec2')

for region_name in get_all_regions(ec2):
    print("Region " + region_name + ":")
    print(get_instances_from_region(region_name))
