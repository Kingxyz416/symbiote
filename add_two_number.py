class ListNode:
    def __init__(self,value):
        self.value=value
        self.next=next
        
class Solution(object):
    def __init__(self):
        self.set=[ListNode(0) for _ in range (769)]
        
    def addTwoNumbers(self, l1, l2):
        u=[]
        index1 = len(l1)%len(self.set)
        index2= len(l2)%len(self.set)
        a=self.set[index1]
        b=self.set[index2]

        while a and b is None:
            return 0
            

            


        