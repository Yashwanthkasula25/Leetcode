class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = sum(nums[:k])
        maxsum = curr
        for i in range(k,len(nums)):
            
            curr += nums[i] - nums[i - k]
            maxsum = max(maxsum , curr)
        result = float(maxsum)/k
        return result
s = Solution()
s.findMaxAverage([1,12,-5,-6,50,3] , 4)  
