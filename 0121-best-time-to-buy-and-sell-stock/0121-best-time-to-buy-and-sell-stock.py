class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We need to use the two pointers method
        left, right = 0, 1
        maxProfit = 0
        
        while (right < len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit