# Brute Force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]


# Better
def twoSum2(nums, target):
    compSet = {}
    for i in range(len(nums)):
        compSet[nums[i]] = i
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in compSet and compSet[comp] != i:
            return [i, compSet[comp]]


print(twoSum([2, 7, 11, 5], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print('better:')
print(twoSum2([2, 7, 11, 5], 9))
print(twoSum2([3, 2, 4, 4], 8))
print(twoSum2([3, 3], 6))
print(twoSum2([3, 2, 5], 6))
