# Author:      Jacob Moore
# Date:        7/25/22
# Description: Uses leetcode API and cannot be tested from own IDE

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, i=0):
        """
        :type n: int
        :rtype: int
        """
        x = int(n/2)




def main():
    a = Solution()
    print(a.firstBadVersion(5))
    print(a.firstBadVersion(1))



if __name__ == "__main__":
    main()