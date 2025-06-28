class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Attach index to value
        arr = [(val, i) for i, val in enumerate(nums)]

        # Step 2: Sort by value descending
        arr.sort(key=lambda x: -x[0])

        # Step 3: Take top-k and re-sort by original index
        top_k = sorted(arr[:k], key=lambda x: x[1])

        # Step 4: Extract values
        return [val for val, _ in top_k]