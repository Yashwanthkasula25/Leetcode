class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = maxx = nums[0]
        for i in range(1,len(nums)):
            maxx = max(maxx+nums[i],nums[i])
            res = max(res,maxx)
        return res       
    

s = Solution()
print(s.maxSubArray([-1,2,3,4,-5,6,7,8,-9]))