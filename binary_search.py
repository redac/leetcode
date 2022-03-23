from json.tool import main
from math import floor
from typing import List


class Solution:
    def binarySearch(self, arr: List[int], target: int, start: int, end: int) -> int:
        # Base case
        if (start > end):
            return -1  # "Not found"

        middle = floor((start+end)/2)
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            self.binarySearch(arr, target, middle+1, end)
        else:
            self.binarySearch(arr, target, start, middle-1)


if __name__ == "__main__":
    a = [2, 3, 4, 6, 7, 6, 54]
    print(Solution().binarySearch(a, 6, 0, len(a)))
