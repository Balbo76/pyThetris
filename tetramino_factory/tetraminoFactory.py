from .tetramino import Tetramino
from .singleton_meta import SingletonMeta
import random

class TetraminoFactory(metaclass=SingletonMeta):

    def get_next(self):
        return Tetramino(int(random.random()*7))
