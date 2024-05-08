""" 
Author: Aarya
Description: On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
    The north direction is the positive direction of the y-axis.
    The south direction is the negative direction of the y-axis.
    The east direction is the positive direction of the x-axis.
    The west direction is the negative direction of the x-axis.
    
    The robot can receive one of three instructions:
        "G": go straight 1 unit.
        "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
        "R": turn 90 degrees to the right (i.e., clockwise direction).

    The robot performs the instructions given in order, and repeats them forever.
    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
Time Complexity: O(n), where n is the length of the instructions string
Space Complexity: O(1), the algorithm utilizes a few pointers that dont grow with the input.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # initialize the starting direction as north
        dir_x, dir_y = 0, 1
        # initialize the starting position as the origin (0, 0)
        x, y = 0, 0
        # loop through the instructions
        for cmd in instructions:
            # if the current instruction is "G" for go, then move the robot in the direction it's facing
            if cmd == "G":
                x, y = x + dir_x, y + dir_y
            # if the current instruction is "L" for left, then change the robot's direction to the left respective of it's current direction
            if cmd == "L":
                """
                Use vector math to change the direction to left
                e.g. if the current direction is (-1, 0) which is facing the left direction,
                    then taking a left should face the robot in the south direction
                    dir_x = -1 * dir_y = -1 * 0 => 0
                    dir_y = dir_x = -1 => -1
                    the final direction becomes (0, -1) after applying the vector math which is facing the south direction 
                """
                dir_x, dir_y = -1 * dir_y, dir_x
            # if the current instruction is "R" for right, then change the robot's direction to the right respective of it's current direction
            if cmd == "R":
                """
                Use vector math to change the direction to left
                e.g. if the current direction is (-1, 0) which is facing the left direction,
                    then taking a right should face the robot in the north direction
                    dir_x = dir_y = 0 => 0
                    dir_y = -1 * dir_x = -1 * -1 => 1
                    the final direction becomes (0, 1) after applying the vector math which is facing the north direction 
                """
                dir_x, dir_y = dir_y, -1 * dir_x
        """
        After applying all the instructions:
        1. If the robot's current position is the same as the starting position then the robot is in a loop (a circle) -> return True
        2. If the robot's current position is different than the starting position then we check if there is a change in direction
            2.1. if there is a change in direction from the initial direction (north) then the robot is in a loop (a circle) -> return True
            2.2. if there is NO change in the direction then the robot is not in a loop (NOT a circle) -> return False
        """
        return (x, y) == (0, 0) or (dir_x, dir_y) != (0, 1)