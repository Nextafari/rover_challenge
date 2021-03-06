class Position:
    """Mars Rover position on a cartisian plane(plateau)"""
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, position):
        return self.x == position.x and self.y == position.y
