from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dict to store visited numbers
        for i, value in enumerate(nums):
           remaining = target - nums[i]  # remaining number to reach the target
           
           if remaining in seen: # solution is found
               return [seen[remaining], i]
           else:
               seen[value] = i

if __name__ == "__main__":
    print(Solution().twoSum([23,3,2,44], 46))