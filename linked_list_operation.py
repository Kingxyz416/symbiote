class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
        
    def insert_head(self,data):
        newdata=Node(data)
        newdata.next=self.head
        self.head=newdata
    def insert_tail(self,data):
        newdata=Node(data)
        if not self.head:
            self.head=newdata
            return
        c=self.head
        while c.next:
            c=c.next
            c.next=newdata
    def display(self):
        c = self.head

        while c:
            print(c.data, end=" -> ")
            c = c.next

    print("None")

l=linkedlist()

l.insert_tail(20)
l.display()


    
    

        