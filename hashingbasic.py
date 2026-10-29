from collections import Counter
class listnodes:
    def __init__(self,size):
        self.size=size
        self.next=None
        self.bucket=[[] for _ in range(967)]
class hash:
    
    def index(self,key):
         key % self.size
        
    def put(self,key,value):
        index=self.index(key)
        bucket = self.set[index]
        while bucket.next:
            if bucket.next.key==key:
                return 
            bucket=bucket.next
            bucket.next=listnodes[key]
if __name__=="__main__":
    



 

    