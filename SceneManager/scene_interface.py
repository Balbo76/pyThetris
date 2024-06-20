from abc import ABC, abstractmethod
class Scene(ABC):
    @abstractmethod
    def run(self):
        pass