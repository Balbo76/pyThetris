class Playground:
    def __init__(self):
        self.data = []

        self.data.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        for i in range(23):
            self.data.append([255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255])
        self.data.append([255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255])
