from model.Map import Map


class Player(object):

    def __init__(self, is_up, map: Map):
        self.size = int(map.width_wall / 4)

        self.start_coor_x = 0
        if is_up:
            self.start_coor_y = 1
        else:
            self.start_coor_y = map.height_wall - 2

        self.map = map

    def move_left(self):
        step = int(self.map.width_wall / 10)
        if not self.start_coor_x - step <= 0:
            self.start_coor_x -= step

    def move_right(self):
        step = int(self.map.width_wall / 10)
        if not self.start_coor_x + step >= self.map.width_wall:
            self.start_coor_x += step

    def get_coor(self):
        coord = []
        start_coor = self.start_coor_x
        for x in range(start_coor, self.size + self.start_coor_x):
            coord.append((x, self.start_coor_y))
        return coord
