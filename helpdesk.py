#from code import characters
from code import operations
from code import tutorials
from code import mechanics


def main():
    """Main programme logic"""
    # initial setup
    data_names, data_issues, data_disasters, data_options = operations.import_data()
    queue = []
    manager = "Lukasz"
    player = tutorials.setup_player(manager)
    #player = characters.ItTech("Mikey", 1)

    # level scaling
    level_min = 1
    if player.level >= 95:
        level_max = 100
    else:
        level_max = player.level + 5

    # customer arrival at helpdesk
    customer = operations.random_customer(data_names, data_issues, level_min, level_max)
    print("A customer arrived at the helpdesk.")
    queue.append(customer)

    # which customer to help
    customer = operations.select_customer(player, queue)

    # player to help customer
    queue = mechanics.player_help_customer(player, customer, queue, data_options, data_disasters)
    print(queue)


if __name__ == "__main__":
    main()
