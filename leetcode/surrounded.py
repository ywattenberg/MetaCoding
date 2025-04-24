from typing import List, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # If a 0 region does not touch the border it is surrounded
        # can search trhough with dfs
        # how to propergate info?
        # easy from all boarder start dfs if cell is 0 mark as clean
        # then second step all left over islands are surrounded

        stack: List[Tuple[int, int]] = []
        for i in range(len(board)):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][-1] == 'O':
                stack.append((i, len(board[0]) - 1))
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                stack.append((0, j))
            if board[-1][j] == 'O':
                stack.append((len(board) - 1, j))
        while len(stack) > 0:
            x, y = stack.pop()
            if board[x][y] != 'O':
                continue
            board[x][y] = 's'
            if x > 0:
                stack.append((x - 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if x < len(board) - 1:
                stack.append((x + 1, y))
            if y < len(board[0]) - 1:
                stack.append((x, y + 1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 's':
                    board[i][j] = 'O'
