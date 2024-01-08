class Solution:
    def reverseVowels(self, s: str) -> str:
        w = list(s)
        i = 0
        j = len(s) - 1
        vowels = "aeiouAEIOU"
        while i < j:
            while i < j and vowels.find(w[i]) == -1:
                i += 1
            while i < j and vowels.find(w[j]) == -1:
                j -= 1
            w[i], w[j] = w[j], w[i]
            i += 1
            j -= 1
        return "".join(w)