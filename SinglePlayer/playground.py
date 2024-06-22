class Playground:
    def __init__(self):
        """
        Build the playground data structure: an array of arrays with 12 x 25 size
        containing a normal tetris playing game (10 x 24) plus boundaries
        0 means a free block
        255 means boundaries
        """
        self.data = []
        self.data.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        for i in range(23):
            self.data.append([255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255])
        self.data.append([255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255])

    def remove_line(self, line_number):
        """
        Remove a line from playground restoring boundaries
        """
        self.data.pop(line_number)
        self.data.insert(1, [255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255])