class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stockPrice = prices[0]
        stockPriceDay = 1
        sellingDay = 0
        for p in range(1,len(prices)):
            buyingPrice = min(stockPrice, prices[p])
            if buyingPrice < stockPrice:
                stockPriceDay = p+1
                stockPrice = buyingPrice
            cumpProfite = max(profit, prices[p]-stockPrice)
            if cumpProfite > profit:
                profit = cumpProfite


        return profit        