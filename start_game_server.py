import threading
import time
from tkinter import Tk

from grafics.Elements_manager import Window
from model.Model import Model, Player
from model.Map import Map
from model.Ball import Ball
from netcode.server.server_v1 import Server
from util.log import log

log("configing")
map = Map(60, 30)
ball = Ball(map)

player1 = Player(True, map)
player2 = Player(False, map)

model = Model(ball, map, player1, player2, 30)

window = Tk()
app = Window(map, player1, player2, window)

log("start main loop")


def run_server(model, name):
    server = Server()
    server.run(model)


def run_model():
    log("start model loop")
    model.run()

    log("start getting model stats")

    while True:
        ball_x = model.ball.x
        ball_y = model.ball.y

        player1_x = model.player1.start_coor_x
        player2_x = model.player2.start_coor_x

        app.set_ball_coor(ball_x, ball_y)
        app.set_player_coor(True, player1_x)
        app.set_player_coor(False, player2_x)

        # model.set_speed(model.speed + 0.5)
        time.sleep(1 / model.speed)


threading.Thread(target=run_server, args=(model, "")).start()
threading.Thread(target=run_model).start()
window.mainloop()
