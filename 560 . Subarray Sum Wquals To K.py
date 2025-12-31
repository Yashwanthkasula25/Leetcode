class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i , len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1
        return count
s = Solution()
s.subarraySum([1,2,3] , 3)                    




class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr_sum = 0
        prefix_sum = {0: 1}  # prefix sum 0 occurs once initially

        for num in nums:
            curr_sum += num

            # If (curr_sum - k) exists, then there is a subarray ending here that sums to k
            if (curr_sum - k) in prefix_sum:
                count += prefix_sum[curr_sum - k]

            # Store or update the count of the current prefix sum
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return count


# Example run
s = Solution()
print(s.subarraySum([1, 2, 3], 3))
