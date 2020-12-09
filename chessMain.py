"""
main drive file responsible for user input and displaying the current gameState object
"""



import pygame as p
from chessEngine import *
from drawingLogic import *

WIDTH = HEIGHT = 512
DIMENSION  = 8 # dimensions for board 8x8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15 #for animation later on
IMAGES = {}
REVERSED_DICT = {'Pawn':"p", 'Rook':"R", 'Knight':"N", 'Bishop':"B", 'Queen':"Q",'King':"K"}

"""
Initialize global dictionary of images.
"""

def loadImage():
    pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))
    #we can access an image by using a dictionary
'''
main driver will handle user input and updating the graphics
'''


def manage_clicks(gs,r,c,sqSelected, playerClicks,valid_moves):

    # if the same cell is clicked
    if sqSelected == (r, c) :
        if gs.board[r][c].getPiece() != None :
            gs.board[r][c].getPiece().setSelected(False)
            sqSelected = ()
            playerClicks = []
            valid_moves = []
    # this is the first click of a mouse or a second click on different square
    else :
        sqSelected = r, c
        # checking whether there is piece and is it a first click
        # if it clicked on empty square and it is first click then we do not save it
        if gs.board[r][c].getPiece() == None and len(playerClicks) == 0 :
            sqSelected = ()
            playerClicks = []
        # we check the turns

        # if there is a piece we select it
        if gs.board[r][c].getPiece() != None and \
                gs.board[r][c].getPiece().isWhite() == gs.whiteToMove :
            gs.board[r][c].getPiece().setSelected(True)
        # we need to safe the square we choose in clicks
        square = Square(r, c, gs.board[r][c].getPiece())
        playerClicks.append(square)
    # if this is the second click and different from first
    if len(playerClicks) == 2 :
        # Check that first click is actually with piece on it (may be not necessary check)
        if playerClicks[0].getPiece() != None :
            playerClicks[0].getPiece().setSelected(False)
        # We create move object
        mv = Move(playerClicks[0], playerClicks[1])
        print(mv.getChessNotation())
        # check whether the end square in the valid moves, if yes the make move
        if mv.endSq in valid_moves :
            gs.move(mv)
        valid_moves = []
        playerClicks = []
        sqSelected = ()
    return sqSelected, playerClicks, valid_moves




def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    val_move_surf = p.surface.Surface((WIDTH,HEIGHT))

    gs = GameState()
    loadImage()
    running =True
    sqSelected = () # no square selected initially keep track of the last click of the user
    playerCLicks=[] # keep track of players clicks  [two tuples]
    valid_moves = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                sqSelected, playerCLicks, valid_moves = manage_clicks(gs,row,col,sqSelected,playerCLicks,valid_moves)
                #here we generate valid moves when clicked on the square with some Piece
                if  gs.board[row][col].getPiece() != None and gs.board[row][col].getPiece().isSelected():
                    selected_piece = gs.board[row][col].getPiece()
                    valid_moves = selected_piece.canMove(gs.board, gs.board[row][col])
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    valid_moves = []
                    sqSelected = ()
                    playerCLicks = []


        #drawGameState(screen,gs)
        drawBoard(screen,valid_moves)
        drawPieces(screen, gs.board, IMAGES)
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()























