class Solution:
    def maxSubarraySimpleSum(self, nums: List[int]) -> int:
        best_sum = nums[0]
        best_start = 0
        best_end = 1
        
        curr_sum = best_sum
        curr_start = best_start

        i = 0
        n = len(nums)        
        for i in range(1,n):            
            if curr_sum < 0:
                curr_sum = 0
                curr_start = i

            curr_sum += nums[i]
            if best_sum < curr_sum:
                best_sum = curr_sum
                best_start = curr_start
                best_end = i+1

        return best_sum, best_start, best_end

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            raise ValueException("empty list")


        # best of contiguous
        best_simple_sum, best_start, best_end = self.maxSubarraySimpleSum(nums)

        # best wrapped
        best_min_sum, mins_start, min_end = self.maxSubarraySimpleSum([-k for k in nums])
        
        min_sum = -best_min_sum
        total_sum = sum(nums)
        best_wrapping_sum = total_sum - min_sum

        if best_wrapping_sum == 0:
            best_wrapping_sum = max(nums)

        max_sum = max(best_simple_sum, best_wrapping_sum)
        return max_sum


        





