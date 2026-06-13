class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''
        for c in s:
            if c.isalnum():
                newStr+=c
        return newStr.lower()[::] == newStr.lower()[::-1]
