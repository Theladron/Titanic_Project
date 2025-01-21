import ocean
import ship

def main():
    while True:
        try:
            boardsize = int(input("How big do you want the board to be?: "))
        except ValueError:
            print("Please input a positive, whole number over 4")
        else:
            if boardsize < 5:
                print("Please input a positive, whole number over 4")
            else:
                break

    ocean.clear()
    board_validity = False
    while not board_validity:       # loops until a valid map is found
        board = ocean.create_ocean(boardsize)
        blacklist = ocean.create_blacklist(board)
        board, ship_placement = ocean.set_titanic(board)
        blacklist, board_validity, start, solution = ocean.ocean_validity(blacklist)

    autopilot, start_point = ocean.get_auto_pilot(start, solution)
    ship.show_autopilot(board, autopilot, ship_placement, start_point)

if __name__ == "__main__":
    main()