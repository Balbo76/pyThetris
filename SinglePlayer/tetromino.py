import random
from .tetrominos_data import tetrominos_vector_data
class Tetromino:

    def __init__(self):
        id = int(random.random() * 7)
        self.id = id + 1
        self.rotation_step = 0
        self.x = 4
        self.y = 0
        self.data = tetrominos_vector_data[id]

    def get_state(self):
        return self.data[self.rotation_step]

    def __str__(self):
        return ''.join([str(elem) for elem in self.data[self.rotation_step]])