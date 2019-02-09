

class ItTech:
    """Defines the player character"""
    def __init__(self, exp, level, t):
        """Inititalises the character's stats"""
        # basic stats
        self.exp = exp
        self.level = level
        # skill stats
        self.password = t
        self.hardware = t
        self.software = t
        self.antivirus = t
        self.network = t
        self.server = t
        # chance of disasterous outcome
        self.disaster = t

    def add_exp(self, exp):
        """
        Adds experience points
        Levels up when enough experience has been gained
        """
        self.exp += exp
        # set experienced required to level up
        if self.level == 0:
            max_exp = 10
        elif 0 < self.level <= 5:
            max_exp = 100
        elif 5 < self.level <= 10:
            max_exp = 200
        elif 10 < self.level <= 25:
            max_exp = 500
        elif 25 < self.level <= 50:
            max_exp = 1000
        elif 50 < self.level:
            max_exp = 2000
        # level up if appropriate and reset experience
        if self.exp >= max_exp:
            self.level += 1
            self.exp -= max_exp
            # increase skill stats
