import pygame
import os
from constants import Constants as C
#from .constants import Constants as C

class Card:

    def __init__(self, kind:str, value:int, image_url:str) -> None:
        self.kind = kind
        self._value = value
        self.image = pygame.transform.scale(pygame.image.load(os.path.abspath('../images/cards/'+image_url)).convert_alpha(), (C.CARD_WIDTH, C.CARD_HEIGHT))
    
    @property
    def value(self)->int:
        return self._value
    
    def draw(self, surface, x, y)->None:
       surface.blit(self.image, (x, y))

    def __gt__(self, other)->bool:
        if not self.isSameKind(other):
            raise Exception("Can't compare different kinds of cards")
        return self.value > other.value
    
    def __lt__(self, other)->bool:
        if not self.isSameKind(other):
            raise Exception("Can't compare different kinds of cards")
        return self.value < other.value
    
    def isSameKind(self, other)->bool:
        return self.kind == other.kind
    
    def __str__(self) -> str:
        return f"({self.kind}, {self.value})"