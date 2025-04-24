from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_cc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '1':
                    continue
                num_cc += 1
                print(i, j)
                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()
                    if grid[x][y] != '1':
                        continue
                    grid[x][y] = 'v'
                    if x > 0:
                        stack.append((x - 1, y))
                    if y > 0:
                        stack.append((x, y - 1))
                    if x < len(grid) - 1:
                        stack.append((x + 1, y))
                    if y < len(grid[0]) - 1:
                        stack.append((x, y + 1))
            print(grid[i])

        return num_cc
