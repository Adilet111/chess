from Piece_logic.Piece import Piece


class Pawn(Piece) :
    def __init__(self, type) :
        super().__init__(type)
    def canMove(self, board, start) :
        allowedMoves = []
        r, c = start.getLocation()
        direction = 0
        if self.isWhite():
            direction = -1
        else:
            direction = 1
        if self.selected :
            if board[r + direction][c].getPiece() is None :
                allowedMoves.append(board[r + direction][c])
            try :
                if board[r + direction][c + 1].getPiece() != None and self.colorDifference(board[r + direction][c + 1].getPiece()) :
                    allowedMoves.append(board[r + direction][c + 1])
            except IndexError :
                pass
            try :
                if board[r + direction][c - 1].getPiece() != None and self.colorDifference(board[r + direction][c - 1].getPiece()) :
                    allowedMoves.append(board[r + direction][c - 1])
            except IndexError :
                pass
            if board[r + 2*direction][c].getPiece() is None and self.firstMove :
                allowedMoves.append(board[r + 2*direction][c])
        return allowedMoves

    def Info(self) :
        return "I am pawn"