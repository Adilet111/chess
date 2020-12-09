from Piece_logic.Piece import Piece
class Knight(Piece) :
    def __init__(self, type) :
        super().__init__(type)

    def canMove(self, board, start) :
        allowedMoves = []
        r, c = start.getLocation()
        row_directions = [-2,2]
        col_directions = [-1,1]
        if self.selected:
            for row in row_directions:
                for col in col_directions:
                    try :
                        if r+row>= 0 and c +col >= 0:
                            if board[r + row][c + col].getPiece() == None:
                                allowedMoves.append(board[r + row][c + col])
                            elif self.colorDifference(board[r +row][c + col].getPiece()):
                                allowedMoves.append(board[r + row][c + col])
                    except IndexError :
                        pass
            for row in col_directions:
                for col in row_directions:
                    try :
                        if r + row >= 0 and c + col >= 0 :
                            if board[r + row][c + col].getPiece() == None :
                                allowedMoves.append(board[r + row][c + col])
                            elif self.colorDifference(board[r + row][c + col].getPiece()) :
                                allowedMoves.append(board[r + row][c + col])
                    except IndexError :
                        pass
        return allowedMoves
    def Info(self) :
        return "I am Knight"