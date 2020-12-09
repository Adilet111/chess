
import abc

class Piece(metaclass=abc.ABCMeta) :
    def __init__(self, type) :
        self.killed = False
        self.white = True if type[0][0] == "w" else False
        self.selected = False
        self.type = type
        self.firstMove = True
    def isWhite(self) :
        return self.white
    def isKilled(self) :
        return self.killed
    def isSelected(self) :
        return self.selected
    def getType(self) :
        return self.type
    def setSelected(self, selected) :
        self.selected = selected
    def setFirstMove(self, first) :
        self.firstMove = first
    def colorDifference(self, piece) :
        return self.white != piece.isWhite()
    def setKilled(self, killed) :
        self.killed = killed
    @abc.abstractmethod
    def canMove(self, board, start, end) :
        pass
    @abc.abstractmethod
    def Info(self) :
        pass