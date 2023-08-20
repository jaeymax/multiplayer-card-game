from abc import abstractmethod, ABC
import pygame
from .constants import Constants as C

class Scene(ABC):
      
      def __init__(self) -> None:
          self.surface:pygame.Surface = pygame.Surface((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))

      @abstractmethod
      def draw(self):
            pass
      
      @abstractmethod
      def update(self):
            pass


class PlayingScene(Scene):
      
      def __init__(self) -> None:
            super().__init__()

      def draw(self):
            self.surface.fill(C.PLAYING_SCENE_BACKGROUND_COLOR)
      
      def update(self):              
            pygame.display.update()