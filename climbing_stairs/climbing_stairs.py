# Author:      Jacob Moore
# Date:        7/26/22
# Description: Solution for leetcode # 70 climbing stairs


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Bottom up dynamic programming
        # Base case: 0 stairs = 1 option
        #            1 stairs = 1 option
        dp = []
        dp.append(1)
        dp.append(1)
        i = 2
        while i < n+1:
            dp.append(dp[i-1] + dp[i-2])
            i += 1
        return dp[n]

def main():
    a = Solution()
    print(a.climbStairs(2))
    print(a.climbStairs(3))
    print(a.climbStairs(4))
    print(a.climbStairs(5))
    print(a.climbStairs(6))


if __name__ == "__main__":
    main()