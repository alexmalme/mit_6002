'''
 Problem 5: RandomWalkRobot Class
10.0/10.0 points (graded)

iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly after every time step, rather than just when they run into walls. You have been asked to design a simulation to determine what effect, if any, this change has on room cleaning times.

Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) but implements the new movement strategy. RandomWalkRobot should have the same interface as StandardRobot.

Test out your new class. Perform a single trial with the StandardRobot implementation and watch the visualization to make sure it is doing the right thing. Once you are satisfied, you can call runSimulation again, passing RandomWalkRobot instead of StandardRobot.

Enter your code for classes Robot and RandomWalkRobot below.
'''

# Enter your code for Robot and RandomWalkRobot in this box


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        raise NotImplementedError  # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        angle = self.getRobotDirection()
        pos = self.getRobotPosition()
        speed = self.speed
        self.room.cleanTileAtPosition(pos)
        try_new_position = pos.getNewPosition(angle, speed)
        if not self.room.isPositionInRoom(try_new_position):
            self.setRobotDirection(random.randint(0, 359))
        else:
            self.setRobotPosition(try_new_position)


# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)

# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    runs = {}
    for i in range(num_trials):
        result = run_robo(num_robots, speed, width,
                          height, min_coverage, robot_type)
        runs[i] = result
    all_time_steps = sum(runs.values())
    return all_time_steps / num_trials


def run_robo(num_robots, speed, width, height, min_coverage, robot_type):
    room = RectangularRoom(width, height)
    robots = [robot_type(room, speed) for r in range(num_robots)]
    total_tiles = room.getNumTiles()
    cleaned = room.getNumCleanedTiles()
    time_steps = 0
    num_tiles_to_clean = total_tiles * min_coverage
    while cleaned <= num_tiles_to_clean:
        time_steps += 1
        for robot in robots:
            robot.updatePositionAndClean()
        cleaned = room.getNumCleanedTiles()
        if cleaned >= num_tiles_to_clean:
            break
    return time_steps


# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(3, 1.0, 10, 10, 0.75, 3, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        pos = self.getRobotPosition()
        speed = self.speed
        self.room.cleanTileAtPosition(pos)
        angle = random.randint(0, 359)
        try_new_position = pos.getNewPosition(angle, speed)
        if not self.room.isPositionInRoom(try_new_position):
            self.setRobotDirection(random.randint(0, 359))
        else:
            self.setRobotDirection(angle)
            self.setRobotPosition(try_new_position)
