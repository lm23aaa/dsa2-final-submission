import numpy as np

def KnightsTourBacktracking(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    # board size
    board_size = 5

    # target step count
    target_steps = board_size * board_size

    # row and col coordinates from user defined starting postion
    (start_row, start_col) = startingPosition

    # define board of zeros, set all to 0, with the initial
    # step set to one
    board = np.zeros((board_size, board_size))
    board[start_row][start_col] = 1

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
        current_row = positions_to_process[-1]['row']
        current_col = positions_to_process[-1]['col']
        step_count = positions_to_process[-1]['step_count']
        next_step_index = positions_to_process[-1]['next_step_index']
        
        # if set_count equals target steps
        # we are at the end point
        if step_count == target_steps:
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
            positions_to_process[-1]['next_step_index'] += 1
            
            # if the new row and col coordinates are possible moves
            # and the coordinate on the board is zero
            if new_row >= 0 and new_col >= 0 and new_row < board_size and new_col < board_size and board[new_row][new_col] == 0:
                # up the space on the board with the step count
                board[new_row][new_col] = step_count + 1
                # add this element to the positions_to_process to start
                # looking through moves from there
                positions_to_process.append({
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
            removed = positions_to_process.pop()

            # remove this from the board
            board[removed['row']][removed['col']] = 0

            # remove from position_order
            position_order.remove([removed['row'], removed['col']])

    # print final board
    print(board)

    # if the non zeros in the board and the length of position_order
    # eaual the target_steps
    if np.count_nonzero(board) == target_steps and len(position_order) == target_steps:
        # return the success boolean and position_order array
        return (True, position_order)
    else:
        # else, return failure results
        return (False, [[-1]])

# print(KnightsTourBacktracking((0,0)))