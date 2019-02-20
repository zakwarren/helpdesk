from code import characters
from code import operations
from code import tutorials


def main():
    """Main entry point to programme"""
    data_names, data_issues, data_disasters = operations.import_data()

    player = characters.ItTech("Bob", 1)
    level_min = 1
    if player.level >= 95:
        level_max = 100
    else:
        level_max = player.level + 5

    customer = operations.random_customer(data_names, data_issues, level_min, level_max)
    technician = operations.random_technician(data_names, level_min, level_max)

    success, disaster = operations.solve_issue(player, customer)
    disaster_outcome = operations.disaster_event(disaster, data_disasters, customer)
    print(success, ":", disaster)


if __name__ == "__main__":
    tutorials.main()
