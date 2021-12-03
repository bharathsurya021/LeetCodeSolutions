class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowIndex = 0
        highIndex = len(nums) - 1
        # base case
        while lowIndex <= highIndex:
            mid = (lowIndex + highIndex) // 2
            # check if element present at mid
            if nums[mid] == target:
                return mid
            # check element in left subarray
            elif nums[mid] > target:
                highIndex = mid - 1
            # check element in left subarray
            else:
                lowIndex = mid + 1
        return -1