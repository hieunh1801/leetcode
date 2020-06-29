"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""
from typing import List


def s1(nums: List[int]) -> List[int]:
    """ s1: lặp 2 vòng thôi
    """
    len_nums = len(nums)
    if len_nums == 0:
        return
    result = []
    for val1 in nums:
        total_num_less_than_val1 = 0
        for val2 in nums:
            if val1 > val2:
                total_num_less_than_val1 += 1
        result.append(total_num_less_than_val1)
    return result


if __name__ == '__main__':
    nums = [6, 5, 4, 8]
    print(s1(nums))
