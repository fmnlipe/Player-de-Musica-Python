from typing import Type
import pygame as pg
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        pg.init()
        mixer.init()
        self.clock = pg.time.Clock()
    
    def menu(self, botao: Type[any] ) -> None:
        botao.apertarbotao()


class Botaodeplay():
     def apertarbotao(self):
        mixer.music.load("Insira a música aqui")
        mixer.music.play()
        while mixer.music.get_busy():
            self.clock.tick(10)

class Botaodeparar:
      def apertarbotao(self):
        mixer.music.stop()

class Botaoderetomar:
    def apertarbotao(self):
        mixer.music.unpause()

play = Botaodeplay()
pause = Botaodeparar()
despause = Botaoderetomar()
spotifydepobre = MusicPlayer()
spotifydepobre.menu(play)