class Solution(object):
    def longestValidParentheses(self, s):
       stack=[-1]
       best=0
       for i in range(len(s)):
           if s[i] =='(':
              stack.append(i)
           else:
               stack.pop()
               if not stack:
                   stack.append(i)
               else:
                   best=max(best,i - stack[-1])
       return best  
            
               

            