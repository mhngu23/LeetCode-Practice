class Solution(object):
    def isValid(self, s):
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]: #look up the last item in stack in the bracket_map
                stack.pop()
            else:
                print(False)
        if stack == []:
            print(True)
ValidParentheses = Solution()
ValidParentheses.isValid("()}}}")
#ValidParentheses.isValid("()[]{}")
#ValidParentheses.isValid("(]")
#ValidParentheses.isValid("(]")
#ValidParentheses.isValid("{[]}")