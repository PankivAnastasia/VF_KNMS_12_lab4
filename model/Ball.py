import random

from model.Map import Map
from util.log import log


class Ball(object):

    def __init__(self, map: Map) -> None:
        self.map = map

        coor = map.get_def_ball_coor()
        self.x = coor[0]
        self.y = coor[1]

        self.height_direction = random.randint(0, 1) == 1
        self.width_direction = random.randint(0, 1) == 1

    def is_goal(self):
        if self.y == self.map.height_wall or self.y == 0:
            return True
        return False

    def set_coor(self, x, y):
        log("set new coord to ball")
        self.x = x
        self.y = y

    def set_mirror_directions(self):
        log("set mirror directions to ball")
        self.height_direction = not self.height_direction

    def set_rand_directions(self):
        log("set rand directions to ball")
        self.height_direction = random.randint(0, 1) == 1
        self.width_direction = random.randint(0, 1) == 1

    def next_step(self):
        if self.__is_width_border():
            self.width_direction = not self.width_direction

        if self.width_direction:
            self.x += 1
        else:
            self.x -= 1

        if self.height_direction:
            self.y += 1
        else:
            self.y -= 1

    def __is_width_border(self):
        if self.x == self.map.width_wall or self.x == 0:
            log("ball is in width border")
            return True
        return False
