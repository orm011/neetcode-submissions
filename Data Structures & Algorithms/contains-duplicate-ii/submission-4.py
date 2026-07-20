class Solution:

    def containsNearbyDuplicateNaive(self, nums: List[int], k: int) -> bool:
        # naive apporach:
            # redo the work on each window.
            # O(nk)
        # improvement: re-using work from previous runs.
        # solve initial case. then move right, incremental work. O(1) hopefully

        # naive approach
        for i in range(len(nums)):
            entries = {}
            for j in range(k+1):
                if i+j >= len(nums):
                    return False
                value = nums[i+j]
                if value not in entries:
                    entries[value] = 1
                else:
                    return True

        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # naive apporach:
            # redo the work on each window.
            # O(nk)
        # improvement: re-using work from previous runs.
        # solve initial case. then move right, incremental work. O(1) hopefully

        # faster approach
        entries = {}
        for i in range(len(nums)):
            # case: k = 1 (ie include 2 elts in window)
            if i > k: # if i > 2, eg i = 2 start removing 2 - 1 -1  = 0 to include only 1 and 2
                old_value = nums[i - k - 1]
                del entries[old_value]

            new_value = nums[i]            

            if new_value in entries:
                return True
            else:
                entries[new_value] = 1

        return False

                

                 


        