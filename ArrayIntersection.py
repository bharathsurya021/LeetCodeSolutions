def arrayIntersection(nums1, nums2):
    myMap = {}
    for num in nums1:
        if num not in myMap:
            myMap[num] = 1
        else:
            myMap[num] += 1
    intersectList = []
    for num in nums2:
        if num in myMap and myMap[num] != 0:
            myMap[num] -= 1
            intersectList.append(num)
    return intersectList


print(arrayIntersection([1, 4, 5, 3, 6], [2, 3, 5, 7, 9]))
