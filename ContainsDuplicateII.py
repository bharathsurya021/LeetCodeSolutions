def containsDuplicate(nums, k):
    mydict = {}
    for i in range(len(nums)):
        if nums[i] in mydict and abs(i - mydict[nums[i]]) <= k:
            return True
        mydict[nums[i]] = i
    return False


print(containsDuplicate([1, 2, 3, 1, 2, 3], 2))
