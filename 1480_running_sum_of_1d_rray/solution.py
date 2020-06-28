"""
cho 1 mảng. tạo một mảng mới có phần tử là tổng của các phần tử trước đó
https://leetcode.com/problems/running-sum-of-1d-array/

Sample 1:
nums = [1,2,3,4]
output = [1,3,6,10] = [1, 1+2, 1+2+3, 1+2+3+4]
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    print(nums)
    if len(nums) == 0:
        return []
    result = []
    sum_of_pre = 0
    for num in nums:
        sum_of_pre = sum_of_pre + num
        result.append(sum_of_pre)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    running_sum(nums=nums)
