from abc import ABC, abstractmethod
class Scene(ABC):

    def __init__(self):
        pass
    @abstractmethod
    def run(self):
        pass