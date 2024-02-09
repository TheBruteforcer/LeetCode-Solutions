class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0 
        chars = {}
        maxlnght = 0
        for end in range(len(s)):
            if s[end] in chars and chars[s[end]] >= start:
                start = chars[s[end]] + 1
            chars[s[end]] = end
            maxlnght = max(maxlnght, end - start + 1)
        return maxlnght

print(Solution.longestPalindrome(Solution, 'abcabcd'))