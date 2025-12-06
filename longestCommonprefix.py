#keetcode-14
# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         if not strs:
#             return ""
        
#         prefix = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
        
#         return prefix
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
# class Solution():
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         pref = strs[0]
#         pref_len = len(pref)
#         for s in strs[1:]:
#             # print('pref before:', pref)
#             # print('s:', s[:pref_len])
#             while pref != s[:pref_len]:
#                 pref_len -= 1
#                 if pref_len == 0:
#                     return ""  
#                 pref = pref[:pref_len]
#             # print('pref after:', pref)
#         return pref
if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(["flower","flow","flight"]))  # Output : "fl"