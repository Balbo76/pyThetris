from Game.playground import Playground
from .TetraminoBuilder import TetraminoBuilder


class Game:

    def __init__(self):
        self.lineeFatte = 0
        self.gameOver = False
        self.playground = Playground();
        self.current = TetraminoBuilder().build_next()
        self.next = TetraminoBuilder().build_next()

    def tick(self):
        pass

    def move_left(self):
        if self._can_go_left():
            self.current.x -= 1

    def move_right(self):
        if self._can_go_right():
            self.current.x += 1

    def move_Down(self):
        if self._can_go_down():
            self.current.y += 1

    def rotate(self):
        if self._can_rotate():
            self.current.rotazione = (self.current.rotazione + 1) % 4

    def _can_go_down(self):
        return self.__can_go(0,1,0)

    def _can_go_left(self):
        return self.__can_go(-1,0,0)

    def _can_go_right(self):
        return self.__can_go(1,0,0)

    def _can_rotate(self):
        can_rotate = True
        return can_rotate

    def __can_go(self, delta_x, delta_y, delta_rotation):
        can_go = True
        tetramino = self.current
        new_x = tetramino.x + delta_x
        new_y = tetramino.y + delta_y
        new_rotation = (tetramino.rotazione + delta_rotation) % 4

        for i in range(4):
            for j in range(4):
                if self.current.data[new_rotation][i][j] == 1:
                    x = new_x + j
                    y = new_y + i
                    if self.playground.data[y][x] > 0:
                        can_go = False

        return can_go
