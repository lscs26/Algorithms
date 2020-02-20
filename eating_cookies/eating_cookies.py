#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  # else:
  #   return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
  elif cache and cache[n] > 0:
    return cache[n]
    # print(cache)
    # running 'python3 eating_cookies/eating_cookies.py 7' should return
    # 'There are 44 ways for Cookie Monster to eat 7 cookies.'
  else:
    if cache is None:
      cache = {}
    value = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    cache[n] = value
    # print("after adding value, cache is: " + str(cache))
    return value
    

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')