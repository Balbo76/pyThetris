from Game.playground import Playground
from .TetraminoBuilder import TetraminoBuilder


class Game:

    def __init__(self):
        self.lineeFatte = 0
        self.gameOver = False
        self.playground = Playground();
        self.tetramino_corrente = TetraminoBuilder().get_next()
        self.prossimo_tetramino = TetraminoBuilder().get_next()

    def tick(self):
        pass

    def move_left(self):
        if self._can_go_left():
            self.tetramino_corrente.x -= 1

    def move_right(self):
        if self._can_go_right():
            self.tetramino_corrente.x += 1

    def move_Down(self):
        if self._can_go_down():
            self.tetramino_corrente.y += 1

    def rotate(self):
        if self._can_rotate():
            self.tetramino_corrente.rotazione = ( self.tetramino_corrente.rotazione + 1 ) % 4

    def _can_go_down(self):
        pass

    def _can_go_left(self):
        pass

    def _can_go_right(self):
        pass

    def _can_rotate(self):
        pass

    def __can_go(self, delta_x, delta_y, delta_rotation):
        can_go = True
        tetramino = self.tetramino_corrente
        new_x = tetramino.x + delta_x
        new_y = tetramino.y + delta_y
        new_rotation = (tetramino.rotazione + delta_rotation) % 4

        for i in range(4):
            for j in range(4):
                if self.tetramino_corrente.data[new_rotation][i][j] == 1:
                    x = new_x + j
                    y = new_y + i

        """         
                       for (var i=0; i<=3; i++) {
                           for (var j=0; j<=3; j++) {	
                               if (tetramini[this.corrente][mr][i][j] == 1) {
                                   var 
                                       x = mx + j,
                                       y = my + i;

                                   if (that.schermata[y][x] > 0){
                                       canMove = false;
                                   }
                               }
                           }
                       }
               """

        return can_go
