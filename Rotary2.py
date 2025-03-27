from typing import List

def getMiniCodeEntry(N:int, M:int, C:List[int])->int:
    s,p = 0,0
    for i in C:
        s += min(abs(p - (i-1)), abs(p - (i - 1 + N)), abs(p - (i - 1 - N)))
        p = i - 1



if __name__ == "__main__":
    getMiniCodeEntry()
