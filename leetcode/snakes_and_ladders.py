from typing import List, Tuple
from collections import deque


class Solution:
    def get_row_col(self, i: int) -> Tuple[int, int]:
        row = int(i / self.col)
        return row, i - row

    def get_idx(self, i: int, j: int) -> int:
        return i * self.col + j

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Build graph where each node is connected with it's 6 previous tiles
        iff. board[r][c] == -1 (not snake or ladder)
        if board[r][c] != -1 connect to relevant tile
        Then use bfs to calculate number of moves (equal to depth of bfs level)
        """
        r, c = len(board), len(board[0])
        self.col = c
        board = board[::-1]
        for i in range(r):
            if i % 2 == 1:
                board[i] = board[i][::-1]

        queue = deque([(0, 0)])
        visited = [False] * (r * c)
        while queue:
            curr, step = queue.popleft()
            if visited[curr]:
                continue
            visited[curr] = True
            i, j = self.get_row_col(curr)
            if curr == c * r - 1 or board[i][j] == c * r - 1:
                return step
            if board[i][j] == -1:
                queue += [
                    (k, step + 1) for k in range(curr + 1, min(c * r - 1, curr + 7))
                ]
            else:
                queue += [
                    (k, step + 1)
                    for k in range(board[i][j] + 1, min(c * r - 1, board[i][j] + 7))
                ]

        return 0
