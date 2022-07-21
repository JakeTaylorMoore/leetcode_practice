# Author:      Jacob Moore
# Date:        7/20/22
# Description: With help from this site https://medium.com/the-research-nest/solving-the-maximum-subarray-sum-a-super-simplified-explanation-34042ffd3fd7


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempSum = nums[0]
        maxSum = tempSum
        i = 1
        while i < len(nums):
            tempSum = max(nums[i], tempSum+nums[i])
            maxSum = max(maxSum, tempSum)
            i += 1
        return maxSum


def main():
    a = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(a.maxSubArray(nums))
    nums = [1]
    print(a.maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(a.maxSubArray(nums))


if __name__ == "__main__":
    main()
