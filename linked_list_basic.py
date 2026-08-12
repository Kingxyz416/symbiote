class Node:
    def __init__(self,ndata):
        self.data=ndata
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
temp = head
while temp is not None:
    print(temp.data,end=" ")
    temp=temp.next 



        