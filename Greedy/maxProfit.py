# 买卖股票的最佳时机
# 输入：[7,1,5,3,6,4]
# 输出 5，在第二天买入 在第五天卖出的时候，利润最大 = 5

class Solution:
    def maxProfit(self, prices):

        if len(prices) < 2:
            return 0

        minProfit = prices[0]
        profit = 0
        for i in prices:
            minProfit = min(i, minProfit)
            profit = max(i - minProfit, profit)
        return profit
