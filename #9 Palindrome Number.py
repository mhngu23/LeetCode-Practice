#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        this method turn the number into a string and check the reverse
        """
        self.number = str(x)
        print(x)
        reverse = self.number[::-1]
        if self.number == reverse:
            return print(True)
        else:
            return print(False)

answer = Solution()
answer.isPalindrome("-100")
