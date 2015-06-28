import os
import sys
import time
import random

BOARD_SIZE = 8
BLACK_CHIP = '��'
WHITE_CHIP = '��'


def draw_board(board):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� �ӧ�ӧ�էڧ� �ߧ� ��ܧ�ѧ� �ڧԧ��ӧ�� ���ݧ� �� ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ֧�
    ��ڧ�֧�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: None.
    """

    HLINE = '   ���������੤�����੤�����੤�����੤�����੤�����੤�����੤������'

    os.system('cls')

    print('     ��   ��   ��   ��   ��   ��   ��   ��') 
    print('   ���������Щ������Щ������Щ������Щ������Щ������Щ������Щ�������')

    for y in range(BOARD_SIZE):
        print('', y + 1 , end=' ')

        for x in range(BOARD_SIZE):
            print('�� {}'.format(board[x][y]), end=' ')
        print('��')

        if y != BOARD_SIZE - 1:
            print(HLINE)

    print('   ���������ة������ة������ة������ة������ة������ة������ة�������')


def reset_board(board):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� �����֧��ӧݧ�֧� �ߧѧ�ѧݧ�ߧ�� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧�.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: None
    """

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            board[x][y] = ' '

    board[3][3] = BLACK_CHIP
    board[3][4] = WHITE_CHIP
    board[4][3] = WHITE_CHIP
    board[4][4] = BLACK_CHIP


def getNewBoard():
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ���٧էѧ֧� ������� �ڧԧ��ӧ�� ���ݧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: �էӧ�ާ֧�ߧ�� ���ڧ��� "�ܧݧ֧���" �ڧԧ��ӧ�ԧ� ���ݧ�.
    """
    
    board = []
    for i in range(BOARD_SIZE):
        board.append([' '] * BOARD_SIZE)

    return board


def is_valid_move(board, tile, xstart, ystart):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ����ӧ֧��֧� ���ѧӧڧݧ�ߧ���� ��է֧ݧѧߧߧ�ԧ� ���է�.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.
        tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ڧԧ���.
        xstart -- �ܧ���էڧߧѧ�� ��֧ܧ��֧ԧ� ���է� ��� ��.
        ystart -- �ܧ���էڧߧѧ�� ��֧ܧ��֧ԧ� ���է� ��� Y.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        False -- �� ��ݧ��ѧ�, �֧�ݧ� �ڧԧ��� ����ѧ֧��� �����ѧӧڧ�� ��ڧ�ܧ� �ߧ� �٧ѧߧ���� �ܧݧ֧�ܧ�
            �ڧݧ� �٧� ���֧է֧ݧ� �ڧԧ��ӧ�ԧ� ���ݧ�, �ݧڧҧ� �է֧ݧѧ֧� ����, �ܧ������ �ߧ� ���٧ӧ�ݧڧ�
            �֧ާ� ��֧�֧ӧ֧�ߧ��� ��ڧ�ܧ� �����ڧӧߧڧܧ�.
        
        ������

        ����ڧ��� �ܧ���էڧߧѧ� ��ڧ�֧� �����ڧӧߧڧܧ�, �ܧ������ �ڧԧ��� �ާ�ا֧� ��֧�֧ӧ֧�ߧ��� ���ڧ� 
        ���է��.
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

    board[xstart][ystart] = ' ' # ����ڧ�ѧ֧� ���٧ڧ�ڧ� ����ӧ֧��֧ާ�ԧ� ���է�

    if len(tiles_to_flip) == 0: # ����ݧ� �ߧ� ��էѧݧ��� ��֧�֧ӧ֧�ߧ��� �ߧ� ��էߧ�� ��ڧ�ܧ�
        return False            # �����ڧӧߧڧܧ� -- �ӧ�٧ӧ�ѧ�ѧ֧� False
        
    return tiles_to_flip


def is_on_board(x, y):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ����ӧ֧��֧� ���ڧߧѧէݧ֧اߧ���� �٧ѧէѧߧߧ�� �ܧݧ֧�ܧ� �ڧԧ��ӧ�ާ� ���ݧ�.

    ����ԧ�ާ֧ߧ��:
        x -- �ܧ���էڧߧѧ�� �� ����ӧ֧��֧ާ�� �ܧݧ֧�ܧ�.
        y -- �ܧ���էڧߧѧ�� y ����ӧ֧��֧ާ�� �ܧݧ֧�ܧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        True -- �֧�ݧ� �ܧݧ֧�ܧ� ���ڧߧѧէݧ֧اڧ� �ڧԧ��ӧ�ާ� ���ݧ�
        False -- �� �����ڧӧߧ�� ��ݧ��ѧ�.
    """
    return (0 <= x < BOARD_SIZE) and (0 <= y < BOARD_SIZE)


def get_board_with_valid_moves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ���٧էѧ֧� �ߧ�ӧ�� �ӧ�֧ާ֧ߧߧ�� �ڧԧ��ӧ�� ���ݧ�, �ߧ� �ܧ������ 
    ��ڧާӧ�ݧ�� '.' ���ާ֧�֧ߧ� �ܧݧ֧�ܧ� �ܧ�է� �ާ�اߧ� ��է֧ݧѧ�� ����.

    ����ԧ�ާ֧ߧ��:
        board -- �ڧԧ��ӧ�� ���ݧ�.
        tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ڧԧ���.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: �ߧ�ӧ�� �ڧԧ��ӧ�� ���ݧ� �� ���ާ֧�֧ߧߧ�ާ� �ܧݧ֧�ܧѧާ� �� �ӧڧէ�
        ���ڧ�ܧ�.
    """

    dupe_board = get_board_copy(board)

    for x, y in get_valid_moves(dupe_board, tile):
        dupe_board[x][y] = '.'
    return dupe_board


def get_valid_moves(board, tile):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� �ӧ�٧ӧ�ѧ�ѧ֧� ���ڧ��� �ӧ�٧ާ�اߧ�� �է�����ڧާ�� ���է�� �էݧ� ��֧ܧ��֧ԧ�
    �ڧԧ��ܧ� �ߧ� ��֧ܧ��֧� ���է�.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.
        tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ڧԧ���.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: ���ڧ��� �ܧ��էڧߧѧ� �ܧݧ֧���.
    """

    valid_moves = []

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])
    return valid_moves


def get_score_of_board(board):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ��ѧ���ڧ��ӧѧ֧� ��֧ܧ��֧� ��ѧ���֧է֧ݧ֧ߧڧ� ���ܧ��.

    ����ԧ�ާ֧ߧ��:
         board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: ��ݧ�ӧѧ�� �� �ܧ�ݧڧ�֧��ӧ�� ���ܧ�� �� ��ҧ�ڧ� �ڧԧ��ܧ��.
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
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ���֧էݧѧԧѧ֧� ���ݧ�٧�ӧѧ�֧ݧ� �ӧ�ҧ�ѧ�� ��ڧ�ܧ�� �ܧѧܧ�ԧ� ��ӧ֧�� ��էߧ��
    �ҧ�է֧� �ڧԧ�ѧ��.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: �ܧ���֧� �ڧ� �էӧ�� ��ݧ֧ާ֧ߧ���, �� �ܧ������ �ߧ� ��֧�ӧ�� �ާ֧���
    ��ܧѧ٧ѧߧ� ��ڧ�ܧ� ���ݧ�٧�ӧѧ�֧ݧ�, �� �ߧ� �ӧ����� -- �ܧ�ާ����֧��.
    """
    
    tile = ''
    while tile not in ('��', '��'):
        tile = input('���� ����ڧ�� �ڧԧ�ѧ�� [��]�֧ݧ�ާ� �ڧݧ� [��]�ק�ߧ�ާ�? ').upper()

    if tile.startswith('��'):
        return (BLACK_CHIP, WHITE_CHIP)
    else:
        return (WHITE_CHIP, BLACK_CHIP)


def who_goes_first():
    """���ѧߧߧѧ� ���ߧܧ�ڧ� �ӧ�ҧڧ�ѧ֧� �ܧ�� �է֧ݧѧ֧� ��֧�ӧ�� ����.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: ��էڧ� �ڧ� ��ݧ֧ާ֧ߧ��� �ܧ���֧ا� ('����ާ����֧�','���ԧ���'),
    �ӧ�ҧ�ѧߧ�� ����ڧ٧ӧ�ݧ�ߧ�� ��ҧ�ѧ٧��.
    """

    return random.choice(('����ާ����֧�', '���ԧ���'))


def play_again():
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ����ӧ֧��֧� ����֧� �ݧ� ���ݧ�٧�ӧѧ�֧ݧ� ���ԧ�ѧ�� �֧�� ��ѧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        True -- �֧�ݧ� ���ݧ�٧�ӧѧ�֧ݧ� ����֧� ���ԧ�ѧ�� �֧�� ��ѧ�.
        False --  �� �����ڧӧߧ�� ��ݧ��ѧ�.
    """

    return input('�����ڧ�� ���ԧ�ѧ�� �֧�� ��ѧ� (�է� �ڧݧ� �ߧ֧�):').lower().startswith('��')


def make_move(board, tile, xstart, ystart):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ���ѧӧڧ� ��ڧ�ܧ� �ڧԧ��ܧ� �ߧ� �٧ѧէѧߧߧ�� �ܧݧ֧�ܧ� �� ��֧�֧ӧ��ѧ�ڧӧѧ֧�
    ��ڧ�ܧ� �����ڧӧߧڧܧ�.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.
        tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ڧԧ���.
        xstart -- �ܧ���էڧߧѧ�� ��֧ܧ��֧ԧ� ���է� ��� ��.
        ystart -- �ܧ���էڧߧѧ�� ��֧ܧ��֧ԧ� ���է� ��� Y.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        True -- �֧�ݧ� ���� ��ӧݧ�֧��� �է�����ڧާ��.
        False -- �� �����ڧӧߧ�� ��ݧ��ѧ�.
    """
    
    tiles_to_flip = is_valid_move(board, tile, xstart, ystart)

    if not tiles_to_flip:
        return False

    board[xstart][ystart] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile
    return True


def get_board_copy(board):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ���٧էѧ֧� �ܧ��ڧ� ��֧ܧ��֧ԧ� �ڧԧ��ӧԧ� ���ݧ�.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: �ܧ��ڧ� �ڧԧ��ӧ�ԧ� ���ݧ� �� �ӧڧէ� ���ڧ�ܧ�.
    """
    
    dupe_board = getNewBoard()

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            dupe_board[x][y] = board[x][y]

    return dupe_board


def is_on_corner(x, y):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ����ӧ֧��֧� ��ӧݧ�֧��� �ݧ� �ܧݧ֧�ܧ� ��ԧݧ�ӧ��.

    ����ԧ�ާ֧ߧ��:
        x -- �ܧ���էڧߧѧ�� �� ����ӧ֧��֧ާ�� �ܧݧ֧�ܧ�.
        y -- �ܧ���էڧߧѧ�� y ����ӧ֧��֧ާ�� �ܧݧ֧�ܧ�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        True -- �֧�ݧ� �ܧݧ֧�ܧ� ��ӧݧ�֧��� ��ԧݧ�ӧ��.
        False -- �� �����ڧӧߧ�� ��ݧ��ѧ�.
    """
    # return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
    return (x, y) in ((0, 0), (BOARD_SIZE - 1, 0),
                    (0, BOARD_SIZE - 1), (BOARD_SIZE - 1, BOARD_SIZE - 1))


def get_player_move(board, tile):
    """���ѧߧߧѧ� ���ߧܧ�ڧ� ���֧էݧѧԧѧ֧� ���ݧ�٧�ӧѧ�֧ݧ� ��է֧ݧѧ�� ���� �� ��ҧ�ѧҧѧ��ӧѧ֧� 
    ���ݧ��֧ߧߧ�� �էѧߧߧ��.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.
        tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ڧԧ���.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        ����ڧ��� �ܧ��էڧߧѧ� �� �ӧڧէ� [x, y] -- �֧�ݧ� ���ݧ�٧�ӧѧ�֧ݧ� ��է֧ݧѧ� ����.
        ������ܧ� '�ӧ����' -- �֧�ݧ� ���ݧ�٧�ӧѧ�֧ݧ� ����֧� �ӧ�ۧ�� �� �ӧӧ֧� '��'.
        ������ܧ� '���է�ܧѧ٧ܧ�' -- �֧�ݧ� ���ݧ�٧�ӧѧ�֧ݧ� ����֧� ��֧�֧ܧݧ��ڧ�� ����ҧ�ѧا֧ߧڧ�
            ���է�ܧѧ٧�� �� �ӧӧ֧� '��'.
        """
    DIGITS = '12345678'
    CHARS = '�ѧҧӧԧէ֧ا�'

    MSG_NOT_VALID_TURN = '���� ��է֧ݧѧݧ� �ߧ֧ӧ֧�ߧ�� ����.'
    while True:
        move = input('���ѧ� ���� (�� - �ӧ�ۧ��, �� - �ӧܧ�./�ӧ�ܧ�. ���է�ܧѧ٧ܧ�): ').lower()
        if move.startswith('��'):
            return '�ӧ����'
        if move.startswith('��'):
            return '���է�ܧѧ٧ܧ�'

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
    """���ѧߧߧѧ� ���ߧܧ�ڧ� �է֧ݧѧ֧� ���� �٧� �ܧ�ާ����֧�.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.
        tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ܧ�ާ����֧�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�:
        ����ڧ��� �ܧ��էڧߧѧ� �� �ӧڧէ� [x, y].
    """
    possible_moves = get_valid_moves(board, tile)

    random.shuffle(possible_moves)

    # ����ݧ� �֧��� �ӧ�٧ާ�اߧ����, �ӧ�֧ԧէ� ���ѧӧڧ�� ��ڧ�ܧ� �� ��ԧ�� �ڧԧ��ӧ�ԧ� ���ݧ�.
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    # �����ۧ�� ��� �ӧ�֧ާ� ���ڧ�ܧ� ���է�� �� �ӧ�ҧ�ѧ�� �ߧѧڧҧ�ݧ֧� ��֧٧�ݧ��ѧ�ڧӧߧ��.
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
    """���ѧߧߧѧ� ���ߧܧ�ڧ� �ӧ�ӧ�էڧ� �ߧ� ��ܧ�ѧ� ��֧ܧ��֧� ��ѧ���֧է֧ݧ֧ߧڧ� ���ܧ��.

    ����ԧ�ާ֧ߧ��:
        board -- ��֧ܧ��֧� ��ѧ���ݧ�ا֧ߧڧ� ��ڧ�֧� �ߧ� �ڧԧ��ӧ�� ���ݧ�.
        player_tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ڧԧ���.
        computer_tile -- ��ڧ�ܧ�, �ܧ������ ���էڧ� �ܧ�ާ����֧�.

    ����٧ӧ�ѧ�ѧ֧ާ�� �٧ߧѧ�֧ߧڧ�: None
    """

    tiles = {BLACK_CHIP:'(��ק�ߧ��)', WHITE_CHIP:'(�ҧ֧ݧ��)'}
    scores = get_score_of_board(board)
    print('�� �ӧѧ� {} -- {}, �� �ܧ�ާ����֧�� {} -- {}.'.format(tiles[player_tile],
                                                          scores[player_tile],
                                                          tiles[computer_tile],
                                                          scores[computer_tile]))

def main():
    """����ߧ�ӧߧ�� ��ڧܧ� ����ԧ�ѧާާ�
    """

    show_hints = False

    os.system('cls')
    print('����ҧ�� ���اѧݧ�ӧѧ�� �� �ڧԧ�� ���֧ӧ֧���!')

    while True:

        main_board = getNewBoard()
        reset_board(main_board)
        player_tile, computer_tile = enter_player_tile()
        
        turn = who_goes_first()
        print(turn, '���էڧ� ��֧�ӧ��.')
        time.sleep(1)
        os.system('cls')

        while True:
            if turn == '���ԧ���':
                if show_hints:
                    valid_moves_board = get_board_with_valid_moves(main_board,
                                                                   player_tile)
                    draw_board(valid_moves_board)
                else:
                    draw_board(main_board)

                show_points(main_board, player_tile, computer_tile)
                move = get_player_move(main_board, player_tile)

                if move == '�ӧ����':
                    print('����ѧ�ڧҧ� �٧� �ڧԧ��!')
                    sys.exit()
                elif move == '���է�ܧѧ٧ܧ�':
                    show_hints = not show_hints
                    continue
                else:
                    make_move(main_board, player_tile, move[0], move[1])

                if get_valid_moves(main_board, computer_tile) == []:
                    break
                else:
                    turn = '����ާ����֧�'

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
                    turn = '���ԧ���'

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