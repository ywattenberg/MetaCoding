from typing import List


def getMinProblemCount(N: int, S: List[int]):
    largest = max(S)
    if all([s % 2 == 0 for s in S]):
        return largest // 2
    threes = largest // 3
    rest = largest % 3
    seen = [rest] if rest else []
    for i in S:
        if len(seen) == 2:
            break
        r = i % 3
        if r and r not in seen:
            seen.append(r)

    return threes + len(seen)


if __name__ == "__main__":
    print(getMinProblemCount(5, [1, 2, 3, 4, 5]))
    print(getMinProblemCount(4, [4, 3, 3, 4]))
    print(getMinProblemCount(4, [2, 4, 6, 8]))
    print(getMinProblemCount(1, [8]))
