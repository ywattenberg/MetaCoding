from typing import List

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res: List[List[int]] = []
        comb :List[int] = []

        def backtrack(start:int):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num+1)
                comb.pop()
            return

        backtrack(1)
        return res


        
