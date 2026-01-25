class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefex = [1]*n
        sufex =  [1]*n
        result = [0]*n
        
        for i in range(1,n):
            prefex[i] = prefex[i-1] * nums[i-1]

        for i in range(n-2 , -1 , -1):
            sufex[i] = sufex[i+1] * nums[i+1]
        for i in range(n):
            result[i] = sufex[i] * prefex[i]
        return result    
#####
s = Solution()
print(s.productExceptSelf([1,3,5,7]))

