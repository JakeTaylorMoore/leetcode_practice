# Author:      Jacob Moore
# Date:        7/15/22
# Description: I wrote this program for the valid anagram leetcode problem # 242

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        while s:
            char = s[0]
            s = s[1::]
            found = t.find(char)
            if found == -1:
                return False
            t = t.replace(char, "", 1)
        if t:
            return False
        else:
            return True


def main():
    a = Solution()
    s = "anagram"
    t = "nagaram"
    print(a.isAnagram(s, t))

    s = "rat"
    t = "car"
    print(a.isAnagram(s, t))


if __name__ == "__main__":
    main()
