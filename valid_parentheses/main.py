# Author:      Jacob Moore
# Date:        6/23/22
# Description: This program...

class Solution:
    # Use stack to solve
    def __init__(self):
        self.string_stack = []
        self.open = ['[', '{', '(']
        self.close = [']', '}', ')']
        self.type = {'(': ')', '{': '}', '[': ']'}

    # Initially append first elem of string to stack and call helper
    def isValid(self, s: str) -> bool:
        # If string is odd length, not valid
        if len(s) % 2 != 0:
            return False
        if s[0] in self.close:
            return False
        self.string_stack.append(s[0])
        new_string = s[1::]
        return self.isValidHelper(new_string)

    def isValidHelper(self, string):
        # stack is empty
        if len(self.string_stack) == 0:
            # Base case
            if len(string) == 0:
                return True
            # If stack empty but first elem of string is closed bracket, false
            elif string[0] in self.close:
                self.string_stack = []
                return False
            # # If first elem is opening paren, recursion
            elif string[0] in self.open and len(string) > 1:
                self.string_stack.append(string[0])
                new_string = string[1::]
                return self.isValidHelper(new_string)
            else:
                self.string_stack = []
                return False
        # If stack not empty but string is, false
        elif len(string) == 0:
            self.string_stack = []
            return False
        else:
            # If first elem of string closes last elem of stack, pop both and recur
            # Otherwise add to stack and recur
            if self.type[self.string_stack[-1]] == string[0]:
                new_string = string[1::]
                self.string_stack.pop()
                return self.isValidHelper(new_string)
            elif string[0] in self.close:
                self.string_stack = []
                return False
            else:
                self.string_stack.append(string[0])
                new_string = string[1::]
                return self.isValidHelper(new_string)


def main():
    t = Solution()
    s = "([)]"
    print(t.isValid(s))
    s = "()[]{}"
    print(t.isValid(s))
    s = "(]"
    print(t.isValid(s))


if __name__ == '__main__':
    main()
