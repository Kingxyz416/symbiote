import math
class Solution(object):

    def winnerSquareGame(self, n):
        y =math.sqrt(n)
        z= n%2
        if n==0:
            return True
        if n==2:
            return False
       
        elif z==0:
            return True
        elif y.is_integer():
            return True
        elif z!=0:
            return False
       
            


            
        
        