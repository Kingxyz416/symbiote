class Solution(object):
    def maxProfit(self, prices):
        j=1
        for i in range(0,len(prices)):
            if prices[i]<prices[j]:
                h=prices[j]
                i+=1
            else:
                return h

            


       
       


          

