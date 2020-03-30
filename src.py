import sys
import os
import boto3
from Instance_Iterator import Instance_Iterator;

def get_profile(): 
    return sys.argv[1]


def get_all_regions(client):

    regions = []

    for region_data in client.describe_regions()["Regions"]:
        regions.append(region_data["RegionName"])

    return regions


def get_instances_from_region(region_name):

    ec2 = boto3.client('ec2', region_name = region_name)

    instances = ec2.describe_instances()["Reservations"]

    instance_iterator = Instance_Iterator(instances)

    instances_data = instance_iterator.get_instances()

    if len(instances_data) == 0:
        return "There's no instance in this region."

    text_data = ""
    iteration = 1
    for instance_data in instances_data:
        text_data += get_instance_data_readable(instance_data)
        if len(instances_data) is not iteration:
            text_data += "\n"
        iteration += 1

    return text_data


def get_instance_data_readable(instance_data):

    string_to_return = ""

    instance = instance_data["Instances"][0]

    instance_id = instance["InstanceId"]
    instance_size = instance["InstanceType"]

    string_to_return += "id: " + instance_id + "\n"
    string_to_return += "\tsize: " + instance_size

    return string_to_return
