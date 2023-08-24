# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:00:08 2023

@author: kimmy
"""
import random

board_position = 0
COMPUTER_WIN = 0
PLAYER_WIN = 1
DRAW = 2
KEEP_GOING = 3

def unpack_board(board):
    list = [0]*9
    for i in range(9):
        list[i] = board % 10
        board = int(board / 10)
   
    list.reverse()
    return list

def pack_board(l):
    board = 0
    for i in l:
        board *= 10
        board += i
       
    return board

def set_cell_by_position(board, position, state):
    l = unpack_board(board)
    l[position] = state
    board = pack_board(l)
   
    return board


def map_coord_to_position(coord):
    row_char = coord[0]
    row_coord = ord(row_char) - ord('A')
    col_char= coord[1]
    col_coord = int(col_char) - 1
    position = (3 * row_coord) + col_coord
   
    return position
   

def set_cell_by_coord(board, coord, state):
    position = map_coord_to_position(coord)
    board = set_cell_by_position(board, position, state)
   
    return board


def pretty_print(board):
    list = unpack_board(board)
    map = ['.', 'X', 'O']
    print(map[list[0]], map[list[1]], map[list[2]])
    print(map[list[3]], map[list[4]], map[list[5]])
    print(map[list[6]], map[list[7]], map[list[8]])
   

def has_more_moves(board):
    list = unpack_board(board)
    return 0 in list


def pick_random_empty_cell(board):
    list = unpack_board(board)
    count_of_zeros = list.count(0)
   
    if count_of_zeros == 0:
        raise Exception('There are no more moves')
       
    nth_zero = random.randint(1, count_of_zeros)
    number_of_zeros = 0
   
    for i in range(len(list)):
        if list[i] == 0:
            number_of_zeros += 1
            if number_of_zeros == nth_zero:
                return i
       
    return -1


def is_coord_used(board, coord):
    l = unpack_board(board)
    position = map_coord_to_position(coord)
   
    return l[position] == 0


def is_coord_valid(coord):
    if len(coord) != 2:
        return False
   
    row_range = ['A', 'B', 'C']
    col_range = ['1', '2', '3']
   
    row_char = coord[0]
    col_char= coord[1]
   
    if row_char not in row_range:
        return False
       
    if col_char not in col_range:
        return False
   
    return True
   

def is_winner(board, player):
    # top row, middle row, bottom row
    # first column, second column, third column
    # front diagonal, back diagonal
    l = unpack_board(board)
   
    # Top Row
    if l[0] == l[1] == l[2] == player:
        return True
   
    # Middle Row
    if l[3] == l[4] == l[5] == player:
        return True
   
    # Bottom Row
    if l[6] == l[7] == l[8] == player:
        return True
   
    # First Column
    if l[0] == l[3] == l[6] == player:
        return True
   
    # Second Column
    if l[1] == l[4] == l[7] == player:
        return True
   
    # Third Column
    if l[2] == l[5] == l[8] == player:
        return True
   
    # Front Diagonal
    if l[0] == l[4] == l[8] == player:
        return True
   
    # Back Diagonal
    if l[2] == l[4] == l[6] == player:
        return True
   
    return False


def play_tic_tac_toe_player(board, token):
    pretty_print(board)
   
    while True:
        coord = input('Enter Coordinates: ')
        if is_coord_valid(coord):
            if is_coord_used(board, coord):
                break
            else:
                print("Coordinate is already in use!")
        else:
            print("Coordinate is invalid!")
           
    board = set_cell_by_coord(board, coord, token)
    if is_winner(board, token):
        pretty_print(board)
        print("You've Won!")
        return PLAYER_WIN, board
       
    elif not has_more_moves(board):
        pretty_print(board)
        print("You've Tied")
        return DRAW, board
    else:
        return KEEP_GOING, board
   
   
def play_tic_tac_toe_computer(board, token):
    position = pick_random_empty_cell(board)
    board = set_cell_by_position(board, position, token)
   
    if is_winner(board, token):
        pretty_print(board)
        print("You've Lost")
        return COMPUTER_WIN, board
       
    elif not has_more_moves(board):
        pretty_print(board)
        print("You've Tied")
        return DRAW, board
    else:
        return KEEP_GOING, board
   
   
def play_tic_tac_toe(player_goes_first):
    # Human always goes first
    board = 000000000
    player_goes_next = player_goes_first
   
    while True:
        if player_goes_next:
            status, board = play_tic_tac_toe_player(board, 1)
           
            if status != KEEP_GOING:
                break
           
            player_goes_next = False
        else:
            status, board = play_tic_tac_toe_computer(board, 2)
           
            if status != KEEP_GOING:
                break
           
            player_goes_next = True
           
    return status  


def is_answer_yes(input):
    input_range = ['Yes', 'yes', 'Y', 'y']
   
    return input in input_range
           

def play_series_of_games():
    computer_wins = 0
    player_wins = 0
    draws = 0
    still_playing = True
   
    player_goes_first_answer = input("Would you like to go first? ")
    player_goes_first = is_answer_yes(player_goes_first_answer)
   
    while still_playing:
        who_won = play_tic_tac_toe(player_goes_first)
        if who_won == COMPUTER_WIN:
            computer_wins += 1
        elif who_won == PLAYER_WIN:
            player_wins += 1
        else:
            draws += 1
        print('Computer: ', computer_wins)
        print('You: ', player_wins)
        print('Draws: ', draws)
        wanna_play = input('Play Again? ')
        still_playing = is_answer_yes(wanna_play)
        player_goes_first = not player_goes_first
       

play_series_of_games()  