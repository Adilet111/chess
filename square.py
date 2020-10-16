
import abc

class Piece(metaclass=abc.ABCMeta):
    def __init__(self,white):
        self.killed = False
        self.white = white
    def isWhite(self):
        return self.white
    def isKilled(self):
        return self.killed
    def setKilled(self,killed):
        self.killed = killed
    @abc.abstractmethod
    def canMove(self,start,end):
        pass

class Pawn(Piece):
    def __init__(self,white):
        super(Pawn, self).__init__(white)
        self.firstMove=False
    def canMove(self,start,end):



class Square:
    def __init__(self,x,y,Piece):
        self.x = x
        self.y = y
        self.piece = Piece

    def getPiece(self):
        return self.piece
    def setPiece(self,Piece):
        self.piece = Piece
