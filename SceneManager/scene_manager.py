from Helpers.singleton_meta import SingletonMeta
from .scene_interface import Scene


class SceneManager(metaclass=SingletonMeta):

    def __init__(self, pygame, screen):
        self.__pygame = pygame
        self.__screen = screen

    @property
    def scene(self) -> Scene:
        return self._scena

    @scene.setter
    def scene(self, scena: Scene) -> None:
        self._scena = scena

    def play(self) -> None:
        result = self._scena.run(self.__pygame, self.__screen)




