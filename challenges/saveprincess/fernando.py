#!/bin/python
from collections import Counter


class SavePrincess(object):

    """
    Class used to save the princess
    """

    def __init__(self, grid):
        self.robot = self.find_person(grid, "m")
        self.princess = self.find_person(grid, "p")
        self.path = []

        compare = lambda x, y: Counter(x) == Counter(y)

        while not compare(self.robot, self.princess):
            # print self.path
            self.step_to_princess()

        # print self.path

    def __str__(self):
        """
        Print the result of the class
        """
        return "\n".join(self.path)


    def find_person(self, grid, person):
        """
        find an element in a grid
        """
        for lin in xrange(len(grid)):
            if grid[lin].find(person) is not -1:
                coord = [grid[lin].find(person), lin]
                # print "Find {0}: {1} ".format(person, coord)

        return coord

    def step_to_princess(self):
        """
        Define the next step to reach the princess
        """
        if ((self.robot[0] >= self.princess[0]) and
                (self.robot[1] >= self.princess[1])):
            if ((self.robot[0] - self.princess[0]) >
                    (self.robot[1] - self.princess[1])):
                self.robot[0] -= 1
                self.path.append("LEFT")
            else:
                self.robot[1] -= 1
                self.path.append("UP")
        elif ((self.robot[0] >= self.princess[0]) and
                (self.robot[1] <= self.princess[1])):
            if ((self.robot[0] - self.princess[0]) >
                    (self.princess[1] - self.robot[1])):
                self.robot[0] -= 1
                self.path.append("LEFT")
            else:
                self.robot[1] += 1
                self.path.append("DOWN")
        elif ((self.robot[0] <= self.princess[0]) and
                (self.robot[1] >= self.princess[1])):
            if ((self.princess[0] - self.robot[0]) >
                    (self.robot[1] - self.princess[1])):
                self.robot[0] += 1
                self.path.append("RIGHT")
            else:
                self.robot[1] -= 1
                self.path.append("UP")
        else:
            if ((self.princess[0] - self.robot[0]) >
                    (self.princess[1] - self.robot[1])):
                self.robot[0] += 1
                self.path.append("RIGHT")
            else:
                self.robot[1] += 1
                self.path.append("DOWN")



def displayPathtoPrincess(n, grid):
    """
    find a path to the princess
    """
    solution = SavePrincess(grid)
    print "{0}".format(solution)


def main():
    # print all the moves here
    m = input()

    grid = []
    for i in xrange(0, m):
        grid.append(raw_input().strip())

    displayPathtoPrincess(m, grid)

if __name__ == "__main__":
    main()
