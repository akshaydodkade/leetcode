class Solution:
  def maximumAmount(coins):
    m, n = len(coins), len(coins[0])
    
    NEG_INF = float('-inf')
    
    # dp[i][j][k]
    dp = [[[NEG_INF]*3 for _ in range(n)] for _ in range(m)]
    
    # Base case
    for k in range(3):
      if coins[0][0] >= 0:
        dp[0][0][k] = coins[0][0]
      else:
        if k > 0:
          dp[0][0][k] = 0
        else:
          dp[0][0][k] = coins[0][0]
    
    # Fill DP
    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          continue
        
        val = coins[i][j]
        
        for k in range(3):
          best_prev_same_k = NEG_INF
          
        if i > 0:
          best_prev_same_k = max(best_prev_same_k, dp[i-1][j][k])
        if j > 0:
          best_prev_same_k = max(best_prev_same_k, dp[i][j-1][k])
        
        # Case 1: no neutralization
        if best_prev_same_k != NEG_INF:
          dp[i][j][k] = max(dp[i][j][k], best_prev_same_k + val)
        
        # Case 2: use neutralization
        if val < 0 and k > 0:
          best_prev_prev_k = NEG_INF
          
          if i > 0:
            best_prev_prev_k = max(best_prev_prev_k, dp[i-1][j][k-1])
          if j > 0:
            best_prev_prev_k = max(best_prev_prev_k, dp[i][j-1][k-1])
          
          if best_prev_prev_k != NEG_INF:
            dp[i][j][k] = max(dp[i][j][k], best_prev_prev_k)
  
    return max(dp[m-1][n-1])


if __name__ == '__main__':
  s = Solution()
  coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
  print(s.survivedRobotsHealths(coins))