class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # naive solution.
        # nb its all positives.
        # nb we do not know the optimal length.
        # approach #1. start growing the array right until we exceed the sum.
        # then try to reduce the array size from the left.keep track of start.
        # approach #2. start with the full array and pull L/R pointers
            # unlikely to work: a single large entry could mislead.
            # need to track a candidate, and then continue?
        # approach #3. find largest and then grow it?
        if len(nums) == 0:
            return 0

        L = 0
        curr_sum = 0
        best_size = len(nums) + 1

        if curr_sum >= target:
            return 1

        # at each step, R pointer moves by one, 
        # we add the new element. if target exceeded, move L
        for R in range(1,len(nums)+1):
            # print(f"{R=} (before) {curr_sum=} (before) {L=}")
            curr_sum += nums[R-1]
            while L < R and curr_sum - nums[L] >= target:
                curr_sum -= nums[L]
                L += 1

                # print(f"{R=} while {curr_sum=} {L=}")

                    
            if curr_sum >= target and R - L < best_size:
                best_size = R - L
        
        if curr_sum >= target:
            return best_size
        else:
            return 0
        
        # why this works: consider an optimal (minimal) interval 
        # that satisfies the constraint that ends at position $r$
        # with length l*
        # Since the R pointer will get to it in iteration r, then the interval [0,r] is included.
        # or smaller. if it its larger than length l*, the inner step will find that.
        # runtime: Outer loop has n iterations. inner loop at most runs total of n. total O(n)

            
            






        

        