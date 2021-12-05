def moveZeroes(nums):
    temp = []
    for i in range(len(nums)):
        if nums[i] == 0:
            pass
        else:
            temp.append(nums[i])
    for i in range(len(nums)):
        if nums[i] != 0:
            pass
        else:
            temp.append(nums[i])
    return temp


def moveZeroes1(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    print(i)
    while i < len(nums):
        nums[i] = 0
        i += 1
    return nums


print(moveZeroes1([0, 1, 0, 3, 12]))
