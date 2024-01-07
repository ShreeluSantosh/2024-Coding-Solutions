class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        def valid(k):
            if n1 % k or n2 % k:
                return False
            m1,m2 = n1//k, n2//k
            base = str1[:k]
            return str1 == m1 * base and str2 == m2 * base
        for i in range(min(n1,n2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""