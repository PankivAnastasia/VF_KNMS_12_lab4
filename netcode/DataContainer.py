class DataContainer:

    def contain_model(self, model):
        message = f"{model.ball.x} {model.ball.y} {model.player1.start_coor_x} {model.player2.start_coor_x}"
        return message

    def decontain_model(self, message):
        split = message.split(" ")

        dict = {
            "ball_x": int(split[0]),
            "ball_y": int(split[1]),
            "pl1_x": int(split[2]),
            "pl2_x": int(split[3])
        }

        return dict
