class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) time complexity and O(1) space complexity
        maxProfit = 0
        left, right = 0, 1
        while (right < len(prices)):
            if (prices[right] > prices[left]):
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit