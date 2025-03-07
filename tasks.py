from typing import List


def solve(n: int, nums: List[int]) -> int:
    nums.remove(max(nums))
    return max(nums)


n = 5
nums = [1, 5, 2, 3, 4]
# nums = [3, 5, 5, 2, 2, 3]
print(solve(n, nums))
