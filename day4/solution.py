with open('input.txt', 'rt') as f:
    lines = f.read().split('\n')

    picks = [int(i) for i in lines[0].split(',')]
    
    boards = []
    board = []
    idx = 2
    while idx < len(lines):
        if lines[idx] == '':
            boards.append(board)
            board = []
        else:
            board.append([int(i.strip()) for i in lines[idx].split(' ') if i != ''])
        idx += 1
    boards.append(board)

    def is_row_complete(board, r_idx, picked):
        for c in range(len(board[r_idx])):
            if board[r_idx][c] not in picked:
                return False
        return True
    
    def is_col_complete(board, c_idx, picked):
        for r in range(len(board)):
            if board[r][c_idx] not in picked:
                return False
        return True

    def bingo(board, picked, latest):
        sum_ = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] not in picked:
                    sum_ += board[r][c]
        return sum_ * latest

    def part1(boards, picks):
        picked = set()
        for pick in picks:
            picked.add(pick)
            for board in boards:
                for r_idx in range(len(board)):
                    if is_row_complete(board, r_idx, picked):
            
                        return bingo(board, picked, pick)
                for c_idx in range(len(board[0])):
                    if is_col_complete(board, c_idx, picked):
            
                        return bingo(board, picked, pick)

    def part2(boards, picks):
        picked = set()
        winners = set()
        last = None
        for pick in picks:
            picked.add(pick)
            for b_idx in range(len(boards)):
                if b_idx in winners:
                    continue
                board = boards[b_idx]
                for r_idx in range(len(board)):
                    if is_row_complete(board, r_idx, picked):
                        winners.add(b_idx)
                        last = b_idx
                for c_idx in range(len(board[0])):
                    if is_col_complete(board, c_idx, picked):
                        winners.add(b_idx)
                        last = b_idx
            if len(winners) == len(boards):
                return bingo(boards[last], picked, pick)
print(f"Part1: {part1(boards, picks)}")
print(f"Part2: {part2(boards, picks)}")