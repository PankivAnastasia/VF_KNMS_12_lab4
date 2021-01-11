import socket, time
import threading

from model.Model import Model
from netcode.DataContainer import DataContainer


class Server:

    def __init__(self) -> None:
        port = 4040
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))

        self.socket = s
        self.clients_ip = []

    def run(self, model: Model):

        quit = False
        print("[ Server Started ]")

        threading.Thread(target=self.__run_reciving, args=(model, "")).start()

        # pl1_addr = ""
        # pl2_addr = ""

        while not quit:
            (data, addr) = self.socket.recvfrom(1024)
            print("New message: ", data.decode("utf-8"), " from ", addr)
            if addr not in self.clients_ip:
                self.clients_ip.append(addr)

            data_str = data.decode("utf-8")
            # if addr == pl1_addr:
            if "q" in data_str:
                model.player1.move_left()

            if "e" in data_str:
                model.player1.move_right()

            # if addr == pl2_addr:
            if "a" in data_str:
                model.player2.move_left()

            if "d" in data_str:
                model.player2.move_right()

            time.sleep(0.05)

        self.socket.close()

    def __run_reciving(self, model, temp):
        while True:
            for client_ip in self.clients_ip:
                print(f"Send model data to {client_ip}")
                self.socket.sendto(DataContainer().contain_model(model).encode("utf-8"), client_ip)
                time.sleep(0.05)
