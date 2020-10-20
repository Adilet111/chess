"""
main drive file responsible for user input and displaying the current gameState object
"""



import pygame as p
from chessEngine import *


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
                #
                if sqSelected == (row,col) :
                    if gs.board[row][col].getPiece()!=None:
                        gs.board[row][col].getPiece().setSelected(False)
                        sqSelected = ()
                        playerCLicks = []
                        valid_moves = []
                    else:
                        continue
                #this is the first click of a mouse or a second click on different square
                else:
                    sqSelected = row,col
                    # checking whether there is piece and is it a first click
                    #if it clicked on empty square and it is first click then we do not save it
                    if gs.board[row][col].getPiece() == None and len(playerCLicks)==0:
                        sqSelected = ()
                        playerCLicks = []
                        continue
                    # we check the turns

                    # if there is a piece we select it
                    if gs.board[row][col].getPiece() !=None and \
                                    gs.board[row][col].getPiece().isWhite()==gs.whiteToMove:
                        gs.board[row][col].getPiece().setSelected(True)
                    # we need to safe the square we choose in clicks
                    square = Square(row,col,gs.board[row][col].getPiece())
                    playerCLicks.append(square)
                # if this is the second click and different from first
                if len(playerCLicks)==2:
                    #Check that first click is actually with piece on it (may be not necessary check)
                    if playerCLicks[0].getPiece()!=None:
                        playerCLicks[0].getPiece().setSelected(False)
                    #We create move object
                    mv = Move(playerCLicks[0],playerCLicks[1])
                    print(mv.getChessNotation())
                    #check whether the end square in the valid moves, if yes the make move
                    if mv.endSq in valid_moves:
                        gs.move(mv)
                    valid_moves = []
                    playerCLicks = []
                    sqSelected = ()


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
        drawPieces(screen, gs.board)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
Responsible for all the graphics
'''
def drawGameState(screen,gs):
    drawBoard(screen) #draw squares on the board
    drawPieces(screen, gs.board) #draw pieces on top of those squares



def drawBordersForValidMoves(screen,valid_moves):
    BLACK = (0,0,0)
    for move in valid_moves:
        p.draw.lines(screen, BLACK, True, [(move.y*SQ_SIZE,move.x*SQ_SIZE),\
                                           (move.y*SQ_SIZE,move.x*SQ_SIZE+SQ_SIZE),\
                                           (move.y*SQ_SIZE+SQ_SIZE,move.x*SQ_SIZE+SQ_SIZE),\
                                           (move.y*SQ_SIZE+SQ_SIZE,move.x*SQ_SIZE)],4)

'''
Draw the squares
'''

def drawBoard(screen,valid_moves):
    WHITE = (255,255,255)
    GREY  = (90, 102, 93)

    for j in range (8):
        for i in range(8):
            if (i+j)%2 == 0:
                p.draw.rect(screen, WHITE, p.Rect(i*SQ_SIZE, j*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                p.draw.rect(screen, GREY, p.Rect(i*SQ_SIZE, j*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    for move in valid_moves:
        p.draw.rect(screen, (245, 236, 113), p.Rect(move.y * SQ_SIZE, move.x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    drawBordersForValidMoves(screen, valid_moves)

'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen,board):
    for j,row in enumerate(range(len(board))):
        for i,sq in enumerate(board[j]):
            if (sq.getPiece() == None):
                continue
            else:

                pi = sq.getPiece()
                img = pi.getType()[0]
                screen.blit(IMAGES[img], p.Rect(i*SQ_SIZE, j*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
    main()























