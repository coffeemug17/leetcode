class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # We will use the two pointer method for this
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)