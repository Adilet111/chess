
from chessMain import SQ_SIZE
import pygame as p

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
def drawPieces(screen,board, imgs):
    for j,row in enumerate(range(len(board))):
        for i,sq in enumerate(board[j]):
            if (sq.getPiece() == None):
                continue
            else:
                piece = sq.getPiece()
                img = piece.getType()[0]
                screen.blit(imgs[img], p.Rect(i*SQ_SIZE, j*SQ_SIZE,SQ_SIZE,SQ_SIZE))