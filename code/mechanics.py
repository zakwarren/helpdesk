"""
Provides the main game mechanics
"""
import math
from . import operations


def handle_outcome(technician, customer, queue, success, disaster, data_disasters):
    """Handle the outcomes of helpdesk interactions"""
    lost = False
    if success is True:
        exp = customer.exp
        technician.add_exp(exp)
        input(customer.issue_type.capitalize() + " issue solved! " \
            + technician.name + " gained " + str(exp) + " experience! ")
        queue.remove(customer)
        input(customer.name + " left happy. ")
    elif success is False and disaster is False:
        exp = math.ceil(customer.exp / 2)
        technician.add_exp(exp)
        input("Failed to solve " + customer.issue_type + " issue! " \
            + technician.name + " gained " + str(exp) + " experience! ")
        customer.lose_patience()
        if customer.patience == 0:
            queue.remove(customer)
            input(customer.name + " ran out of patience and left. ")
            lost = True
    elif disaster is True:
        exp = 0
        disaster_outcome = operations.disaster_event(disaster, data_disasters, customer)
        input("Disaster! " + technician.name + " " + disaster_outcome + "!")
        queue.remove(customer)
        input(customer.name + " left in despair. You gained no experience. ")
        lost = True
    return queue, exp, lost


def player_help_customer(player, customer, data_options):
    """Player interaction to help customer with their issue"""
    # options available
    options = operations.random_options(data_options, customer)
    print("Choices:")
    i = 1
    for opt in options:
        print("    " + str(i) + " = " + opt)
        i += 1
    choice = input(player.name + ": ")

    # attempt to solve problem and return results
    if not choice:
        success = False
        disaster = True
    else:
        try:
            choice = int(choice)
            success, disaster = operations.solve_issue(player, customer)
        except:
            success = False
            disaster = True
    return success, disaster


def customer_arrival(team, queue, data_names, data_issues, level_min, level_max):
    """Manage customer arrival at helpdesk based on team size"""
    team_size = len(team)
    for _ in range(0, team_size):
        customer = operations.random_customer(data_names, data_issues, level_min, level_max)
        queue.append(customer)
    if team_size == 1:
        arrival_descriptor = "A customer has"
    else:
        arrival_descriptor = str(team_size) + " customers have"
    print(arrival_descriptor + " arrived at the helpdesk.")


def hire_new_technician(player, team, data_names, level_min, level_max):
    """Review and hire new technicians"""
    input(player.name + ": Let's review the resumes of our current candidates. ")
    # generate candidates
    resumes = []
    for _ in range(0, 3):
        tech = operations.random_technician(data_names, level_min, level_max)
        resumes.append(tech)
    # select a candidate and get player choice
    hired = False
    while True:
        person = operations.select_person(player, resumes, "resumes")
        while True:
            choice_string = "Choice: 1 = see " + person.name + """'s stats
        2 = hire """ + person.name + """
        3 = view another resume"""
            candidate_choice = input(choice_string + "\n" + player.name + ": ")
            # action choice
            if candidate_choice == "1":
                print(person)
            elif candidate_choice == "2":
                input(person.name + " hired! ")
                team.append(person)
                hired = True
                break
            elif candidate_choice == "3":
                break
            else:
                print("Unrecognised choice")
        if hired is True:
            break
