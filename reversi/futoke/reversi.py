import os
import sys
import time
import random

BOARD_SIZE = 8
BLACK_CHIP = '¡ö'
WHITE_CHIP = '¡è'


def draw_board(board):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §Ó§í§Ó§à§Õ§Ú§ä §ß§Ñ §ï§Ü§â§Ñ§ß §Ú§Ô§â§à§Ó§à§Ö §á§à§Ý§Ö §ã §ä§Ö§Ü§å§ë§Ö§Þ §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö§Þ
    §æ§Ú§ê§Ö§Ü.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: None.
    """

    HLINE = '   ©À©¤©¤©¤©à©¤©¤©¤©à©¤©¤©¤©à©¤©¤©¤©à©¤©¤©¤©à©¤©¤©¤©à©¤©¤©¤©à©¤©¤©¤©È'

    os.system('cls')

    print('     §Ñ   §Ò   §Ó   §Ô   §Õ   §Ö   §Ø   §Ù') 
    print('   ©°©¤©¤©¤©Ð©¤©¤©¤©Ð©¤©¤©¤©Ð©¤©¤©¤©Ð©¤©¤©¤©Ð©¤©¤©¤©Ð©¤©¤©¤©Ð©¤©¤©¤©´')

    for y in range(BOARD_SIZE):
        print('', y + 1 , end=' ')

        for x in range(BOARD_SIZE):
            print('©¦ {}'.format(board[x][y]), end=' ')
        print('©¦')

        if y != BOARD_SIZE - 1:
            print(HLINE)

    print('   ©¸©¤©¤©¤©Ø©¤©¤©¤©Ø©¤©¤©¤©Ø©¤©¤©¤©Ø©¤©¤©¤©Ø©¤©¤©¤©Ø©¤©¤©¤©Ø©¤©¤©¤©¼')


def reset_board(board):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §à§ã§å§ë§Ö§ã§ä§Ó§Ý§ñ§Ö§ä §ß§Ñ§é§Ñ§Ý§î§ß§à§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: None
    """

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            board[x][y] = ' '

    board[3][3] = BLACK_CHIP
    board[3][4] = WHITE_CHIP
    board[4][3] = WHITE_CHIP
    board[4][4] = BLACK_CHIP


def getNewBoard():
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §ã§à§Ù§Õ§Ñ§Ö§ä §á§å§ã§ä§à§Ö §Ú§Ô§â§à§Ó§à§Ö §á§à§Ý§Ö.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §Õ§Ó§å§Þ§Ö§â§ß§í§Û §ã§á§Ú§ã§à§Ü "§Ü§Ý§Ö§ä§à§Ü" §Ú§Ô§â§à§Ó§à§Ô§à §á§à§Ý§ñ.
    """
    
    board = []
    for i in range(BOARD_SIZE):
        board.append([' '] * BOARD_SIZE)

    return board


def is_valid_move(board, tile, xstart, ystart):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §á§â§à§Ó§Ö§â§ñ§Ö§ä §á§â§Ñ§Ó§Ú§Ý§î§ß§à§ã§ä§î §ã§Õ§Ö§Ý§Ñ§ß§ß§à§Ô§à §ç§à§Õ§Ñ.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.
        tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ú§Ô§â§à§Ü.
        xstart -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ §ä§Ö§Ü§å§ë§Ö§Ô§à §ç§à§Õ§Ñ §á§à §·.
        ystart -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ §ä§Ö§Ü§å§ë§Ö§Ô§à §ç§à§Õ§Ñ §á§à Y.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        False -- §Ó §ã§Ý§å§é§Ñ§Ö, §Ö§ã§Ý§Ú §Ú§Ô§â§à§Ü §á§í§ä§Ñ§Ö§ä§ã§ñ §á§à§ã§ä§Ñ§Ó§Ú§ä§î §æ§Ú§ê§Ü§å §ß§Ñ §Ù§Ñ§ß§ñ§ä§å§ð §Ü§Ý§Ö§ä§Ü§å
            §Ú§Ý§Ú §Ù§Ñ §á§â§Ö§Õ§Ö§Ý§í §Ú§Ô§â§à§Ó§à§Ô§à §á§à§Ý§ñ, §Ý§Ú§Ò§à §Õ§Ö§Ý§Ñ§Ö§ä §ç§à§Õ, §Ü§à§ä§à§â§í§Û §ß§Ö §á§à§Ù§Ó§à§Ý§Ú§ä
            §Ö§Þ§å §á§Ö§â§Ö§Ó§Ö§â§ß§å§ä§î §æ§Ú§ê§Ü§Ú §á§â§à§ä§Ú§Ó§ß§Ú§Ü§Ñ.
        
        §ª§­§ª

        §³§á§Ú§ã§à§Ü §Ü§à§à§â§Õ§Ú§ß§Ñ§ä §æ§Ú§ê§Ö§Ü §á§â§à§ä§Ú§Ó§ß§Ú§Ü§Ñ, §Ü§à§ä§à§â§í§Ö §Ú§Ô§â§à§Ü §Þ§à§Ø§Ö§ä §á§Ö§â§Ö§Ó§Ö§â§ß§å§ä§î §ï§ä§Ú§Þ 
        §ç§à§Õ§à§Þ.
    """

    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False

    board[xstart][ystart] = tile

    if tile == BLACK_CHIP:
        other_tile = WHITE_CHIP
    else:
        other_tile = BLACK_CHIP

    tiles_to_flip = []
    for xdirection, ydirection in [[0, 1],  [1, 1],   [1, 0],  [1, -1],
                                   [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection

        if is_on_board(x, y) and board[x][y] == other_tile:
            x += xdirection
            y += ydirection

            if not is_on_board(x, y):
                continue

            while board[x][y] == other_tile:
                x += xdirection
                y += ydirection

                if not is_on_board(x, y):
                    break

            if not is_on_board(x, y):
                continue

            if board[x][y] == tile:

                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x, y])

    board[xstart][ystart] = ' ' # §°§é§Ú§ë§Ñ§Ö§Þ §á§à§Ù§Ú§è§Ú§ð §á§â§à§Ó§Ö§â§ñ§Ö§Þ§à§Ô§à §ç§à§Õ§Ñ

    if len(tiles_to_flip) == 0: # §¦§ã§Ý§Ú §ß§Ö §å§Õ§Ñ§Ý§à§ã§î §á§Ö§â§Ö§Ó§Ö§â§ß§å§ä§î §ß§Ú §à§Õ§ß§à§Û §æ§Ú§ê§Ü§Ú
        return False            # §á§â§à§ä§Ú§Ó§ß§Ú§Ü§Ñ -- §Ó§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ False
        
    return tiles_to_flip


def is_on_board(x, y):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §á§â§à§Ó§Ö§â§ñ§Ö§ä §á§â§Ú§ß§Ñ§Õ§Ý§Ö§Ø§ß§à§ã§ä§î §Ù§Ñ§Õ§Ñ§ß§ß§à§Û §Ü§Ý§Ö§ä§Ü§Ú §Ú§Ô§â§à§Ó§à§Þ§å §á§à§Ý§ð.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        x -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ §ç §á§â§à§Ó§Ö§â§ñ§Ö§Þ§à§Û §Ü§Ý§Ö§ä§Ü§Ú.
        y -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ y §á§â§à§Ó§Ö§â§ñ§Ö§Þ§à§Û §Ü§Ý§Ö§ä§Ü§Ú.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        True -- §Ö§ã§Ý§Ú §Ü§Ý§Ö§ä§Ü§Ñ §á§â§Ú§ß§Ñ§Õ§Ý§Ö§Ø§Ú§ä §Ú§Ô§â§à§Ó§à§Þ§å §á§à§Ý§ð
        False -- §Ó §á§â§à§ä§Ú§Ó§ß§à§Þ §ã§Ý§å§é§Ñ§Ö.
    """
    return (0 <= x < BOARD_SIZE) and (0 <= y < BOARD_SIZE)


def get_board_with_valid_moves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §ã§à§Ù§Õ§Ñ§Ö§ä §ß§à§Ó§à§Ö §Ó§â§Ö§Þ§Ö§ß§ß§à§Ö §Ú§Ô§â§à§Ó§à§Ö §á§à§Ý§Ö, §ß§Ñ §Ü§à§ä§à§â§à§Þ 
    §ã§Ú§Þ§Ó§à§Ý§à§Þ '.' §á§à§Þ§Ö§é§Ö§ß§í §Ü§Ý§Ö§ä§Ü§Ú §Ü§å§Õ§Ñ §Þ§à§Ø§ß§à §ã§Õ§Ö§Ý§Ñ§ä§î §ç§à§Õ.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §Ú§Ô§â§à§Ó§à§Ö §á§à§Ý§Ö.
        tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ú§Ô§â§à§Ü.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §ß§à§Ó§à§Ö §Ú§Ô§â§à§Ó§à§Ö §á§à§Ý§Ö §ã §á§à§Þ§Ö§é§Ö§ß§ß§í§Þ§Ú §Ü§Ý§Ö§ä§Ü§Ñ§Þ§Ú §Ó §Ó§Ú§Õ§Ö
        §ã§á§Ú§ã§Ü§Ñ.
    """

    dupe_board = get_board_copy(board)

    for x, y in get_valid_moves(dupe_board, tile):
        dupe_board[x][y] = '.'
    return dupe_board


def get_valid_moves(board, tile):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §Ó§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§ä §ã§á§Ú§ã§à§Ü §Ó§à§Ù§Þ§à§Ø§ß§í§ç §Õ§à§á§å§ã§ä§Ú§Þ§í§ç §ç§à§Õ§à§Ó §Õ§Ý§ñ §ä§Ö§Ü§å§ë§Ö§Ô§à
    §Ú§Ô§â§à§Ü§Ñ §ß§Ñ §ä§Ö§Ü§å§ë§Ö§Þ §ç§à§Õ§Ö.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.
        tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ú§Ô§â§à§Ü.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §ã§á§Ú§ã§à§Ü §Ü§à§à§Õ§Ú§ß§Ñ§ä §Ü§Ý§Ö§ä§à§Ü.
    """

    valid_moves = []

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])
    return valid_moves


def get_score_of_board(board):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §â§Ñ§ã§ã§é§Ú§ä§í§Ó§Ñ§Ö§ä §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§â§Ö§Õ§Ö§Ý§Ö§ß§Ú§Ö §à§é§Ü§à§Ó.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
         board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §ã§Ý§à§Ó§Ñ§â§î §ã §Ü§à§Ý§Ú§é§Ö§ã§ä§Ó§à§Þ §à§é§Ü§à§Ó §å §à§Ò§à§Ú§ç §Ú§Ô§â§à§Ü§à§Ó.
    """


    black_score, white_score = 0, 0

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == BLACK_CHIP:
                black_score += 1
            if board[x][y] == WHITE_CHIP:
                white_score += 1
    return {BLACK_CHIP:black_score, WHITE_CHIP:white_score}


def enter_player_tile():
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §á§â§Ö§Õ§Ý§Ñ§Ô§Ñ§Ö§ä §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§ð §Ó§í§Ò§â§Ñ§ä§î §æ§Ú§ê§Ü§à§Û §Ü§Ñ§Ü§à§Ô§à §è§Ó§Ö§ä§Ñ §à§Õ§ß§à§Û
    §Ò§å§Õ§Ö§ä §Ú§Ô§â§Ñ§ä§î.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §Ü§à§â§ä§Ö§Ø §Ú§Ù §Õ§Ó§å§ç §ï§Ý§Ö§Þ§Ö§ß§ä§à§Ó, §Ó §Ü§à§ä§à§â§à§Þ §ß§Ñ §á§Ö§â§Ó§à§Þ §Þ§Ö§ã§ä§Ö
    §å§Ü§Ñ§Ù§Ñ§ß§Ñ §æ§Ú§ê§Ü§Ñ §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§ñ, §Ñ §ß§Ñ §Ó§ä§à§â§à§Þ -- §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ.
    """
    
    tile = ''
    while tile not in ('§¢', '§¹'):
        tile = input('§£§í §ç§à§ä§Ú§ä§Ö §Ú§Ô§â§Ñ§ä§î [§¢]§Ö§Ý§í§Þ§Ú §Ú§Ý§Ú [§¹]§×§â§ß§í§Þ§Ú? ').upper()

    if tile.startswith('§¹'):
        return (BLACK_CHIP, WHITE_CHIP)
    else:
        return (WHITE_CHIP, BLACK_CHIP)


def who_goes_first():
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §Ó§í§Ò§Ú§â§Ñ§Ö§ä §Ü§ä§à §Õ§Ö§Ý§Ñ§Ö§ä §á§Ö§â§Ó§í§Û §ç§à§Õ.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §à§Õ§Ú§ß §Ú§Ù §ï§Ý§Ö§Þ§Ö§ß§ä§à§Ó §Ü§à§â§ä§Ö§Ø§Ñ ('§¬§à§Þ§á§î§ð§ä§Ö§â','§ª§Ô§â§à§Ü'),
    §Ó§í§Ò§â§Ñ§ß§í§Û §á§â§à§Ú§Ù§Ó§à§Ý§î§ß§í§Þ §à§Ò§â§Ñ§Ù§à§Þ.
    """

    return random.choice(('§¬§à§Þ§á§î§ð§ä§Ö§â', '§ª§Ô§â§à§Ü'))


def play_again():
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §á§â§à§Ó§Ö§â§ñ§Ö§ä §ç§à§é§Ö§ä §Ý§Ú §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§î §ã§í§Ô§â§Ñ§ä§î §Ö§ë§Ö §â§Ñ§Ù.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        True -- §Ö§ã§Ý§Ú §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§î §ç§à§é§Ö§ä §ã§í§Ô§â§Ñ§ä§î §Ö§ë§Ö §â§Ñ§Ù.
        False --  §Ó §á§â§à§ä§Ú§Ó§ß§à§Þ §ã§Ý§å§é§Ñ§Ö.
    """

    return input('§·§à§ä§Ú§ä§Ö §ã§í§Ô§â§Ñ§ä§î §Ö§ë§Ö §â§Ñ§Ù (§Õ§Ñ §Ú§Ý§Ú §ß§Ö§ä):').lower().startswith('§Õ')


def make_move(board, tile, xstart, ystart):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §ã§ä§Ñ§Ó§Ú§ä §æ§Ú§ê§Ü§å §Ú§Ô§â§à§Ü§Ñ §ß§Ñ §Ù§Ñ§Õ§Ñ§ß§ß§å§ð §Ü§Ý§Ö§ä§Ü§å §Ú §á§Ö§â§Ö§Ó§à§â§Ñ§é§Ú§Ó§Ñ§Ö§ä
    §æ§Ú§ê§Ü§Ú §á§â§à§ä§Ú§Ó§ß§Ú§Ü§Ñ.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.
        tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ú§Ô§â§à§Ü.
        xstart -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ §ä§Ö§Ü§å§ë§Ö§Ô§à §ç§à§Õ§Ñ §á§à §·.
        ystart -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ §ä§Ö§Ü§å§ë§Ö§Ô§à §ç§à§Õ§Ñ §á§à Y.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        True -- §Ö§ã§Ý§Ú §ç§à§Õ §ñ§Ó§Ý§ñ§Ö§ä§ã§ñ §Õ§à§á§å§ã§ä§Ú§Þ§í§Þ.
        False -- §Ó §á§â§à§ä§Ú§Ó§ß§à§Þ §ã§Ý§å§é§Ñ§Ö.
    """
    
    tiles_to_flip = is_valid_move(board, tile, xstart, ystart)

    if not tiles_to_flip:
        return False

    board[xstart][ystart] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile
    return True


def get_board_copy(board):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §ã§à§Ù§Õ§Ñ§Ö§ä §Ü§à§á§Ú§ð §ä§Ö§Ü§å§ë§Ö§Ô§à §Ú§Ô§â§à§Ó§Ô§à §á§à§Ý§ñ.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: §Ü§à§á§Ú§ñ §Ú§Ô§â§à§Ó§à§Ô§à §á§à§Ý§ñ §Ó §Ó§Ú§Õ§Ö §ã§á§Ú§ã§Ü§Ñ.
    """
    
    dupe_board = getNewBoard()

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            dupe_board[x][y] = board[x][y]

    return dupe_board


def is_on_corner(x, y):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §á§â§à§Ó§Ö§â§ñ§Ö§ä §ñ§Ó§Ý§ñ§Ö§ä§ã§ñ §Ý§Ú §Ü§Ý§Ö§ä§Ü§Ñ §å§Ô§Ý§à§Ó§à§Û.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        x -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ §ç §á§â§à§Ó§Ö§â§ñ§Ö§Þ§à§Û §Ü§Ý§Ö§ä§Ü§Ú.
        y -- §Ü§à§à§â§Õ§Ú§ß§Ñ§ä§Ñ y §á§â§à§Ó§Ö§â§ñ§Ö§Þ§à§Û §Ü§Ý§Ö§ä§Ü§Ú.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        True -- §Ö§ã§Ý§Ú §Ü§Ý§Ö§ä§Ü§Ñ §ñ§Ó§Ý§ñ§Ö§ä§ã§ñ §å§Ô§Ý§à§Ó§à§Û.
        False -- §Ó §á§â§à§ä§Ú§Ó§ß§à§Þ §ã§Ý§å§é§Ñ§Ö.
    """
    # return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
    return (x, y) in ((0, 0), (BOARD_SIZE - 1, 0),
                    (0, BOARD_SIZE - 1), (BOARD_SIZE - 1, BOARD_SIZE - 1))


def get_player_move(board, tile):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §á§â§Ö§Õ§Ý§Ñ§Ô§Ñ§Ö§ä §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§ð §ã§Õ§Ö§Ý§Ñ§ä§î §ç§à§Õ §Ú §à§Ò§â§Ñ§Ò§Ñ§ä§í§Ó§Ñ§Ö§ä 
    §á§à§Ý§å§é§Ö§ß§ß§í§Ö §Õ§Ñ§ß§ß§í§Ö.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.
        tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ú§Ô§â§à§Ü.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        §³§á§Ú§ã§à§Ü §Ü§à§à§Õ§Ú§ß§Ñ§ä §Ó §Ó§Ú§Õ§Ö [x, y] -- §Ö§ã§Ý§Ú §á§à§Ý§ì§Ù§à§Ó§Ñ§ä§Ö§Ý§î §ã§Õ§Ö§Ý§Ñ§Ý §ç§à§Õ.
        §³§ä§â§à§Ü§Ñ '§Ó§í§ç§à§Õ' -- §Ö§ã§Ý§Ú §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§î §ç§à§é§Ö§ä §Ó§í§Û§ä§Ú §Ú §Ó§Ó§Ö§Ý '§µ'.
        §³§ä§â§à§Ü§Ñ '§á§à§Õ§ã§Ü§Ñ§Ù§Ü§Ú' -- §Ö§ã§Ý§Ú §á§à§Ý§î§Ù§à§Ó§Ñ§ä§Ö§Ý§î §ç§à§é§Ö§ä §á§Ö§â§Ö§Ü§Ý§ð§é§Ú§ä§î §à§ä§à§Ò§â§Ñ§Ø§Ö§ß§Ú§Ö
            §á§à§Õ§ã§Ü§Ñ§Ù§à§Ü §Ú §Ó§Ó§Ö§Ý '§±'.
        """
    DIGITS = '12345678'
    CHARS = '§Ñ§Ò§Ó§Ô§Õ§Ö§Ø§Ù'

    MSG_NOT_VALID_TURN = '§£§í §ã§Õ§Ö§Ý§Ñ§Ý§Ú §ß§Ö§Ó§Ö§â§ß§í§Û §ç§à§Õ.'
    while True:
        move = input('§£§Ñ§ê §ç§à§Õ (§µ - §Ó§í§Û§ä§Ú, §± - §Ó§Ü§Ý./§Ó§í§Ü§Ý. §á§à§Õ§ã§Ü§Ñ§Ù§Ü§Ú): ').lower()
        if move.startswith('§å'):
            return '§Ó§í§ç§à§Õ'
        if move.startswith('§á'):
            return '§á§à§Õ§ã§Ü§Ñ§Ù§Ü§Ú'

        if len(move) == 2 and move[0] in CHARS and move[1] in DIGITS:
            x = CHARS.index(move[0])
            y = DIGITS.index(move[1])
            if not is_valid_move(board, tile, x, y):
                print(MSG_NOT_VALID_TURN)
                continue
            else:
                break
        else:
            print(MSG_NOT_VALID_TURN)

    return [x, y]


def get_computer_move(board, tile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §Õ§Ö§Ý§Ñ§Ö§ä §ç§à§Õ §Ù§Ñ §Ü§à§Þ§á§î§ð§ä§Ö§â.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.
        tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ü§à§Þ§á§î§ð§ä§Ö§â.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö:
        §³§á§Ú§ã§à§Ü §Ü§à§à§Õ§Ú§ß§Ñ§ä §Ó §Ó§Ú§Õ§Ö [x, y].
    """
    possible_moves = get_valid_moves(board, tile)

    random.shuffle(possible_moves)

    # §¦§ã§Ý§Ú §Ö§ã§ä§î §Ó§à§Ù§Þ§à§Ø§ß§à§ã§ä§î, §Ó§ã§Ö§Ô§Õ§Ñ §ã§ä§Ñ§Ó§Ú§ä§î §æ§Ú§ê§Ü§å §Ó §å§Ô§à§Ý §Ú§Ô§â§à§Ó§à§Ô§à §á§à§Ý§ñ.
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    # §±§â§à§Û§ä§Ú §á§à §Ó§ã§Ö§Þ§å §ã§á§Ú§ã§Ü§å §ç§à§Õ§à§Ó §Ú §Ó§í§Ò§â§Ñ§ä§î §ß§Ñ§Ú§Ò§à§Ý§Ö§Ö §â§Ö§Ù§å§Ý§î§ä§Ñ§ä§Ú§Ó§ß§í§Û.
    best_score = -1
    for x, y in possible_moves:
        dupe_board = get_board_copy(board)
        make_move(dupe_board, tile, x, y)
        score = get_score_of_board(dupe_board)[tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score
    return best_move


def show_points(board, player_tile, computer_tile):
    """§¥§Ñ§ß§ß§Ñ§ñ §æ§å§ß§Ü§è§Ú§ñ §Ó§í§Ó§à§Õ§Ú§ä §ß§Ñ §ï§Ü§â§Ñ§ß §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§â§Ö§Õ§Ö§Ý§Ö§ß§Ú§Ö §à§é§Ü§à§Ó.

    §¡§â§Ô§å§Þ§Ö§ß§ä§í:
        board -- §ä§Ö§Ü§å§ë§Ö§Ö §â§Ñ§ã§á§à§Ý§à§Ø§Ö§ß§Ú§Ö §æ§Ú§ê§Ö§Ü §ß§Ñ §Ú§Ô§â§à§Ó§à§Þ §á§à§Ý§Ö.
        player_tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ú§Ô§â§à§Ü.
        computer_tile -- §æ§Ú§ê§Ü§Ñ, §Ü§à§ä§à§â§à§Û §ç§à§Õ§Ú§ä §Ü§à§Þ§á§î§ð§ä§Ö§â.

    §£§à§Ù§Ó§â§Ñ§ë§Ñ§Ö§Þ§à§Ö §Ù§ß§Ñ§é§Ö§ß§Ú§Ö: None
    """

    tiles = {BLACK_CHIP:'(§é§×§â§ß§í§Ö)', WHITE_CHIP:'(§Ò§Ö§Ý§í§Ö)'}
    scores = get_score_of_board(board)
    print('§µ §Ó§Ñ§ã {} -- {}, §å §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ {} -- {}.'.format(tiles[player_tile],
                                                          scores[player_tile],
                                                          tiles[computer_tile],
                                                          scores[computer_tile]))

def main():
    """§°§ã§ß§à§Ó§ß§à§Û §è§Ú§Ü§Ý §á§â§à§Ô§â§Ñ§Þ§Þ§í
    """

    show_hints = False

    os.system('cls')
    print('§¥§à§Ò§â§à §á§à§Ø§Ñ§Ý§à§Ó§Ñ§ä§î §Ó §Ú§Ô§â§å §²§Ö§Ó§Ö§â§ã§Ú!')

    while True:

        main_board = getNewBoard()
        reset_board(main_board)
        player_tile, computer_tile = enter_player_tile()
        
        turn = who_goes_first()
        print(turn, '§ç§à§Õ§Ú§ä §á§Ö§â§Ó§í§Þ.')
        time.sleep(1)
        os.system('cls')

        while True:
            if turn == '§ª§Ô§â§à§Ü':
                if show_hints:
                    valid_moves_board = get_board_with_valid_moves(main_board,
                                                                   player_tile)
                    draw_board(valid_moves_board)
                else:
                    draw_board(main_board)

                show_points(main_board, player_tile, computer_tile)
                move = get_player_move(main_board, player_tile)

                if move == '§Ó§í§ç§à§Õ':
                    print('§³§á§Ñ§ã§Ú§Ò§à §Ù§Ñ §Ú§Ô§â§å!')
                    sys.exit()
                elif move == '§á§à§Õ§ã§Ü§Ñ§Ù§Ü§Ú':
                    show_hints = not show_hints
                    continue
                else:
                    make_move(main_board, player_tile, move[0], move[1])

                if get_valid_moves(main_board, computer_tile) == []:
                    break
                else:
                    turn = '§¬§à§Þ§á§î§ð§ä§Ö§â'

            else:
                # Computer's turn.
                draw_board(main_board)
                show_points(main_board, player_tile, computer_tile)
                # input('Press Enter to see the computer\'s move.')
                x, y = get_computer_move(main_board, computer_tile)
                make_move(main_board, computer_tile, x, y)

                if get_valid_moves(main_board, player_tile) == []:
                    break
                else:
                    turn = '§ª§Ô§â§à§Ü'

        # Display the final score.
        draw_board(main_board)
        scores = get_score_of_board(main_board)
        print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
        if scores[player_tile] > scores[computer_tile]:
            print('You beat the computer by %s points! Congratulations!' % (scores[player_tile] - scores[computer_tile]))
        elif scores[player_tile] < scores[computer_tile]:
            print('You lost. The computer beat you by %s points.' % (scores[computer_tile] - scores[player_tile]))
        else:
            print('The game was a tie!')

        if not play_again():
            break


if __name__ == '__main__':
    main()