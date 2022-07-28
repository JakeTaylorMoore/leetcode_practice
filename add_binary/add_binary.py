# Author:      Jacob Moore
# Date:        7/27/22
# Description: Leetcode problem 67. Completed following Neetcode tutorial:
#              https://www.youtube.com/watch?v=keuWJ47xG8g&ab_channel=NeetCode


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res



def main():
    a = Solution()
    c = "11"
    b = "1"
    print(a.addBinary(c, b))

    c = "1010"
    b = "1011"
    print(a.addBinary(c, b))


if __name__ == '__main__':
    main()
