from Piece_logic.Piece import Piece

class King(Piece) :
    def __init__(self, type) :
        super().__init__(type)

    def canMove(self, board, start) :
        return []

    def Info(self) :
        return "I am King"