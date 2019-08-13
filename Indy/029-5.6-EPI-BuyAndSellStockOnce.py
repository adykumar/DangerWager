"""
Input: An array representing daily stock prices
Output: The maximum profit that can be made by buying and selling the stock once (sell only a day after buying)
Logic:
- Greedy (difference of min and max) won't work - sell can only be on the next day
- At each index maintain:
    - min stock price seen so far (min so far)
    - the max profit that can be made so far (current price - min price so far)
- Once the entire array has been processed, you will have the max profit
"""

from typing import List


class Solution:
    def buy_and_sell_stock_once(self, prices: List[int]) -> int:

        # 2 variables to track the min price so far and max profit so far
        min_price_so_far, max_profit_so_far = float('inf'), 0.0

        # for today's share price, find the max profit that can be made if sold today
        # update max profit if applicable
        # update the min price seen so far if applicable
        for price in prices:
            max_profit_sell_today = price - min_price_so_far
            max_profit_so_far = max(max_profit_so_far, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, price)

        return max_profit_so_far


s = Solution()
print(s.buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))
