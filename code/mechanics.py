import math
from . import operations


def player_help_customer(player, customer, queue, data_options, data_disasters):
    """Player interaction to help customer with their issue"""
    # help selected customer
    input(customer.name + ": Hello! " + customer.issue + ". Can you help? ")

    # options available
    options = operations.random_options(data_options, customer)
    print("Choices:")
    i = 1
    for opt in options:
        print(str(i) + " = " + opt)
        i += 1
    choice = input(player.name + ": ")

    # attempt to solve problem
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

    # handle outcome
    if success is True:
        player.add_exp(customer.exp)
        input(customer.issue_type.capitalize() + " issue solved! " \
            + player.name + " gained " + str(customer.exp) + " experience! ")
        queue.remove(customer)
        input(customer.name + " left happy. ")
    elif success is False and disaster is False:
        exp = math.ceil(customer.exp / 2)
        player.add_exp(exp)
        input("Failed to solve " + customer.issue_type + " issue! " \
            + player.name + " gained " + str(exp) + " experience! ")
        customer.lose_patience()
        if customer.patience == 0:
            queue.remove(customer)
            input(customer.name + " ran out of patience and left. ")
    elif disaster is True:
        disaster_outcome = operations.disaster_event(disaster, data_disasters, customer)
        input("Disaster! " + player.name + " " + disaster_outcome + "!")
        queue.remove(customer)
        input(customer.name + " left in despair. You gained no experience. ")
    
    return queue
