from .position import Position


class Rover(object):
    """Mars Rover object and also the various attributes of the Mars Rover"""
    # Available commands key values
    AVAILABLE_COMMANDS = {
        'M': 'move',
        'L': 'turn_left',
        'R': 'turn_right',
    }

    DIRECTIONS = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    heading = DIRECTIONS['N']

    def __init__(self, plateau, position, heading):
        """
        Initializing mars rover with below params
        :param plateau:
        :param position:
        :param heading:
        """
        self.plateau = plateau
        self.position = position
        self.heading = heading

    def __str__(self):
        return self.current_position

    def set_position(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y

        self.heading = heading

    @property
    def current_position(self):
        return '{} {} {}'.format(self.position.x, self.position.y, self.get_heading)

    @property
    def get_heading(self):
        directions = list(self.DIRECTIONS.keys())

        try:
            direction = directions[self.heading - 1]
        except IndexError:
            direction = 'N'
            print('Direction error...')

        return direction

    def process(self, commands):
        """Process NASA commands before running"""
        for i in range(len(commands)):
            self.run_command(commands[i])

    def run_command(self, command):
        """Run NASA commands to spin left, right, or to move"""
        if 'L' == command:
            self.turn_left()
        elif 'R' == command:
            self.turn_right()
        elif 'M' == command:
            if not self.move():
                print("Where are you trying to go?")
        else:  # Unrecognized instruction
            print("Wrong parameters!..")

    def move(self):
        """Moves the rover according to its position on the plane"""
        if not self.plateau.move_available(self.position):
            return False
        # Assume that the square directly North from (x, y) is (x, y+1).
        if self.DIRECTIONS['N'] == self.heading:
            self.position.y += 1
        elif self.DIRECTIONS['E'] == self.heading:
            self.position.x += 1
        elif self.DIRECTIONS['S'] == self.heading:
            self.position.y -= 1
        elif self.DIRECTIONS['W'] == self.heading:
            self.position.x -= 1

        return True

    def turn_left(self):
        """Spins the rover to the left without moving it"""
        self.heading = self.DIRECTIONS['W'] if (self.heading - 1) < self.DIRECTIONS['N'] else self.heading - 1

    def turn_right(self):
        """Spins the rover to the right without moving it"""
        self.heading = self.DIRECTIONS['N'] if (self.heading + 1) > self.DIRECTIONS['W'] else self.heading + 1
