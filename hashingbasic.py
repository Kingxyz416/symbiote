from collections import Counter
class listnodes:
    def __init__(self,size):
        self.size=size
        self.next=None
class hash:
    def __init__(self):
        self.set=listnodes([0] for _ in range(10))
    def index(self,key):
        a= key% len(self.set)
        return a

    