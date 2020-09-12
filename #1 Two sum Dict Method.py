class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        self.nums = nums
        self.target = target
        for i in range(len(self.nums)):
            result = self.target - self.nums[i]
            if result in dict.keys():
                secondIndex = self.nums.index(result)
                return print(sorted([i,secondIndex]))
            dict.update({self.nums[i]:i})
solution = Solution()
solution.twoSum([3,3], 6)