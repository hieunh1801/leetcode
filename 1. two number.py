

def two_sum(nums: list, target: int) -> list:
    len_nums = len(nums)
    if len_nums <= 1:
        return False
    buff_dict = dict()
    for i in range(len_nums):
        val = nums[i]
        if val in buff_dict:
            return [buff_dict[val], i]
        else:
            sub = target - val
            buff_dict[sub] = i


nums = [3, 4, 6, 7, 8, 9, 2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("result: ", result)
