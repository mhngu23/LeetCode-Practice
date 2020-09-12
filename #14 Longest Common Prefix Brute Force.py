class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # need to be common
        if len(strs) == 0:
            return ''
        current = strs[0]
        for i in range(1, len(strs)):
            temp = ''
            for j in range(len(strs[i])):
                if j < len(current) and ((strs[i])[j]) == (current[j]):  # the j< length current will prevent index out of range
                    temp += strs[i][j]
                else:
                    break
            current = temp
        return current


Leetcode14 = Solution()
Leetcode14.longestCommonPrefix(["flower", "flight", "flow", "flight"])