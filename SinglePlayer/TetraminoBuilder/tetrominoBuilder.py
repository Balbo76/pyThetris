from .tetromino import Tetromino
from Helpers.singleton_meta import SingletonMeta
import random

class TetrominoBuilder(metaclass=SingletonMeta):

    def build_next(self):
        return Tetromino(int(random.random() * 7))
