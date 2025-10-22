import numpy as np

# CONSTANTS
# board size (minimum board size is 6 for closed)
BOARD_SIZE = 6

# board area
BOARD_AREA = BOARD_SIZE * BOARD_SIZE

# target step count
TARGET_STEPS = BOARD_AREA + 1

def KnightsTour():
    should_outer_loop = True

    print("Welcome to the Knights Tour by Liam Mills.")

    while should_outer_loop:
        print("Which type would you like to use?")
        tour_type = input("For backtracking, type 1. For Las Vegas, type 2. To exit, type 3: ")

        if tour_type not in ["1", "2", "3"]:
            print("Error: you entered an incorrect option. The program will retry this step.\n")
        elif tour_type in ["1", "2"]:
            should_inner_loop = True

            while should_inner_loop:
                coordinates = input("\nPlease enter the row and column of the starting square, i.e. 0,0: ")
                coordinates_arr = coordinates.split(",")

                if len(coordinates_arr) != 2:
                    print("Error: you entered an incorrect option. The program will retry this step.\n")
                    continue
                else:
                    try:
                        row = int(coordinates_arr[0])
                        col = int(coordinates_arr[1])
                    except:
                        print("Error: you entered an incorrect option. The program will retry this step.\n")
                        continue

                    should_inner_loop = False

                    if tour_type == "1":
                        (bool, arr) = KnightsTourBacktracking((row, col))
                    else:
                        (bool, arr) = KnightsTourLasVegas((row, col))
                    
                    message = "success" if bool else "failure"

                    print(f"\nYour run was a {message}.")
                    KnightsTourPrintBoard(arr)

            print("Your tour has finished, the program will return to the main menu.\n")

        else:
            should_outer_loop = False
            break

    print("Thank you for using the Knights Tour by Liam Mills, goodbye!")

def KnightsTourBacktracking(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    # row and col coordinates from user defined starting postion
    (start_row, start_col) = startingPosition

    # array of possible moves the knight can take
    # the knight can move in an L shape of 1 square along
    # then 2 at a right angle from the first
    possible_moves = [
        (-1, -2),
        (-2, -1),
        (1, -2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (1, 2),
        (2, 1),
    ]

    # positions to process, a queue to process next steps,
    # or if that fails, then the previous step
    # initialised with starting position
    #
    # row = row value of current position
    # col = col value of the current position
    # step_count = step count of the element, used to mark the board,
    # and judge if the loop has got to the end
    # next_step_index = used as an index for the possible_moves arr,
    # to get the position of the next move
    # 
    positions_to_process = [{
        'row': start_row,
        'col': start_col,
        'step_count': 1,
        'next_step_index': 0
    }]

    # positions to return, an array to store the order of the steps
    # to output at the end of the function
    position_order = [[start_row, start_col]]

    while len(positions_to_process):
        # get current postion data fomr the last element in
        # the positions_to_process array
        current_row = positions_to_process[0]['row']
        current_col = positions_to_process[0]['col']
        step_count = positions_to_process[0]['step_count']
        next_step_index = positions_to_process[0]['next_step_index']
        
        # if set_count equals target steps
        # we are at the end point
        if step_count == TARGET_STEPS:
            # exit while if it hasn't already
            break
        
        # if current neighbour index is below the size of
        # possible_moved array, then there are possible moves
        # to take
        if next_step_index < len(possible_moves):
            # get next possible move
            (add_row, add_col) = possible_moves[next_step_index]
            # create new coordinates by adding the move values
            # with the current row and y values
            new_row = current_row + add_row
            new_col = current_col + add_col

            # up the current elements next_step_index incase we need
            # to backtrack
            positions_to_process[0]['next_step_index'] += 1
            
            # if the new row and col coordinates are possible moves
            # and the coordinate on the board is zero
            # OR, the tour is at the last step, and that it is going back to the 
            # first spot
            if (new_row >= 0 and new_col >= 0 and new_row < BOARD_SIZE and new_col < BOARD_SIZE and [new_row,new_col] not in position_order) or (step_count == BOARD_AREA and new_row == start_row and new_col == start_col):
                # add this element to the positions_to_process to start
                # looking through moves from there
                positions_to_process.insert(0, {
                    'row': new_row,
                    'col': new_col,
                    'step_count': step_count + 1,
                    'next_step_index': 0
                })
                # add the new coordinates to the position_order array
                position_order.append([new_row, new_col])
        else:
            # else, the next_step_index is equal to the len of 
            # possible_moves array, so there are no moves left to make
            # the current item is not working so we need to backtrack
            # remove this item from positions_to_process
            removed = positions_to_process.pop(0)

            # remove from position_order
            position_order.remove([removed['row'], removed['col']])

    # return tuple of:
    # boolean: if the length of position_order equal the TARGET_STEPS
    # list[list[int]]: the order in which we toured the board
    return (len(position_order) == TARGET_STEPS, position_order)
    
def KnightsTourLasVegas(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    # row and col coordinates from user defined starting postion
    (start_row, start_col) = startingPosition

    # array of possible moves the knight can take
    # the knight can move in an L shape of 1 square along
    # then 2 at a right angle from the first
    possible_moves = [
        (-1, -2),
        (-2, -1),
        (1, -2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (1, 2),
        (2, 1),
    ]

    # positions to process, a queue to process next steps,
    # or if that fails, then the previous step
    # initialised with starting position
    #
    # row = row value of current position
    # col = col value of the current position
    # step_count = step count of the element, used to mark the board,
    # and judge if the loop has got to the end
    # 
    positions_to_process = [{
        'row': start_row,
        'col': start_col,
        'step_count': 1
    }]

    # positions to return, an array to store the order of the steps
    # to output at the end of the function
    position_order = [[start_row, start_col]]

    # attempt array for each step
    attempted_positions = []

    while len(positions_to_process):
        # get current postion data fomr the last element in
        # the positions_to_process array
        current_row = positions_to_process[0]['row']
        current_col = positions_to_process[0]['col']
        step_count = positions_to_process[0]['step_count']
        
        # if set_count equals target steps
        # or the items has been attempted in all child options
        # we are at the end point
        if step_count == TARGET_STEPS or len(attempted_positions) == 8:
            # exit while if it hasn't already
            break
        
        # set variables for the next attempt 
        # addition variable loop
        loop_for_next_attempt = True
        add_row = 0
        add_col = 0

        while loop_for_next_attempt:
            # randomly get the index for the possible moves array
            index = np.random.randint(0, 8, 1)[0]
            (row, col) = possible_moves[index]

            # if these coordinates have not already been attempted
            # set vars, else retry
            if (index not in attempted_positions):
                add_row = row
                add_col = col
                attempted_positions.append(index)
                loop_for_next_attempt = False

        # create new coordinates by adding the move values
        # with the current row and y values
        new_row = current_row + add_row
        new_col = current_col + add_col
        
        # if the new row and col coordinates are possible moves
        # and the coordinate on the board is zero
        # OR, the tour is at the last step, and that it is going back to the 
        # first spot
        if (new_row >= 0 and new_col >= 0 and new_row < BOARD_SIZE and new_col < BOARD_SIZE and [new_row,new_col] not in position_order) or (step_count == BOARD_AREA and new_row == start_row and new_col == start_col):
            # add this element to the positions_to_process to start
            # looking through moves from there
            positions_to_process.insert(0, {
                'row': new_row,
                'col': new_col,
                'step_count': step_count + 1
            })
            # add the new coordinates to the position_order array
            position_order.append([new_row, new_col])
            # empty attempted_positions for next position to process
            attempted_positions = []

    # return tuple of:
    # boolean: if the length of position_order equal the TARGET_STEPS
    # list[list[int]]: the order in which we toured the board
    return (len(position_order) == TARGET_STEPS, position_order)

def KnightsTourPrintBoard(visited: list[list[int]]) -> None:
    # define board of zeros, set all to 0
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

    # loop termination number
    terminator = len(visited) - 1 if TARGET_STEPS == len(visited) else len(visited)

    for i in range(0, terminator):
        # get the row and column value
        (row, col) = visited[i]

        # place it on the board
        board[row][col] = i + 1

    # print final board
    print(f"Your final board layout was: \n{board}\n")

    return

# print(KnightsTourLasVegas((2,2)))
KnightsTour()