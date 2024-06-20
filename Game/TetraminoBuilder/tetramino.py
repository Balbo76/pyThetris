from .tetramini import tetramini
class Tetramino:

    def __str__(self):
        return ''.join([str(elem) for elem in self.data[self.rotazione]])


    def __init__(self, id):
        self.corrente = 0       # Id da 0 a 6 che identifica il pezzo
        self.rotazione = 0      # da 0 a 3
        self.x = 4
        self.y = 0
        self.data = tetramini[id]

    def get_state(self):
        return self.data[self.rotazione]

    def rotate_clockwise(self):
        self.rotazione += 1
        if self.rotazione > 3 :
            self.rotazione = 0

    def rotate_counterclockwise(self):
        self.rotazione -= 1
        if self.rotazione < 0:
            self.rotazione = 3
        pass
