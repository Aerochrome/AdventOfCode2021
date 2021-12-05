filepath = "input.txt"

with open(filepath) as file:
    splits = file.read().split("\n\n")

drawn_numbers = [int(i) for i in splits[0].split(',')]
bingo_strings = splits[1:]
bingo_boards = []

for bingo_str in bingo_strings:
    bingo_board = []
    bingo_row_strings = [i.lstrip() for i in bingo_str.split("\n")]

    for row_str in bingo_row_strings:
        bingo_board.append([{'value': int(i), 'checked': False} for i in row_str.split()])

    bingo_boards.append(bingo_board)


def check_bingo(board):
    rows = [0, 0, 0, 0, 0]
    columns = [0, 0, 0, 0, 0]

    for i, brow in enumerate(board):
        for j, bnum in enumerate(brow):
            if bnum['checked']:
                rows[i] += 1
                columns[i] += 1

                if rows[i] == 5:
                    return True
                elif columns[i] == 5:
                    return True
    return False


def calc_result(board, just_called):
    sum_unmarked = 0
    for row in board:
        for num in row:
            if not num['checked']:
                sum_unmarked += num['value']

    return sum_unmarked*just_called


def draw_nums():
    for draw_num in drawn_numbers:
        for board in bingo_boards:
            for row in board:
                for num in row:
                    if num['value'] == draw_num:
                        num['checked'] = True

            if check_bingo(board):
                print("Board won!", board)
                print('Result', calc_result(board, draw_num))
                return


draw_nums()
