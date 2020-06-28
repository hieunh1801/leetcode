def xor_operation(n: int, start: int) -> int:
    stop = n * 2 + start
    arr = [number for number in range(start, stop, 2)]
    xor_result = 0
    for i in arr:
        xor_result = xor_result ^ i
    return xor_result


if __name__ == '__main__':
    n = 4
    start = 3
    print(xor_operation(n, start))

