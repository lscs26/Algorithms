#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #to hold max profit calculations
  maxProfit = prices[1] - prices[0]
  currentMin = prices[0]
  for price in prices[1:]:
    if price < currentMin:
      currentMin = price
    elif price - currentMin > maxProfit:
      maxProfit = price - currentMin
  return maxProfit

print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))