def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        temp = numbers[i] + numbers[j]
        if temp < target:
            i += 1
        elif temp > target:
            j -= 1
        else:
            break
    return i + 1, j + 1


print(twoSum([0, 0, 3, 4], 0))
