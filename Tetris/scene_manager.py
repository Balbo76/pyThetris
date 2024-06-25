from Tetris.Abstract.singleton_meta import SingletonMeta
from Tetris.Abstract.scene_interface import Scene


class SceneManager(metaclass=SingletonMeta):

    def __init__(self, screen):
        self._screen = screen

    @property
    def scene(self) -> Scene:
        return self._scena

    @scene.setter
    def scene(self, scena: Scene) -> None:
        self._scena = scena

    def play(self) -> None:
        result = self._scena.run(self._screen)




