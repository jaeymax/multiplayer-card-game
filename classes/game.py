from .deck import Deck

class GameController:

    def __init__(self, id:int) -> None:
        self.deck = Deck()
        self.__leader = 'playerOne'
        self.playerOneCards = []
        self.playerTwoCards = []


    @property
    def leader(self):
        return self.__leader
    

    @leader.setter
    def leader(self, value):
        self.__leader = value
        
    
        
    