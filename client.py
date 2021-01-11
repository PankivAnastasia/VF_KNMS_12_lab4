import socket, threading, time
from tkinter import Tk

from grafics.Elements_manager import Window
from model.Map import Map
from model.Player import Player
from netcode.DataContainer import DataContainer
from util.log import log


def get_connect():
    server_ip = ("192.168.56.1", 4040)
    client_ip = ('192.168.56.1', 0)

    connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connect.bind(client_ip)
    return connect, server_ip


def init_graph():
    log("configing")
    map = Map(60, 30)

    player1 = Player(True, map)
    player2 = Player(False, map)

    window = Tk()
    app = Window(map, player1, player2, window)
    return app, window


def receving(name, sock, app):
    print(f"Start reciving model data")
    while True:
        data, addr = sock.recvfrom(1024)

        data_dict = DataContainer().decontain_model(data.decode("utf-8"))
        # print(f"Get new model data: {data_dict}")

        app.set_ball_coor(data_dict["ball_x"], data_dict["ball_y"])
        app.set_player_coor(True, data_dict["pl1_x"])
        app.set_player_coor(False, data_dict["pl2_x"])

        time.sleep(0.05)


def run_gui(connect, server_ip):
    shutdown = False
    join = False

    client_name = input("Name: ")

    while not shutdown:
        if not join:

            connect.sendto(("[" + client_name + "] => join chat ").encode("utf-8"), server_ip)
            join = True
        else:
            message = input()
            connect.sendto(message.encode("utf-8"), server_ip)

            time.sleep(0.05)

    connect.close()


connect, server_ip = get_connect()

app, window = init_graph()
threading.Thread(target=receving, args=("RecvThread", connect, app)).start()
threading.Thread(target=run_gui, args=(connect, server_ip)).start()
window.mainloop()
