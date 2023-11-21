class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_x, dir_y = 0, 1
        x, y = 0, 0

        for cmd in instructions:
            if cmd == "G":
                x, y = x + dir_x, y + dir_y
            if cmd == "L":
                dir_x, dir_y = -1 * dir_y, dir_x
            if cmd == "R":
                dir_x, dir_y = dir_y, -1 * dir_x
    
        return (x, y) == (0, 0) or (dir_x, dir_y) != (0, 1)