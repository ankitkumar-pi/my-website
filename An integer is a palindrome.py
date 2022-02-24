class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        """
        x = str(x)
        x2 = x[::-1]
        return x == x2
