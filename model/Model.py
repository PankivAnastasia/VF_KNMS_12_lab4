import threading
import time

from model.Ball import Ball
from model.Map import Map
from model.Player import Player
from util.log import log


class Model(object):
    def __init__(self, ball: Ball, map: Map, player1: Player, player2: Player, speed=50) -> None:
        self.speed = speed
        log("creating model")
        self.ball = ball
        self.map = map
        self.player1 = player1
        self.player2 = player2

    def run(self):
        log("start model threading")
        threading.Thread(target=self.__start_model).start()

    def set_speed(self, speed):
        self.speed = speed

    def __start_model(self):
        log('start model')
        while True:
            time.sleep(1 / self.speed)
            self.ball.next_step()

            if self.is_mirror():
                log("is mirror")
                self.__manage_mirror()
                continue

            if self.__is_end():
                log("is end")
                self.__manage_end()
                continue

    def is_mirror(self):
        coords = []
        coords.extend(self.player1.get_coor())
        coords.extend(self.player2.get_coor())

        for x, y in coords:
            if x == self.ball.x and y == self.ball.y:
                return True
        return False

    def __is_end(self):
        goal = self.ball.is_goal()
        return goal

    def __manage_end(self):
        (x, y) = self.map.get_def_ball_coor()
        self.ball.set_coor(x, y)
        self.ball.set_rand_directions()

    def __manage_mirror(self):
        self.ball.set_mirror_directions()
