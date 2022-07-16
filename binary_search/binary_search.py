# Author:      Jacob Moore
# Date:        7/15/22
# Description: Binary Search #704 original work

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        half = int(len(nums)/2)
        if nums[half] == target:
            return half
        elif target > nums[half]:
            return self.searchHelper(nums, target, half, len(nums)-1)
        else:
            return self.searchHelper(nums, target, 0, half)


    def searchHelper(self, nums, target, i, j):
        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        elif i >= j:
            return -1
        half = int((j-i)/2)+i
        if nums[half] == target:
            return half
        elif target > nums[half]:
            return self.searchHelper(nums, target, half+1, j)
        else:
            return self.searchHelper(nums, target, i, half-1)


def main():
    a = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(a.search(nums, target))

    nums = [-1, 0, 5]
    target = 5
    print(a.search(nums, target))

if __name__ == "__main__":
    main()
