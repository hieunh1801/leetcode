"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.

Input: num = 8
Output: 4

Input: num = 123
Output: 12
"""


def number_of_steps(num: int) -> int:
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps = steps + 1
    return steps


def number_of_steps2(num: int) -> int:
    """viết gọn hơn sử dụng ternary operator"""
    steps = 0
    while num != 0:
        num = num / 2 if num % 2 == 0 else num - 1
        steps = steps + 1
    return steps


def number_of_steps3(num: int) -> int:
    """
    sử dụng đệ quy recursive
    case: điều kiện dừng
    case: trả về cái gì sau mỗi lần lặp
        -> chính là cái ta quan tâm: ở đây là số bước lặp. số bước lặp = số bước lặp cũ + 1
    """

    if num == 0:
        return 0
    if num % 2 == 0:
        return 1 + number_of_steps3(num / 2)
    else:
        return 1 + number_of_steps3(num - 1)


if __name__ == '__main__':
    num = 123
    print(number_of_steps3(num))
