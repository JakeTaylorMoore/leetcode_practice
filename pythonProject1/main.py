#
# def longestCommonPrefix(strs: list[str]) -> str:
#     # Naive solution
#     # Set temp to first string in array
#     temp = strs[0]
#     # Set i to 1
#     i = 1
#     # While loop while i < len(array)
#     while i < len(strs):
#         # If len(temp) is 0 break
#         if len(temp) == 0:
#             break
#         # Set j to 0
#         j = 0
#         # comp_string is temp string to add confirmed matches
#         comp_string = ''
#         # While j is less than len(temp) AND less than len(array[i])
#         while j < len(temp):
#             # if comp string is longer than current string, make temp comp_string and break
#             if j == len(strs[i]):
#                 temp = comp_string
#                 i += 1
#                 break
#             # If temp[j] == array[i][j]
#             elif temp[j] == strs[i][j]:
#                 comp_string += temp[j]
#                 # j++
#                 j += 1
#             # Else chain is broken
#             else:
#                 # Set temp = comp_string and break
#                 temp = comp_string
#                 i += 1
#                 break
#     return temp


# def longestCommonPrefix(strs):
    # """
    # :type strs: List[str]
    # :rtype: str
    # """
    # if not strs:
    #     return ""
    # shortest = min(strs, key=len)
    # for i, ch in enumerate(shortest):
    #     for other in strs:
    #         if other[i] != ch:
    #             return shortest[:i]
    # return shortest

def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for count, value in enumerate(shortest):
        for other in strs:
            if other[count] != value:
                return shortest[:count]
    return shortest

arr1 = ["flower", "flow", "flight"]
arr2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(arr1))
print(longestCommonPrefix(arr2))
