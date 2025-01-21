import ocean
import time


def show_autopilot(board, direction_list, ship, starting_point):
    '''moves the ship along the board'''
    ocean.visualize_board(board)
    time.sleep(1)
    while ship[0] != starting_point[0]:     # loop until the ship is on the starting position of the autopilot list
        if ship[0] < starting_point[0]:
           board[ship[0]][ship[1]] = "\U0001F7E6"
           board[ship[0] + 1][ship[1]] = "\U0001F6A2"
           ship[0] += 1
        elif ship[0] > starting_point[0]:
           board[ship[0]][ship[1]] = "\U0001F7E6"
           board[ship[0] - 1][ship[1]] = "\U0001F6A2"
           ship[0] -= 1
        else:
            break

        time.sleep(1)
        ocean.visualize_board(board)

    direction_list.reverse()
    for direction in direction_list:
        ocean.visualize_board(board)
        time.sleep(0.6)
        match direction:                                    # oriented on the masterschool exercise
            case "WEST":
                board[ship[0]][ship[1]] = "\U0001F7E6"
                board[ship[0]][ship[1] - 1] = "\U0001F6A2"
                ship[1] -= 1
            case "SOUTH":
                board[ship[0]][ship[1]] = "\U0001F7E6"
                board[ship[0] + 1][ship[1]] = "\U0001F6A2"
                ship[0] += 1
            case "EAST":
                board[ship[0]][ship[1]] = "\U0001F7E6"
                board[ship[0]][ship[1] + 1] = "\U0001F6A2"
                ship[1] += 1
            case "NORTH":
                board[ship[0]][ship[1]] = "\U0001F7E6"
                board[ship[0] - 1][ship[1]] = "\U0001F6A2"
                ship[0] -= 1

    ocean.visualize_board(board)
    time.sleep(1)
    print("\nThe Titanic has savely reached it's destination")
    time.sleep(2)
