"""
https://leetcode.com/problems/two-sum/
Bài toán:
    - input:
        - cho một dãy số nhiều phần tử
        - target: tổng của hai số trong dãy
    - output:
        - mảng gồm chỉ số của 2 phần tử
    - sample:
        - input: ([2, 7, 11, 15], 9) => output: [0, 1]
"""
from typing import List


def solution1(nums: List[int], target: int) -> List[int]:
    """
    cho 2 vòng lặp => bao giờ tổng của 2 số = target thì in ra
    runtime: 6052 ms
    """
    # case 1: mảng ko đủ phần tử để dùng
    if len(nums) < 2:
        return
    nums_len = len(nums)
    # case 2:
    for i in range(0, nums_len):
        for j in range(i + 1, nums_len):
            # print(nums[i], " ", nums[j])
            if nums[i] + nums[j] == target:
                return [i, j]
    # print(nums)
    # print(target)


def solution2(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        return
    buff_dict = dict()
    for index, num in enumerate(nums):
        buff_dict[target - num] = index
    for index, num in enumerate(nums):
        if (num in buff_dict) and (buff_dict[num] != index):
            return [index, buff_dict[num]]


def solution3(nums: List[int], target: int) -> List[int]:
    """
    - với mỗi số ta lưu lại sub của nó và index của số đó vào buffer_dict
        buffer_dict[sub, index]
         + sub = target - num
         + index = chỉ số của phần tử đó
    - loop qua tung phan tu:
        + nếu phần tử đó tồn tại trong buff_dict:
            => tìm được hiệu rồi => return
        + nếu không thì lưu lại sub và index của phần tử đó rồi loop tiếp
    """
    if len(nums) < 2:
        return

    buff_dict: dict = dict()

    for index, num in enumerate(nums):
        if num in buff_dict:
            return [buff_dict[num], index]
        else:
            buff_dict[target - num] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    # result = solution1(nums=nums, target=target)
    result = solution2(nums=nums, target=target)
    print(result)
