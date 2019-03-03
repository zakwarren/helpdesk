"""
A Helpdesk Tale
An IT helpdesk simulation game

Help customers with their IT issues,
avoid disaster and improve your skills
one ticket at a time.
"""
import sys
import operations
import tutorials
import mechanics
import data


def main():
    """Coordinates the main programme logic"""
    welcome = r""" _     _____ _     ____  ____  _____ ____  _  __     
/ \ /|/  __// \   /  __\/  _ \/  __// ___\/ |/ /     
| |_|||  \  | |   |  \/|| | \||  \  |    \|   /      
| | |||  /_ | |_/\|  __/| |_/||  /_ \___ ||   \      
\_/ \|\____\\____/\_/   \____/\____\\____/\_|\_\     
                                                     
 ____  _  _      _     _     ____  _____  ____  ____ 
/ ___\/ \/ \__/|/ \ /\/ \   /  _ \/__ __\/  _ \/  __\
|    \| || |\/||| | ||| |   | / \|  / \  | / \||  \/|
\___ || || |  ||| \_/|| |_/\| |-||  | |  | \_/||    /
\____/\_/\_/  \|\____/\____/\_/ \|  \_/  \____/\_/\_\
                                                     """
    # initial setup
    print(welcome)
    data.restore_lists()
    hours_in_day = 8
    days_in_year = 6
    manager = "Lukasz"
    player = tutorials.setup_player(manager)
    team = [player]
    team_helped = []

    # main game loops
    years = 0
    while True:
        print("Year: " + str(years+1) + "\n")

        # yearly loop
        yearly_exp_gained = 0
        yearly_successes = 0
        yearly_customers_lost = 0
        days = 0
        while days < days_in_year:

            # daily loop
            print("Day: " + str(days+1) + "\n")
            queue = []
            daily_exp_gained = 0
            daily_successes = 0
            daily_customers_lost = 0
            hours = 0
            while hours < hours_in_day:
                # refresh data
                data_names, data_issues, data_disasters, data_options = operations.import_data()

                # level scaling
                level_min = 1
                if player.level >= 95:
                    level_max = 100
                else:
                    level_max = player.level + 5

                # manage customer arrival at helpdesk
                mechanics.customer_arrival(
                    team,
                    queue,
                    data_names,
                    data_issues,
                    level_min,
                    level_max
                )

                while len(team) > 0:
                    # team management
                    technician = operations.select_person(player, team, "technician")
                    team_choice = operations.team_options(player, technician)
                    if team_choice == "change":
                        # go back to start of team management loop
                        continue
                    elif team_choice == "ticket":
                        # move team member to helped already list
                        team_helped.append(technician)
                        team.remove(technician)
                        # which customer to help
                        customer = operations.select_person(player, queue, "customer")
                        input(customer.name + ": Hello! " + customer.issue + ". Can you help? ")
                        # check whether technician is player or not and act accordingly
                        if technician == player:
                            # player to help customer
                            success, disaster = mechanics.player_help_customer(
                                player,
                                customer,
                                data_options
                            )
                        else:
                            input(technician.name + " is attempting to solve the issue ")
                            success, disaster = operations.solve_issue(technician, customer)
                        # deal with the outcome
                        queue, exp, lost = mechanics.handle_outcome(
                            technician,
                            customer,
                            queue,
                            success,
                            disaster,
                            data_disasters
                        )

                # decrease patience for anyone waiting in the queue
                print("")
                for custom in queue:
                    custom.lose_patience()

                # aggregate daily counters
                daily_exp_gained += exp
                if lost:
                    daily_customers_lost += 1
                else:
                    daily_successes += 1

                # move team back to ready list
                while len(team_helped) > 0:
                    transfer = team_helped.pop()
                    team.append(transfer)

                # iterate game time
                hours += 1

            # daily review
            daily_customers_lost += len(queue)
            operations.review_wording(
                player,
                manager,
                "day",
                days,
                daily_exp_gained,
                daily_successes,
                daily_customers_lost
            )

            # aggregate yearly counters
            yearly_exp_gained += daily_exp_gained
            yearly_successes += daily_successes
            yearly_customers_lost += daily_customers_lost

            # iterate game time
            days += 1

        # yearly review
        operations.review_wording(
            player,
            manager,
            "year",
            years,
            yearly_exp_gained,
            yearly_successes,
            yearly_customers_lost
        )
        if player.is_manager is True:
            year_choice_options = """Choice: 1 = continue to next year
        2 = quit
        3 = hire new IT technician"""
        else:
            year_choice_options = """Choice: 1 = continue to next year
        2 = quit"""
        year_choice = input(year_choice_options + "\n" + player.name + ": ")
        print("")
        if year_choice == "2":
            sys.exit()
        elif player.is_manager is True and year_choice == "3":
            mechanics.hire_new_technician(player, team, data_names, level_min, level_max)


if __name__ == "__main__":
    main()
