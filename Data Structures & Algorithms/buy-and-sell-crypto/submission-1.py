class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini_buy=prices[0]
        maxi_profit=0
        for i in range(len(prices)):
            mini_buy=min(mini_buy,prices[i])
            pro=prices[i]-mini_buy
            maxi_profit=max(pro,maxi_profit)
        return maxi_profit