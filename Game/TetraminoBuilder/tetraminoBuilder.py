from .tetramino import Tetramino
from Helpers.singleton_meta import SingletonMeta
import random

class TetraminoBuilder(metaclass=SingletonMeta):

    def build_next(self):
        return Tetramino(int(random.random()*7))
