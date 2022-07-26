# Author:      Jacob Moore
# Date:        7/26/22
# Description: Leetcode # 409 Longest Palindrome


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        j = {}
        for k in range(len(alpha)):
            j[alpha[k]] = 0
        for i in range(len(s)):
            j[s[i]] += 1
        tracker = 0
        one_odd = 0
        for l in j.keys():
            if j[l] % 2 == 0:
                tracker += j[l]
            elif one_odd == 0:
                one_odd += 1
                tracker += j[l]
            else:
                tracker += (j[l] - 1)
        return tracker



def main():
    a = Solution()
    print(a.longestPalindrome('abccccdd'))
    print(a.longestPalindrome('a'))


if __name__ == "__main__":
    main()