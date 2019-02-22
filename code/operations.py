"""
Defines the regular operations conducted by the game mechanics
"""
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
    with open('data/options.json') as f:
        data_options = json.load(f)
    return data_names, data_issues, data_disasters, data_options


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


def random_options(data_options, customer):
    """Generate a random set of four options for the problem"""
    options_list = data_options[customer.issue_type]
    options = []
    for _ in range(0, 4):
        opt = random.choice(options_list)
        options.append(opt)
        options_list.remove(opt)
    return options


def select_customer(player, queue):
    """Take user input and select customer from helpdesk queue"""
    print("Helpdesk queue: " + str(queue))
    to_help = input(player.name + ": Who should I select? Number: ")
    print("")
    # normalise choice and apply
    try:
        if not to_help:
            to_help = 0
        else:
            to_help = int(to_help)
        if to_help <= 0:
            to_help = 0
        elif to_help > len(queue):
            to_help = len(queue) - 1
        else:
            to_help -= 1
    except:
        to_help = 0
    customer = queue[to_help]
    return customer


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
    disaster = False
    disaster_min = 75
    disaster_max = 100
    for i in range(0, 5):
        if characters.LEVEL_BOUNDS[i][0] <= technician.level <= characters.LEVEL_BOUNDS[i][1]:
            # disaster chance scales down with increasing level
            if disaster_chance >= random.randint(disaster_min, disaster_max):
                success = False
                disaster = True
        disaster_min -= 10
        disaster_max -= 10
    # check if technician is successful
    if disaster is False and skill > customer.level:
        success = True
        # add full experience
        technician.add_exp(customer.exp)
    elif disaster is False:
        success = False
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


def review_rating(technician, successes, losses):
    """Calculates an overall star rating based on performance"""
    exp = 0
    if losses == 0:
        # to avoid dividing by zero
        losses = 1
    # calculate success to loss ratio
    success_ratio = successes / losses
    # scale ratings based on current level
    upper_bound = 1
    lower_bound = 0
    for i in range(0, 5):
        low = characters.LEVEL_BOUNDS[i][0]
        high = characters.LEVEL_BOUNDS[i][1]
        if low <= technician.level <= high:
            # rebase lowest boundary if it's 0 or below
            if low <= 0:
                low = 1
            # calculate rating bounds
            half_bound = (upper_bound + lower_bound) / 2
            one_quarter_bound = (upper_bound + lower_bound) / 4
            three_quarter_bound = ((upper_bound + lower_bound) / 4) * 3
            # calculate rating
            if success_ratio >= upper_bound:
                rating = "5*"
                # random exp value between heightened level boundaries
                exp = random.randint(low + upper_bound, high + upper_bound)
            elif upper_bound > success_ratio >= three_quarter_bound:
                rating = "4*"
                # random exp value between current level boundaries
                exp = random.randint(low, high)
            elif three_quarter_bound > success_ratio >= half_bound:
                rating = "3*"
            elif half_bound > success_ratio >= one_quarter_bound:
                rating = "2*"
            elif one_quarter_bound > success_ratio >= lower_bound:
                rating = "1*"
            elif lower_bound > success_ratio:
                rating = "0*"
        # iterate upper bound
        upper_bound += 1
    # return rating
    return rating, exp


def review_wording(player, manager, is_manager, review_type, type_number, exp, successes, losses):
    """Work out what to say for the review"""
    # wording for managers
    if is_manager is True:
        you = "Your team"
    else:
        you = "You"
    # general review wording
    print("End of " + review_type + " " + str(type_number+1) + " review")
    input(manager + ": " + you + " gained " + str(exp) + " experience. ")
    input(manager + ": " + you + " had " + str(successes) + " successes, " \
        + "but lost " + str(losses) + " customers. ")
    # additional review for end of year
    if review_type == "year":
        rating, exp_gift = review_rating(player, successes, losses)
        input(manager + ": Your performance rating is " + str(rating) + ". ")
        if exp_gift > 0:
            input(manager + ": Congratulations! " \
                + "You've earned a bonus of " + str(exp_gift) + " experience points. ")
            player.add_exp(exp_gift)
        if is_manager is False and player.level > characters.LEVEL_BOUNDS[4][0]:
            is_manager = True
            input(manager + ": Congratulations! You've been promoted to a manager! ")
    print("")
