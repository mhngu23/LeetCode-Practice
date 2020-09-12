class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #if len(s) < 1 or len(s) > 10^4 or any(c not in '()[]{}' for c in s):
            #print('False')
        temp = []
        for para in s:
            if para == "(" or para == "[" or para == "{":
                temp.append(para)
            elif temp and para == ")" and temp[-1] == "(":
                temp.pop()
            elif temp and para == "]" and temp[-1] == "[":
                temp.pop()
            elif temp and para == "}" and temp[-1] == "{":
                temp.pop()
            else:
                return False
        if temp == []:
            return True
ValidParentheses = Solution()
ValidParentheses.isValid("()}}}")
# ValidParentheses.isValid("()[]{}")
# ValidParentheses.isValid("(]")
# ValidParentheses.isValid("(]")
# ValidParentheses.isValid("{[]}")