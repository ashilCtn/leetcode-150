class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = r + 1
            else:
                profit = prices[r] - prices[l]
                maxProf = max(maxProf, profit)
                r += 1
            
        return maxProf