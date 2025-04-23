from typing import List
import bisect


class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        nums.sort()
        n = len(nums)
        best = float('inf')
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if abs(curr - target) < abs(best):
                    best = curr
                if curr > target:
                    right -= 1
                elif curr < target:
                    left -= 1
                else:
                    return target
        return best

    def letterCombinations(self, digits: List[str]) -> List[str]:
        mapping = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        if len(digits) == 0:
            return []
        results = ['']
        for digit in digits:
            curr: List[str] = []
            map = mapping[int(digit)]
            for res in results:
                for c in map:
                    curr.append(res + c)
            results = curr
        return results

    def fourSum(self, nums: List[int], target: int):
        nums.sort()
        results = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[j] == nums[j - 1]:
                    continue
                n, m = j + 1, len(nums) - 1
                while n < m:
                    curr = [nums[i], nums[j], nums[n], nums[m]]
                    scurr = sum(curr)
                    if scurr > target:
                        m -= 1
                    elif scurr < target:
                        n += 1
                    else:
                        results.append(curr)
                        n += 1
                        m -= 1
                        while nums[n - 1] == nums[n]:
                            n += 1
                        while m + 1 == len(nums) or nums[m] == nums[m + 1]:
                            m -= 1
        return results


if __name__ == '__main__':
    sol = Solution()
    input = [-2, -1, 0, 0, 1, 2, 3]
    target = 0
    print(sol.fourSum(input, target))
