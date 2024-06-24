from .playground import Playground
from .tetromino import Tetromino

class PlayerGame:

    def __init__(self):
        self.lineeFatte = 0
        self.gameOver = False
        self.playground = Playground()
        self.current = Tetromino()
        self.next = Tetromino()

    def tick(self):
        """
        Bring the game status to the next step: this means
        our tetramino will go down (fall) one position otherwise,
        if there is no other space to fall, it will be added to playground and related check will be done.
        """
        if self._can_go_down():
            self.move_down()
        else:
            self._add_to_playground()
            self.lineeFatte += self._check_for_new_lines()
            self.current = self.next
            self.next = Tetromino()
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
            self.current.rotation_step = (self.current.rotation_step + 1) % 4

    def _can_go_down(self):
        return self.__can_move(0, 1, 0)

    def _can_go_left(self):
        return self.__can_move(-1, 0, 0)

    def _can_go_right(self):
        return self.__can_move(1, 0, 0)

    def _can_rotate(self):
        return self.__can_move(0, 0, 1)

    def _add_to_playground(self):
        for i in range(4):
            y = self.current.y + i
            for j in range(4):
                x = self.current.x + j
                if self.current.data[self.current.rotation_step][i][j] != 0:
                    self.playground.data[y][x] = self.current.id

    def _check_for_new_lines(self):
        new_lines = []
        for i in range(24):
            new_line = True
            for j in range(12):
                if self.playground.data[i][j] == 0:
                    new_line = False
            if new_line:
                new_lines.append(i)

        for line in new_lines:
            self.playground.remove_line(line)

        return len(new_lines)

    def _check_if_game_over(self):
        return not self.__can_move(0,0,0)

    def __can_move(self, delta_x, delta_y, delta_rotation):
        can_move = True
        tetramino = self.current
        new_x = tetramino.x + delta_x
        new_y = tetramino.y + delta_y
        new_rotation = (tetramino.rotation_step + delta_rotation) % 4

        for i in range(4):
            for j in range(4):
                if self.current.data[new_rotation][i][j] == 1:
                    x = new_x + j
                    y = new_y + i
                    if self.playground.data[y][x] > 0:
                        can_move = False

        return can_move