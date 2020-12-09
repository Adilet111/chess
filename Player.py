

class Player:
    def __init__(self,color):
        self.color = color
        self.turn = True if color.lower()=='white' else False
    def make_move(self):
        pass
    def