class Solution(object):
    def minCostClimbingStairs(self, cost):
       n=len(cost)
       dp=[0]*n
       dp[0]=cost[0]
       dp[1]=cost[1]
       for i in range(2,n):
           x=cost[i]+min(dp[i-1],dp[i-2])
           dp.append(x)
           
       return min(dp[i-1],dp[i-2])


            

        