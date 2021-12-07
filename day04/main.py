# https://adventofcode.com/2021/day/4

from typing import NamedTuple

class Input(NamedTuple):
    numbers: list[int]
    boards: list[list[list[int]]]

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            data = f.read().split("\n")
        numbers = list(map(int, data.pop(0).split(",")))
        data.pop(0) # there is a space between the numbers and boards >:(
        
        boards = []
        while True:
            board = []
            while True:
                if len(data) == 0:
                    break
                row = data.pop(0)
                if row == "":
                    break
                else:
                    board.append(list(map(int, (i for i in row.split(" ") if i))))
            boards.append(board)
            
            if len(data) == 0:
                break
        return cls(numbers=numbers, boards=boards)

test_input = Input.from_file("test-input")
input = Input.from_file("input")

def part1(input):
    for number in input.numbers:
        for board in input.boards:
            for index in range(len(board)):
                try:
                    board[index] = [board[index][n] if i != number else None for n, i in enumerate(board[index])]
                except ValueError:
                    pass
                    
                if len([item for item in board[index] if item is not None]) == 0 or all(board[i][index] is None for i in range(5)):
                    return sum(sum(item for item in row if item is not None) for row in board) * number

print("[part 1] test input", part1(test_input))
print("[part 1] actual input", part1(input))

def part2(input):
    for number in input.numbers:
        for n, board in enumerate(input.boards):
            if board is None:
                continue
            
            for index in range(len(board)):
                try:
                    board[index] = [board[index][n] if i != number else None for n, i in enumerate(board[index])]
                except ValueError:
                    pass
                    
                if len([item for item in board[index] if item is not None]) == 0 or all(board[i][index] is None for i in range(5)):
                    if not len([b for b in input.boards if b is not None]) == 1:
                        input.boards[n] = None
                    else:
                        return sum(sum(item for item in row if item is not None) for row in board) * number

print("[part 2] test input", part2(test_input))
print("[part 2] actual input", part2(input))
