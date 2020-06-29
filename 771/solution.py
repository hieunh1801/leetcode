"""
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Input: J = "aA", S = "aAAbbbb"
Output: 3

Input: J = "z", S = "ZZ"
Output: 0

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


def s1(J: str, S: str) -> int:
    """ solution1: kiểm tra xem mỗi hòn đá trong S có phải kim cương ko.
    """
    total_jewels_founded = 0
    for stone in S:
        if stone in J:
            total_jewels_founded += 1
    return total_jewels_founded


def s2(J: str, S: str) -> int:
    """ solution2: đệ quy thử phát nào
    - điểm dừng
    - trả về cái gì nhỉ
    """
    len_s = len(S)
    if len_s == 0:
        return 0  # return số lượng của kim cương
    if S[0] in J:
        return 1 + s2(J, S[1: len_s])  # số lượng kim cương + 1 nếu thấy
    else:
        return s2(J, S[1: len_s])  # số lượng kim cương + 0  nếu không thấy


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(s2(J, S))
