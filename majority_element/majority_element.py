# Author:      Jacob Moore
# Date:        7/27/22
# Description: The majority element is the element that appears more than
#              ⌊n / 2⌋ times. You may assume that the majority element
#              always exists in the array.

#              My solution is commented out. New solution is significantly more efficient


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # import math
        # threshold = math.floor(len(nums)/2)
        # i = {}
        # for num in nums:
        #     if num not in i.keys():
        #         i[num] = 1
        #     else:
        #         i[num] += 1
        #     if i[num] > threshold:
        #         return num
        current = nums[0]
        counter = 0
        for num in nums:
            if num == current:
                counter += 1
            elif counter == 0:
                current = num
            else:
                counter -= 1
        return current


def main():
    a = Solution()
    nums = [3, 2, 3]
    print(a.majorityElement(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(a.majorityElement(nums))


if __name__ == '__main__':
    main()
