class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        span = 1
        while self.stocks and price >= self.stocks[-1][0]:
            price_info = self.stocks.pop()
            span += price_info[1]
        
        self.stocks.append([price,span])

        return self.stocks[-1][1]
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)