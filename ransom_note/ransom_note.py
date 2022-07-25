# Author:      Jacob Moore
# Date:        7/25/22
# Description: This program is my solution to leetcode question #383 "ransom Note"

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        table = {}
        i = 0
        while i < len(alphabet):
            table[alphabet[i]] = 0
            i += 1

        i = 0
        while i < len(magazine):
            table[magazine[i].lower()] += 1
            i += 1

        i = 0
        while i < len(ransomNote):
            letter = ransomNote[i].lower()
            if table[letter] > 0:
                table[letter] -= 1
            else:
                return False
            i += 1
        return True



def main():
    a = Solution()
    ransomNote = "a"
    magazine = "b"
    print(a.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "ab"
    print(a.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "aab"
    print(a.canConstruct(ransomNote, magazine))


if __name__ == "__main__":
    main()