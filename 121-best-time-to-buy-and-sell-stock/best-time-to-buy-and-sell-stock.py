class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_sum = 0
        max_sum = 0
        for i in range(1, len(prices)):
            temp_sum = temp_sum + prices[i] - prices[i-1]
            temp_sum = temp_sum if temp_sum > 0 else 0
            max_sum = max_sum if max_sum > temp_sum else temp_sum
        return max_sum