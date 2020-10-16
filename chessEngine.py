"""
This class is responcible for storing all the information about current state. Also for calculation
of valid moves and keep move log
"""
import abc

def make_instance(cls,*arg):
    return cls(arg)



class Piece(metaclass=abc.ABCMeta):
    def __init__(self,type):
        self.killed = False
        self.white = True if type[0][0] == "w" else False
        self.selected = False
        self.type = type
        self.firstMove = True
    def isWhite(self):
        return self.white
    def isKilled(self):
        return self.killed
    def isSelected(self):
        return self.selected
    def getType(self):
        return self.type
    def setSelected(self,selected):
        self.selected = selected
    def setFirstMove(self,first):
        self.firstMove = first
    def colorDifference(self, piece):
        return self.white != piece.isWhite()
    def setKilled(self,killed):
        self.killed = killed
    @abc.abstractmethod
    def canMove(self,board,start,end):
        pass
    @abc.abstractmethod
    def Info(self) :
        pass



class Pawn(Piece):
    def __init__(self,type):
        super().__init__(type)
    def canMove(self,board,start):
        allowedMoves = []
        r,c = start.getLocation()
        if self.selected:
            if board[r-1][c].getPiece() is None:
                allowedMoves.append(board[r-1][c])
            try:
                if board[r-1][c+1].getPiece() != None and self.colorDifference(board[r - 1][c + 1].getPiece()):
                    allowedMoves.append(board[r - 1][c+1])
            except IndexError:
                pass
            try:
                if board[r - 1][c - 1].getPiece() != None and self.colorDifference(board[r - 1][c - 1].getPiece()):
                    allowedMoves.append(board[r - 1][c - 1])
            except IndexError:
                pass
            if board[r-2][c].getPiece() is None and self.firstMove:
                allowedMoves.append(board[r - 2][c])
        return allowedMoves

    def Info(self):
        return "I am pawn"




class Rook(Piece):
    def __init__(self,type):
        super().__init__(type)
    def canMove(self,board,start):
        return []
    def Info(self):
        return "I am rook"


class Knight(Piece):
    def __init__(self,type):
        super().__init__(type)
    def canMove(self,board,start):
        return []
    def Info(self):
        return "I am knight"



class Bishop(Piece):
    def __init__(self,type):
        super().__init__(type)
    def canMove(self,board,start):
        return []
    def Info(self):
        return "I am bishop"



class Queen(Piece):
    def __init__(self,type):
        super().__init__(type)
    def canMove(self,board,start):
        return []
    def Info(self):
        return "I am Queen"



class King(Piece):
    def __init__(self,type):
        super().__init__(type)
    def canMove(self,board,start):
        return []
    def Info(self):
        return "I am King"





PIECES = {"wp" : Pawn, "wR":Rook, "wN":Knight,"wB":Bishop,"wQ":Queen,"wK":King,
            "bp" : Pawn, "bR":Rook, "bN":Knight,"bB":Bishop,"bQ":Queen,"bK":King }

class Square:
    def __init__(self,x,y,Piece=None):
        self.x = x
        self.y = y
        self.piece = Piece

    def getPiece(self):
        return self.piece
    def setPiece(self,Piece,board):
        self.piece = Piece
    def getLocation(self):
        return self.x, self.y
    def __eq__(self, other) :
        """Overrides the default implementation"""
        if isinstance(other, Square) :
            return self.x == other.x and self.y == other.y

        return False


class Board:
    def __init__(self,conf):
        self.conf = conf
        self.board = [[0 for _ in range(8)] for _ in range(8)]

    def arrangeSquares(self):
        for row in range(len(self.conf)):
            for col, piece in enumerate(conf[row]):
                if piece != "--":
                    obj = make_instance(PIECES[piece], piece)
                    self.board[row][col] = Square(row,col, obj)
                else:
                    self.board[row][col] = Square(row, col)
        return self.board




conf = [    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]


class GameState():
    def __init__(self):
        #board is 8x8 2-d list, each element of the list has 2 characters. The 1st character represents color 'b'
        # or'w' the second type of piece. We have "K", "Q", "B", "N", "R". Finally "--" represents empty place.
        b = Board(conf)
        self.board = b.arrangeSquares()
        self.whiteToMove = True
        self.moveLog = []

    def move(self,mv):
        self.board[mv.startRow][mv.startCol].setPiece(None,self.board)
        self.board[mv.endRow][mv.endCol].setPiece(mv.pieceMoved,self.board)
        mv.pieceMoved.setFirstMove(False)
        self.moveLog.append(mv)
        self.whiteToMove = not self.whiteToMove

    def undoMove(self):
        if len(self.moveLog) >0:
            move = self.moveLog.pop()
            capt_row = move.endRow
            capt_col = move.endCol
            moved_row = move.startRow
            moved_col  = move.startCol
            self.board[capt_row][capt_col].setPiece(move.pieceCaptured,self.board)
            self.board[moved_row][moved_col].setPiece(move.pieceMoved,self.board)
        else:
            print("no moves were done")



class Move:
    ranksToRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = {v:k for k,v in ranksToRows.items()}

    filesToCols = {"a":0, "b":1,"c":2, "d":3,"e":4, "f":5, "g":6,"h":7}
    colsToFiles = {v:k for k,v in filesToCols.items()}

    def __init__(self,startSq, endSq):
        self.endSq=endSq
        self.startRow,self.startCol = startSq.getLocation()

        self.endRow, self.endCol = endSq.getLocation()
        self.pieceMoved = startSq.getPiece()
        self.pieceCaptured = endSq.getPiece()

    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol)+self.getRankFile(self.endRow,self.endCol)

    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]


    def __eq__(self, other) :
        """Overrides the default implementation"""
        if isinstance(other, Move) :
            return self.startRow==other.startRow and self.startCol ==other.startCol \
            and self.endRow == other.endRow and self.endCol == other.endCol
        return False

