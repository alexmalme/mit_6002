'''
 Problem 1: RectangularRoom Class
10.0/10.0 points (graded)

You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position and direction of each robot.

In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:

    RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
    Position: We've also provided a complete implementation of this class. It stores the x- and y-coordinates of a robot in a room.

Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.
Problem 1

In this problem you will implement the RectangularRoom class. For this class, decide what fields you will use and decide how the following operations are to be performed:

    Initializing the object
    Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or the function math.floor - may be useful to you here)
    Determining if a given tile has been cleaned
    Determining how many tiles there are in the room
    Determining how many cleaned tiles there are in the room
    Getting a random position in the room
    Determining if a given position is in the room

Complete the RectangularRoom class by implementing its methods in ps2.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.

Hint: During debugging, you might want to use random.seed(0) so that your results are reproducible.

Enter your code for RectangularRoom below.
'''

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)




# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {}
        self.t = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height


    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = pos.getX()
        y = pos.getY()
        m, n = int(x), int(y)
        pos = (m, n)
        if pos not in self.tiles.keys():
            self.tiles[pos] = 'clean'
        self.t += 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.t >= 1:
            return (m,n) in self.tiles
        else:
            return False
        #raise NotImplementedError

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self._width * self._height
        #raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.tiles)
        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #m = random.randrange(-1*math.floor(self.width/2), math.floor(self.width/2))
        #n = random.randrange(-1*math.floor(self.height/2), math.floor(self.height/2))
        m = random.uniform(0, self.width)
        n = random.uniform(0, self.width)
        p = Position(m, n)
        return p
        #raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height:
            return True
        else:
            return False
        #raise NotImplementedError