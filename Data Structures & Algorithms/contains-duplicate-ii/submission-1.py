class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
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

                

                 


        