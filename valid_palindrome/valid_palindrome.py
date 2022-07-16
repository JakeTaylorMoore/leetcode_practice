# Author:      Jacob Moore
# Date:        7/13/22
# Description: My solution for valid palindrome leetcode #125

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        return self.isPalindromeHelper(s.lower(), i, j)

    def isPalindromeHelper(self, s, i, j, alpha="abcdefghijklmnopqrstuvwxyz0123456789"):
        if i >= j:
            return True
        elif s[i] not in alpha:
            return self.isPalindromeHelper(s, i+1, j)
        elif s[j] not in alpha:
            return self.isPalindromeHelper(s, i, j-1)
        elif s[i] == s[j]:
            return self.isPalindromeHelper(s, i+1, j-1)
        else:
            return False


def main():
    a = Solution()
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))
    s = "race a car"
    print(a.isPalindrome(s))
    s = " "
    print(a.isPalindrome(s))


if __name__ == "__main__":
    main()
