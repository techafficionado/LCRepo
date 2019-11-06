import sys
def coinChange(coins,amount):

  '''
  STRATEGY: USE A SINGLE ARRAY, SET DP[0]=0 AND UPDATE THE ARRAY ONLY WHEN j>=coins. DO NOT USE A 2D ARRAY!!!
  '''
  dp = [sys.maxsize]*(amount+1)
  dp[0] = 0

  for i in range(len(coins)):
    for j in range(1,len(dp)):
      if j >= coins[i]:
        count = 1+dp[j-coins[i]]
        dp[j] = min(dp[j],count)

  return dp[-1]


coins = [1,5,10,25]
amount = 49
print(coinChange(coins,amount))  
