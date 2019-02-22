"""
A Helpdesk Tale
An IT helpdesk simulation game

Help customers with their IT issues,
avoid disaster and improve your skills
one ticket at a time.
"""
import sys
from code import characters
from code import operations
from code import tutorials
from code import mechanics


def main():
    """Coordinates the main programme logic"""
    # initial setup
    is_manager = False
    team = []
    hours_in_day = 8
    days_in_year = 6
    manager = "Lukasz"
    #player = tutorials.setup_player(manager)
    player = characters.ItTech("Mikey", 1)

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
            print(player)
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

                # customer arrival at helpdesk
                customer = operations.random_customer(data_names, data_issues, level_min, level_max)
                print("A customer arrived at the helpdesk.")
                queue.append(customer)

                # team management
                print("Your team: " + str(team))

                # which customer to help
                customer = operations.select_customer(player, queue)
                input(customer.name + ": Hello! " + customer.issue + ". Can you help? ")

                # player to help customer
                success, disaster = mechanics.player_help_customer(
                    player,
                    customer,
                    queue,
                    data_options
                )
                queue, exp, lost = mechanics.handle_outcome(
                    player,
                    customer,
                    queue,
                    success,
                    disaster,
                    data_disasters
                )
                print("")

                # decrease patience for anyone waiting in the queue
                for custom in queue:
                    custom.lose_patience()

                # aggregate daily counters
                daily_exp_gained += exp
                if lost:
                    daily_customers_lost += 1
                else:
                    daily_successes += 1

                # iterate game time
                hours += 1

            # daily review
            daily_customers_lost += len(queue)
            operations.review_wording(
                player,
                manager,
                is_manager,
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
            is_manager,
            "year",
            years,
            yearly_exp_gained,
            yearly_successes,
            yearly_customers_lost
        )
        year_choice = input(
            """Choice: 1 = continue to next year
        2 = quit""" \
            + "\n" + player.name + ": "
        )
        if year_choice == "2":
            sys.exit()


if __name__ == "__main__":
    main()
