class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        m = 0
        for i in range(len(t)):
            if m <= len(s)-1:
                if s[m] == t[i]:
                    m += 1
        return m == len(s)