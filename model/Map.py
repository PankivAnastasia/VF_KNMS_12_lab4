class Map(object):

    def __init__(self, height, width) -> None:
        self.height_wall = height
        self.width_wall = width

    def get_def_ball_coor(self):
        def_width_ball_position = int(self.width_wall / 2)
        def_height_ball_position = int(self.height_wall / 2)
        return def_width_ball_position, def_height_ball_position
