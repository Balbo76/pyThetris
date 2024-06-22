from SinglePlayer.playground import Playground
from .TetraminoBuilder import TetrominoBuilder
import pdb

class SinglePlayer:

    def __init__(self):
        self.lineeFatte = 0
        self.gameOver = False
        self.playground = Playground()
        self.current = TetrominoBuilder().build_next()
        self.next = TetrominoBuilder().build_next()

    def tick(self):
        if self._can_go_down():
            self.move_down()
        else:
            self._add_to_playground()
            n = self._check_for_new_lines()
            self.current = self.next
            self.next = TetrominoBuilder().build_next()
            if self._check_if_game_over():
                self.gameOver = True

    def move_left(self):
        if self._can_go_left():
            self.current.x -= 1

    def move_right(self):
        if self._can_go_right():
            self.current.x += 1

    def move_down(self):
        if self._can_go_down():
            self.current.y += 1

    def rotate(self):
        if self._can_rotate():
            self.current.rotazione = (self.current.rotazione + 1) % 4

    def _can_go_down(self):
        return self.__can_move(0, 1, 0)

    def _can_go_left(self):
        return self.__can_move(-1, 0, 0)

    def _can_go_right(self):
        return self.__can_move(1, 0, 0)

    def _can_rotate(self):
        return self.__can_move(0, 0, 1)

    def __can_move(self, delta_x, delta_y, delta_rotation):
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

    def _add_to_playground(self):
        for i in range(4):
            y = self.current.y + i
            for j in range(4):
                x = self.current.x + j
                if self.current.data[self.current.rotazione][i][j] != 0:
                    self.playground.data[y][x] = self.current.id



    def _check_for_new_lines(self):
        pass

    def _check_if_game_over(self):
        pass

