from .scene import Scene
from .scene import PlayingScene
from .constants import Constants as C
import sys
import pygame


class App:
    CURRENT_SCENE:Scene = None
    FPS:int = 60
    CLOCK = pygame.time.Clock()
    WINDOW:pygame.Surface = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))


    def __init__(self) -> None:
        pygame.display.set_caption('cards')
        App.CURRENT_SCENE = PlayingScene()

    @staticmethod
    def run()->None:
        while True:
            App.CLOCK.tick(App.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN  and event.key == pygame.K_ESCAPE:
                    sys.exit()    

            App.__render()
            App.__update()

    @staticmethod
    def __update()->None:
        App.CURRENT_SCENE.update()

    @staticmethod
    def __render()->None:
        App.CURRENT_SCENE.draw()
        App.WINDOW.blit(App.CURRENT_SCENE.surface, (0, 0))