def conatinsDuplicate(nums):
    # myList = []
    # for i in range(len(nums)):
    #     if nums[i] not in myList:
    #         myList.append(nums[i])
    #         print(myList)
    #     else:
    #         return True
    # return False
    mySet = set(nums)
    if len(nums) != len(mySet):
        return True
    else:
        return False


print(conatinsDuplicate([1, 2, 3, 1]))
