from typing import List

# Write any import statements here


def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    # Write your code here
    L = [l - 1 for l in L]
    depth = [-1] * N
    max_depth = -1
    for i in range(N):
        if depth[i] != -1:
            continue
        # Find cycle
        seen = set()
        order = []
        j = i
        while j not in seen and depth[j] == -1:
            order.append(j)
            seen.add(j)
            j = L[j]
        if depth[j] == -1:
            # Find Cycle length
            start, length, j = j, 1, L[j]
            while j != start:
                length += 1
                j = L[j]
            # Set Cycle depths
            depth[j] = length
            j = L[j]
            while j != start:
                depth[j] = length
                j = L[j]
        # For all visited sites set depth
        while len(order) > 0:
            j = order.pop()
            if depth[j] != -1:
                continue
            else:
                depth[j] = depth[L[j]] + 1
        max_depth = max(max_depth, depth[i])
    return max_depth


if __name__ == "__main__":
    print(getMaxVisitableWebpages(4, [4, 1, 2, 1]))
