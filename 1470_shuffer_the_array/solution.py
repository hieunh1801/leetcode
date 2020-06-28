"""
Give array nums have 2n elements
nums: [x1,x2,...,xn,y1,y2,...,yn]
output: [x1,y1,x2,y2,...,xn,yn] => suffered
"""
from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    if len(nums) == 0:
        return []

    arr1 = nums[:n]
    arr2 = nums[n:]
    result = []
    for i in range(n):
        result.extend([arr1[i], arr2[i]])
    return result


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    shuffle(nums=nums, n=n)
