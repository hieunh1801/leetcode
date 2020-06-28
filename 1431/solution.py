"""
Greatest Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""
from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    if len(candies) == 0:
        return
    max_candies = candies[0]
    for candy in candies:
        if max_candies < candy:
            max_candies = candy
    result = []
    for val in candies:
        result.append(max_candies <= val + extra_candies)
    return result


if __name__ == '__main__':
    candies = [4, 2, 1, 1, 2]
    extra_candies = 1
    kids_with_candies(candies, extra_candies)
