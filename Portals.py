
from typing import List
from collections import deque, defaultdict

def getSecondsRequired(R: int, C: int, G: List[List[str]]):

    stack = deque()
    portal_loc = defaultdict(lambda: [])
    for i in range(R):
        for j in range(C):
            if 96 < ord(G[i][j]) and ord(G[i][j]) < 123:
               portal_loc[G[i][j]].append((i,j)) 
            elif G[i][j] == "S":
                stack.append((i,j,0))

    while len(stack) > 0:
        i,j,time = stack.pop()
        if G[i][j] == "E":
            return time
        elif G[i][j] == -1:
            continue
        else:
            if 96 < ord(G[i][j]) and ord(G[i][j]) < 123:
                locs = portal_loc[G[i][j]]
                # Add all portal locals
                [stack.appendleft((*loc,time+1)) for loc in locs if loc != (i,j)]
            # Add all steps 
            if i+1 < R and G[i+1][j] != "#":
                stack.appendleft((i+1,j,time+1))
            if i-1 > 0 and G[i-1][j] != "#":
                stack.appendleft((i-1,j,time+1))
            if j+1 < C and G[i][j+1] != "#":
                stack.appendleft((i,j+1,time+1))
            if j-1 > 0 and G[i][j-1] != "#":
                stack.appendleft((i,j-1,time+1))
            G[i][j] = -1
    return -1




if __name__ == "__main__":

