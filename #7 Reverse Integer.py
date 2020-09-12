class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        self.x = str(x)
        if x>=0:
            result = self.x[::-1]
        else:
            t = str(abs(x))
            t = t[::-1]
            result = "-" + t
        if int(result) > (-2 ** 31) and int(result)  < (2 ** 31 - 1):
            return print(int(result))
        else:
            return print(0)

solution = Solution()
solution.reverse(1534236469)