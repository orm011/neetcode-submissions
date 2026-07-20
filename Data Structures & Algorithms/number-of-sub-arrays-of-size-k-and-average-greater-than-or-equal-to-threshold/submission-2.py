class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # will track current sum and update it every time.
        if len(arr) < k:
            return 0

        current_sum = sum(arr[:k])
        sum_threshold = threshold * k 
        current_count = int(current_sum >= sum_threshold)

        for L in range(1, len(arr) - k + 1):
            R = L + k
            current_sum -= arr[L-1]
            current_sum += arr[R-1]
            current_count += (current_sum >= sum_threshold)
            # print(f"{L=} {arr[L-1]=} {arr[R-1]=} {current_count=}")

            
        return current_count

