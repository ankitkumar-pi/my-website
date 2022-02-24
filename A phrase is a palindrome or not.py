class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = (''.join(e for e in s if e.isalnum())).lower()
        s2 = s[::-1]
        return s == s2
