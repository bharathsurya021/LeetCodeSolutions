# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lowIndex = 1
        highIndex = n
        result = n
        while lowIndex <= highIndex:
            mid = (lowIndex + highIndex) // 2
            if isBadVersion(mid):
                result = mid
                highIndex = mid - 1
            else:
                lowIndex = mid + 1
        return result