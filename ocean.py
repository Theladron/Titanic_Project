import random
import copy
import time
from os import system, name


def create_ocean(boardsize):
    '''creates the board via joining two lists'''
    board = []
    for row in range(boardsize):
        row_matrix = []
        for col in range(boardsize):
            if col < boardsize-1:
                if random.randrange(0,10) <= 3:
                    row_matrix.append("\U0001F9CA")

                else:
                    row_matrix.append("\U0001F7E6")
            else:
                row_matrix.append("\U0001F7E6") # Wasser-Symbol
        board.append(row_matrix)
    return board

def set_titanic(board):
    '''sets the titanic randomly on a field in the last row'''
    ship_placement = [random.randrange(0, len(board) - 1), len(board) - 1]  # cornercase
    board[ship_placement[0]][ship_placement[1]] = "\U0001F6A2"
    return board, ship_placement

def create_blacklist(board):
    '''creates a blacklist via deepcopy'''
    return copy.deepcopy(board)

def ocean_validity(blacklist):
    '''checks if the map is solvable'''
    possible_starts = []    # List for all the different starting points (starting points are points where same colums in row 1+2 are free
    for row in range(len(blacklist)):
        if blacklist[row][0] == "\U0001F7E6" and blacklist[row][1] == "\U0001F7E6":
           possible_starts.append([row, 1])
           blacklist[row][0] = "\U0001F7E2" #Grüner Kreis
           blacklist[row][1] = "\U0001F7E2"
        if not possible_starts:
           return blacklist, False, 0, 0

    while True:
        for location in possible_starts:
            starting_point = copy.deepcopy(location)    # starting point in case it is the one we want to start the autopilot from
            right_path, blacklist, solution = find_path(blacklist, location)
            if right_path:
               return blacklist, True, starting_point, solution
        return blacklist, False, 0, 0

def is_crossroad(blacklist, position):
    '''checks if a position has multiple ways to go'''
    counter = 0
    if position[1] != 0 and blacklist[position[0]][position[1] - 1] == "\U0001F7E6":
       counter += 1
    if position[1] != len(blacklist) - 1 and blacklist[position[0]][position[1] + 1] == "\U0001F7E6":
       counter += 1
    if position[0] != 0 and blacklist[position[0] - 1][position[1]] == "\U0001F7E6":
       counter += 1
    if position[0] != len(blacklist) - 1 and blacklist[position[0] + 1][position[1]] == "\U0001F7E6":
       counter += 1
    return counter > 1


def find_path(blacklist, position):
    '''checks the path from the input starting position, returns the blacklist and bool arg for right path'''
    path = [] # lists all the positions with multiple ways to go
    path_length = []
    solution = []
    while True:
        next_pos = next_position(blacklist, position)
        if not next_pos:
               if not path:
                  return False, blacklist, 0
               else:
                    position = path.pop()     # position at the last known crossroad
                    solution = solution[0:path_length.pop() + 1]

        else:
               if is_crossroad(blacklist, position):
                  path.append(copy.deepcopy(position))
                  path_length.append(len(solution))

               blacklist[position[0]][position[1]] = "\U0001F7E2"
               solution.append(copy.deepcopy(position))
               position = next_pos
        time.sleep(1)               # for blacklist,visualisation
        visualize_board(blacklist)  # put both lines in quotes to stop blacklist visualisation
        if position[1] == len(blacklist) - 1:
           return True, blacklist, solution


def next_position(blacklist, cur_pos):
    '''returns the next valid position, false if no valid position'''
    if cur_pos[1] != len(blacklist) - 1 and blacklist[cur_pos[0]][cur_pos[1] + 1] == "\U0001F7E6":
       cur_pos[1] += 1
       return cur_pos
    elif cur_pos[0] != 0 and blacklist[cur_pos[0] - 1][cur_pos[1]] == "\U0001F7E6":
       cur_pos[0] -= 1
       return cur_pos
    elif cur_pos[0] != len(blacklist) - 1 and blacklist[cur_pos[0] + 1][cur_pos[1]] == "\U0001F7E6":
       cur_pos[0] += 1
       return cur_pos
    elif cur_pos[1] != 0 and blacklist[cur_pos[0]][cur_pos[1] - 1] == "\U0001F7E6":
       cur_pos[1] -= 1
       return cur_pos
    else:
       return []



def get_auto_pilot(start, solution):
    ''' creates a list with directions for the ship, orientates on marked paths from the blacklist'''
    autopilot = ["WEST"]
    while True:
        position = solution[0]
        if start[1] + 1 == position[1]:
           autopilot.append("WEST")
           start[1] += 1
        elif start[0] - 1 == position[0]:
           autopilot.append("SOUTH")
           start[0] -= 1
        elif start[0] + 1 == position[0]:
           autopilot.append("NORTH")
           start[0] += 1
        elif start[1] - 1 == position[0]:
           autopilot.append("EAST")
           start[1] -= 1
        starting_point = solution.pop(0)
        if not solution:
           return autopilot, starting_point


def visualize_board(board):
    '''prints out the current status of the board'''
    clear()
    for row in range(len(board)):
        for col in range(len(board)):
            print(board[row][col], end=" ")
        print("")

def clear():
    '''clears the terminal for a smoother look on visual board updates'''
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')