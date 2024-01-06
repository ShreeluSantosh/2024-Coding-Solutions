class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ""
        for i in range(n):
            res += word1[i] + word2[i]
        if len(word1) > len(word2):
            m = len(word1)
            res += word1[n:]
        else:
            res += word2[n:]
        return res