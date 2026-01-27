from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    
    def make_move(self):
        a,b = random.choice(self.moves)
        x,y = self.position
        self.position = (x + a, y + b)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0,1), # x, y
            (0,-1),
            (1,0),
            (-1,0)
        ]
    
    def level_up(self):
        self.moves.extend([
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ])
