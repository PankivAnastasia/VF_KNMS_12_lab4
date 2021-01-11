import pathlib
from tkinter import *

from PIL import Image, ImageTk

from model.Map import Map
from model.Player import Player


class Window(Frame):
    def __init__(self, map: Map, player1, player2, master=None):
        self.player1: Player = player1
        self.player2: Player = player2
        self.dot_size = 10

        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        self.__init_window(map)
        self.__init_border(map)
        self.__init_ball()
        self.__init_player1()
        self.__init_player2()

    def set_ball_coor(self, x, y):
        x = (x + 1) * self.dot_size
        y = (y + 1) * self.dot_size
        self.ball.place(x=x, y=y)

    def set_player_coor(self, player_is_up, x):
        if player_is_up:
            self.player1Label.place(x=x * self.dot_size + self.dot_size)
        else:
            self.player2Label.place(x=x * self.dot_size + self.dot_size)

    def __init_window(self, map):
        self.master.wm_title("Tkinter window")
        self.master.geometry(
            str((map.width_wall + 3) * self.dot_size) +
            "x" +
            str((map.height_wall + 3) * self.dot_size))

    def __init_ball(self):
        absolute = pathlib.Path(__file__).parent.absolute()
        fullpath = str(absolute) + "/smile_ball_small.png"
        load = Image.open(fullpath)
        render = ImageTk.PhotoImage(load)
        self.ball = Label(self, image=render)
        self.ball.image = render
        self.ball.place(x=50, y=50)

    def __init_player1(self):
        self.player1Label = Label(self,
                                  bg="blue",
                                  width=int(self.player1.size * 1.45))

        self.player1Label.place(
            y=self.player1.start_coor_y * (self.dot_size * 1) + self.dot_size
        )

    def __init_player2(self):
        self.player2Label = Label(self,
                                  bg="red",
                                  width=int(self.player1.size * 1.45))

        self.player2Label.place(
            y=self.player2.start_coor_y * (self.dot_size * 1) + self.dot_size
        )

    def __init_border(self, map: Map):
        canvas = Canvas(self)

        x1, y1 = self.dot_size, self.dot_size
        x2, y2 = (map.width_wall + 2) * self.dot_size, self.dot_size
        x3, y3 = (map.width_wall + 2) * self.dot_size, (map.height_wall + 2) * self.dot_size
        x4, y4 = self.dot_size, (map.height_wall + 2) * self.dot_size

        canvas.create_line(x1, y1, x2, y2)
        canvas.create_line(x2, y2, x3, y3)
        canvas.create_line(x3, y3, x4, y4)
        canvas.create_line(x4, y4, x1, y1)

        canvas.pack(fill=BOTH, expand=1)
