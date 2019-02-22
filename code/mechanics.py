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


def player_help_customer(player, customer, queue, data_options):
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
