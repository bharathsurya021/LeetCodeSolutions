def matrixReshape(nums, r, c):
    tempMat = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            tempMat.append(nums[i][j])
    if r * c == len(tempMat):
        reshaped = []
        index = 0
        for i in range(r):
            reshaped.append([])
            for j in range(c):
                reshaped[i].append(tempMat[index])
                index += 1
        return reshaped
    else:
        return nums


print(matrixReshape([[1, 2], [4, 5], [7, 8]], 2, 3))
