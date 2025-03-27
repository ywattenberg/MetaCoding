# test.py
from typing import List
from collections import deque, defaultdict

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    if S == 0.0:
        return sum(V) - C
    elif S == 1.0:
        relS = [s for s in S if s > C]
        return sum(relS) - len(relS) * C

    ns = 1 - S

    value_cache = [[0] * (N) for i in range(N)]
    value_cache[0][0]=V[0]
    for i in range(1,N):
        value_cache[0][i] = value_cache[0][i-1] * ns + V[i]




    ev = [[0] * (N) for i in range(N)]
    ev[0][0] = V[0]
    for i in range(1, N):
        ev[0][i] = ev[0][i - 1] * ns + V[i]

    for i in range(1, N):
        ev[i][i - 1] = ev[i - 1][i - 1] - C
        # ev[i][i] = ev[i - 1][i] + V[i] - C
        for j in range(i, N):
            ev[i][j] = max(ev[i - 1][j] + V[j] - C, ev[i - 1][j] * ns + V[j])

    for i in range(N):
        print(ev[i])


def getSecondsRequired(R: int, C: int, G: List[List[str]]):

    stack = deque()
    portal_loc = {}
    for i in range(R):
        for j in range(C):
            if 96 < ord(G[i][j]) and ord(G[i][j]) < 123:

            if G[i][j] == "S":
                stack.append((i,j,0))

    while len(stack) > 0:
        i,j,time = stack.pop()
        if G[i][j] == "E":
            return time
        else:

if __name__ == "__main__":

    getMaxExpectedProfit(5, [10, 2, 8, 6, 4], 3, 0.5)
