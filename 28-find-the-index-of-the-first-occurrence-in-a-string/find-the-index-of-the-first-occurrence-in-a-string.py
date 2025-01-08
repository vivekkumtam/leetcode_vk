class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = haystack
        b = needle

        if b in a :
            return a.index(b)
        
        else:
            return -1