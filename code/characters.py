"""
Defines the character objects
"""
from random import randint


# set the level boundaries
LEVEL_BOUNDS = [
    [0, 5],
    [5, 10],
    [10, 25],
    [25, 50],
    [50, 100],
    [100, 250],
]


class ItTech:
    """Defines the player character"""
    def __init__(self, name, level):
        """Inititalizes the character's stats"""
        # basic stats
        self.name = name
        self.level = level
        self.exp = 0
        self.charisma = randint(1, 100)
        # initialize skill stats
        self.password = 0
        self.hardware = 0
        self.software = 0
        self.antivirus = 0
        self.network = 0
        self.server = 0
        # chance of disasterous outcome
        self.disaster = 0
        # apply appropriate skill levels
        self.skill_load()


    def __str__(self):
        """Defines the string response"""
        return self.name + " is level " + str(self.level) \
            + " with " + str(self.exp) + " experience points." \
            + "\nCharisma: " + str(self.charisma) + "%" \
            + "\nChance of disaster: " + str(self.disaster) + "%" \
            + "\nPassword reset skill: " + str(self.password) + "%" \
            + "\nHardware skill: " + str(self.hardware) + "%" \
            + "\nSoftware skill: " + str(self.software) + "%" \
            + "\nAntivirus skill: " + str(self.antivirus) + "%" \
            + "\nNetwork skill: " + str(self.network) + "%" \
            + "\nServer skill: " + str(self.server) + "%\n"


    def add_exp(self, exp):
        """
        Adds experience points
        Levels up when enough experience has been gained
        """
        self.exp += exp
        # set experienced required to level up
        for i in range(0, 5):
            if LEVEL_BOUNDS[i][0] <= self.level <= LEVEL_BOUNDS[i][1]:
                # max experience for a level 
                # is set as next level's upper bound
                max_exp = LEVEL_BOUNDS[i+1][1]
        # level up if appropriate and reset experience
        if self.exp >= max_exp:
            self.level += 1
            self.exp -= max_exp
            print("Level up!")
            # increase skill stats
            self.skill_load()


    def skill_load(self):
        """
        Initializes and balances skill load
        Applies improvements with each level up
        """
        if LEVEL_BOUNDS[0][0] <= self.level <= LEVEL_BOUNDS[0][1]:
            if self.disaster:
                self.disaster -= randint(1, 3)
            else:
                self.disaster = randint(75, 95)
            if self.password:
                self.password += randint(1, 3)
            else:
                self.password = randint(1, 10)
            if self.hardware:
                self.hardware += randint(1, 3)
            else:
                self.hardware = randint(1, 10)
            self.software = 0
            self.antivirus = 0
            self.network = 0
            self.server = 0

        elif LEVEL_BOUNDS[1][0] < self.level <= LEVEL_BOUNDS[1][1]:
            if self.disaster:
                self.disaster -= randint(1, 3)
            else:
                self.disaster = randint(50, 75)
            if self.password:
                self.password += randint(1, 3)
            else:
                self.password = randint(10, 25)
            if self.hardware:
                self.hardware += randint(1, 3)
            else:
                self.hardware = randint(10, 25)
            if self.software:
                self.software += randint(1, 3)
            else:
                self.software = randint(1, 10)
            if self.antivirus:
                self.antivirus += randint(1, 3)
            else:
                self.antivirus = randint(1, 10)
            self.network = 0
            self.server = 0

        elif LEVEL_BOUNDS[2][0] < self.level <= LEVEL_BOUNDS[2][1]:
            if self.disaster:
                self.disaster -= randint(1, 3)
            else:
                self.disaster = randint(25, 50)
            if self.password:
                self.password += randint(1, 3)
            else:
                self.password = randint(25, 50)
            if self.hardware:
                self.hardware += randint(1, 3)
            else:
                self.hardware = randint(25, 50)
            if self.software:
                self.software += randint(1, 3)
            else:
                self.software = randint(10, 25)
            if self.antivirus:
                self.antivirus += randint(1, 3)
            else:
                self.antivirus = randint(10, 25)
            if self.network:
                self.network += randint(1, 3)
            else:
                self.network = randint(1, 10)
            self.server = 0

        elif LEVEL_BOUNDS[3][0] < self.level <= LEVEL_BOUNDS[3][1]:
            if self.disaster:
                self.disaster -= randint(1, 3)
            else:
                self.disaster = randint(10, 25)
            if self.password:
                self.password += randint(1, 3)
            else:
                self.password = randint(50, 75)
            if self.hardware:
                self.hardware += randint(1, 3)
            else:
                self.hardware = randint(50, 75)
            if self.software:
                self.software += randint(1, 3)
            else:
                self.software = randint(25, 50)
            if self.antivirus:
                self.antivirus += randint(1, 3)
            else:
                self.antivirus = randint(25, 50)
            if self.network:
                self.network += randint(1, 3)
            else:
                self.network = randint(10, 25)
            if self.server:
                self.server += randint(1, 3)
            else:
                self.server = randint(1, 10)

        elif LEVEL_BOUNDS[4][0] < self.level <= LEVEL_BOUNDS[4][1]:
            if self.disaster:
                self.disaster -= randint(1, 3)
            else:
                self.disaster = randint(1, 10)
            if self.password:
                self.password += randint(1, 3)
            else:
                self.password = randint(75, 100)
            if self.hardware:
                self.hardware += randint(1, 3)
            else:
                self.hardware = randint(75, 100)
            if self.software:
                self.software += randint(1, 3)
            else:
                self.software = randint(50, 75)
            if self.antivirus:
                self.antivirus += randint(1, 3)
            else:
                self.antivirus = randint(50, 75)
            if self.network:
                self.network += randint(1, 3)
            else:
                self.network = randint(25, 50)
            if self.server:
                self.server += randint(1, 3)
            else:
                self.server = randint(10, 25)

            # max and min handler
            if self.disaster < 0:
                self.disaster = 0
            if self.password > 100:
                self.password = 100
            if self.hardware > 100:
                self.hardware = 100
            if self.software > 100:
                self.software = 100
            if self.antivirus > 100:
                self.antivirus = 100
            if self.network > 100:
                self.network = 100
            if self.server > 100:
                self.server = 100


class Customer():
    """Defines the customer object"""
    def __init__(self, name, level, issue_type, issue):
        """Provide the initialization variables for the class"""
        # basics
        self.name = name
        self.level = level
        # attributes
        self.issue_type = issue_type
        self.issue = issue
        self.patience = randint(1, 100)
        # define experience available to technician on success
        for i in range(0, 5):
            if LEVEL_BOUNDS[i][0] <= self.level <= LEVEL_BOUNDS[i][1]:
                # rebase lowest boundary if it's 0 or below
                low = LEVEL_BOUNDS[i][0]
                if low <= 0:
                    low = 1
                # random value between current level boundaries
                self.exp = randint(low, LEVEL_BOUNDS[i][1])


    def __str__(self):
        """Defines the string response"""
        return self.name + " is level " + str(self.level) \
            + "\nIssue type: " + self.issue_type \
            + "\nIssue: " + self.issue \
            + "\nPatience: " + str(self.patience) + "%" \
            + "\nExperience available: " + str(self.exp) + "\n"
