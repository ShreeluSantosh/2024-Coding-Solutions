class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        L = s.split()
        M = L[::-1]
        s = " ".join(M)
        return s