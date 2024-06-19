from playground import Playground
from tetramino_factory import TetraminoFactory

class Game:

    def __init__(self):
        self.lineeFatte = 0
        self.gameOver = False
        self.playground = Playground();
        self.tetramino_corrente = TetraminoFactory().get_next()
        self.prossimo_tetramino = TetraminoFactory().get_next()

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_Down(self):
        pass

    def rotate(self):
        pass

    def canGoDown(self):
        pass

    def can_Go_Left(self):
        pass

    def can_Go_Right(self):
        pass

    def can_Rotate(self):
        pass