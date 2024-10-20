class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        longest_pre = strs[0]
        for i in range(1,len(strs)):
            while(strs[i].find(longest_pre)!=0):
                longest_pre = longest_pre[:-1]
                if len(longest_pre) == 0: return ""
        return longest_pre