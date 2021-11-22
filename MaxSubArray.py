# Brute  O(n^2)
def maxSumSubArray(nums):
    maxSum = -1e8
    for i in range(len(nums)):
        currsum = 0
        for j in range(i, len(nums)):
            currsum = currsum + nums[j]
            if currsum > maxSum:
                maxSum = currsum
    return maxSum


# Better kadane's algorithm O(n)
def maxSumSubArray1(nums):
    currentSum = 0
    maxSumSoFar = nums[0]
    for i in range(len(nums)):
        currentSum += nums[i]
        if currentSum > maxSumSoFar:
            maxSumSoFar = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSumSoFar


print(maxSumSubArray([5, 4, -1, 7, 8]))
print(maxSumSubArray1([5, 4, -1, 7, 8]))
