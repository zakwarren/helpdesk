import random
import json
import math
from . import characters


def import_data():
    """Import datasets to internal memory"""
    with open('data/names.json') as f:
        data_names = json.load(f)
    with open('data/issues.json') as f:
        data_issues = json.load(f)
    with open('data/disasters.json') as f:
        data_disasters = json.load(f)
    return data_names, data_issues, data_disasters


def random_customer(data_names, data_issues, level_min, level_max):
    """Generate a random customer"""
    # get random basic details
    name = random.choice(data_names)
    level = random.randint(level_min, level_max)
    # get issue types available
    data_issue_types = list(data_issues.keys())
    # reduce issue types in scope for low level players
    level_ceiling = level_max - 5
    if level_ceiling <= characters.LEVEL_BOUNDS[0][1]:
        data_issue_types = data_issue_types[:2]
    elif level_ceiling <= characters.LEVEL_BOUNDS[1][1]:
        data_issue_types = data_issue_types[:4]
    # get random issue
    issue_type = random.choice(data_issue_types)
    issue = random.choice(data_issues[issue_type])
    # build customer
    customer = characters.Customer(name, level, issue_type, issue)
    return customer


def random_technician(data_names, level_min, level_max):
    """Generate a random IT technician"""
    name = random.choice(data_names)
    level = random.randint(level_min, level_max)
    technician = characters.ItTech(name, level)
    return technician


def solve_issue(technician, customer):
    """Attempt to solve the customer's issue"""
    # get relevant skill chances
    skillset = {
        "password": technician.password,
        "hardware": technician.hardware,
        "software": technician.software,
        "antivirus": technician.antivirus,
        "network": technician.network,
        "server": technician.server,
    }
    skill = skillset[customer.issue_type]
    # check if technician has a disaster
    disaster_chance = technician.disaster
    if disaster_chance >= random.randint(50, 100):
        success = False
        disaster = True
    # check if technician is successful
    elif skill > customer.level:
        success = True
        disaster = False
        # add full experience
        technician.add_exp(customer.exp)
    else:
        success = False
        disaster = False
        # give half experience round up to nearest integer
        exp = math.ceil(customer.exp / 2)
        technician.add_exp(exp)
    return success, disaster


def disaster_event(disaster, data_disasters, customer):
    """Generate a random disaster event"""
    if disaster is True:
        list_disasters = data_disasters[customer.issue_type]
        disaster_outcome = random.choice(list_disasters)
    else:
        disaster_outcome = "no disaster"
    return disaster_outcome
