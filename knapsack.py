'''
https://www.byte-by-byte.com/wp-content/uploads/2019/01/50-Coding-Interview-Questions.pdf
Question: 2. 0-1 Knapsack
Question: Given a list of items with values and weights, as well as a max weight,
find the maximum value you can generate from items where the sum of the
weights is less than the max.

'''

def knapsack(items,maxWeight):
  '''
  STRATEGY: rows = index of items
  cols = maxWeight + 1 (to handle 0 weight)
  if item weight is less than the col weight, then alone compute the value
  the value would be max from previous row without this weight included or with this weight included plus value with remaining weight
  '''

  rlen = len(items)
  clen = maxWeight+1
  dp = [[0 for i in range(clen)] for j in range(rlen)]
  
  for i in range(len(dp)):
    for j in range(1,len(dp[0])):
      print("weight:{} targetweight:{}".format(items[i],j))
      # the value would be max from previous row without this weight included or with this weight included plus value with remaining weight
      if items[i][0] < j:
        val = items[i][1] + dp[i][j-items[i][0]]
        dp[i][j] = max(dp[i-1][j],val)


  print("dp:{}".format(dp))

  return dp[rlen-1][clen-1]







'''items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
maxWeight = 5
knapsack(items, maxWeight) = 22'''

items = [[1,6],[2,10],[3,28]]
maxWeight = 5
print(knapsack(items,maxWeight))
