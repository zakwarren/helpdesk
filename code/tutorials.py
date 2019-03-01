"""
Provides the game start and tutorials
"""
import math
from . import characters
from . import operations


def setup_player(manager):
    """Set up player character"""
    input(manager + ": Welcome to your new job at Incompecorp! " \
        + "Press enter to progress. ")
    input(manager + ": I'm " + manager + " and I'll be your manager here. ")
    name = input(manager + ": What's your name? ")
    if not name:
        name = "Mikey"
    print(name + ": " + name)
    level = 1
    player = characters.ItTech(name, level)
    input(manager + ": Great to meet you " + name + ". I'm sure you'll do great. ")
    input(manager + ": Would you like a full induction " \
        + "or would you prefer to get started straight away? ")
    start_choice = input(
        """\nChoice: 1 = full tutorial
        2 = quick start""" \
        + "\n\nType the number and press enter to make your choice.\n" \
        + name + ": "
    )
    if start_choice == "2":
        input(manager + ": Well no time to waste. The helpdesk awaits you! ")
        print("")
    else:
        start_tutored(player, manager)
    return player


def start_tutored(player, manager):
    """Full tutorial"""
    # setup
    input(manager + ": No problem. I have a full induction planned for you. ")
    input(manager + ": Hopefully you've eaten your bacon sandwiches this morning! ")
    queue = []

    # first customer (success)
    customer = characters.Customer(
        "Roger",
        1,
        "password",
        "I've lost my password"
    )
    input(manager + ": Oh, what good timing! A customer has arrived. " \
        + "Let's find out what they need. ")
    print("")
    # dealing with queues
    print("A customer arrived at the helpdesk.")
    queue.append(customer)
    print("Helpdesk queue: " + str(queue))
    print("")
    input(manager + ": First enter their number to select them from the queue. ")
    customer = operations.select_person(player, queue, "customer")
    # solving the issue
    input(manager + ": Great, now let's see what they need help with. ")
    print("")
    input(customer.name + ": Hello! " + customer.issue + ". Can you help? ")
    print("")
    input(manager + ": This customer has an issue with their " + customer.issue_type + ". ")
    input(manager + ": " + customer.name + " is only level " \
        + str(customer.level) + " so it's an easy one to solve. ")
    input(manager + ": Let's take a look at your options. Enter the number to make your choice. ")
    input(
        """\nChoice: 1 = Reset password
        2 = Recover password
        3 = Reset account
        4 = Use admin powers""" \
        + "\n" + player.name + ": "
    )
    print(customer.issue_type.capitalize() + " issue solved!")
    queue.remove(customer)
    print("")
    input(manager + ": Congratulations! You successfully helped this customer. ")
    input(manager + ": You've earned " + str(customer.exp) + " experience points from this helpdesk issue. ")
    player.add_exp(customer.exp)
    input(manager + ": When you achieve enough experience, you'll level up. ")
    input(manager + ": This will increase your skills and even unlock new skills. ")

    # second customer (soft fail)
    input(manager + ": Let's see if we have any more customers waiting. ")
    customer = characters.Customer(
        "Caroline",
        1,
        "password",
        "I've forgotten my password"
    )
    customer.patience = 96
    print("")
    # queue
    print("A customer arrived at the helpdesk.")
    queue.append(customer)
    customer = operations.select_person(player, queue, "customer")
    # solving the issue
    input(customer.name + ": Hey! " + customer.issue + ". Can you help? ")
    input(
        """\nChoice: 1 = Reset password
        2 = Recover password
        3 = Reset account
        4 = Use admin powers""" \
        + "\n" + player.name + ": "
    )
    print("Failed to solve " + customer.issue_type + " issue!")
    print("")
    input(manager + ": Don't worry about that. This happens a lot when you're new. ")
    exp = math.ceil(customer.exp / 2)
    input(manager + ": Failure is a good opportunity to learn. " \
        + "This time you've gained " + str(exp) + " experience. ")
    input(manager + ": Fortunately, this customer has " + str(customer.patience) + "% patience. ")
    input(manager + ": Each time you fail their patience will decrease. When it reaches 0, they'll leave. ")
    input(manager + ": Let's try again! ")
    input(
        """\nChoice: 1 = Reset password
        2 = Recover password
        3 = Reset account
        4 = Use admin powers""" \
        + "\n" + player.name + ": "
    )
    print(customer.issue_type.capitalize() + " issue solved!")
    queue.remove(customer)
    print("")
    input(manager + ": Congratulations! You successfully helped " + customer.name + ". ")
    input(manager + ": You've also earned " + str(customer.exp) + " experience points. ")
    player.add_exp(customer.exp)

    # third customer (disaster)
    input(manager + ": Let's try helping one more customer together. ")
    customer = characters.Customer(
        "Mandy",
        1,
        "hardware",
        "My screen is blank"
    )
    print("")
    # queue
    print("A customer arrived at the helpdesk.")
    queue.append(customer)
    customer = operations.select_person(player, queue, "customer")
    # solving the issue
    input(customer.name + ": Excuse me. " + customer.issue + ". Can you fix it? ")
    input(
        """\nChoice: 1 = Try turning it off and on again
        2 = Open up machine
        3 = Fix wiring
        4 = Hit it with a wrench""" \
        + "\n" + player.name + ": "
    )
    disaster = "destroyed the hardware"
    print("Disaster! You " + disaster + "!")
    print("")
    input(manager + ": Oh dear! You've caused a disaster! ")
    input(manager + ": This can happen occasionally. " \
        + "Your current chance of disaster is " + str(player.disaster) + "%. ")
    input(manager + ": You'll reduce this chance with experience. ")
    input(manager + ": Unsurprisingly, this counts as a failure. ")
    input(manager + ": However, you won't recieve any experience points. ")

    # conclusion
    print("")
    input(manager + ": Before I go, let's take a quick look at your current skills. ")
    print(player)
    input(manager + ": Not bad for a new hire. With experience, you'll improve. ")
    input(manager + ": Well that's all the induction I had planned for today. ")
    input(manager + ": You now know enough to try it on your own. Good luck! ")
    print("")
