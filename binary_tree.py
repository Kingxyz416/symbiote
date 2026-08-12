class Node:
    def __init__(self, d):
        self.data =d
        self.right = None
        self.left = None
    
firstNode=Node(1)
secondNode=Node(2)
thirdNode=Node(3)
fourthNode=Node(4)
fifthNode=Node(5)

firstNode.left = secondNode
firstNode.right=thirdNode
secondNode.left=fourthNode
secondNode.right=fifthNode
def binaryprint(n,level=0,label='Root'):
        if n is None:
            return 
        print(" "*(level*3)+ f"{label}:{n.data}")
        binaryprint(n.left,level+1,"L")
        binaryprint(n.right,level+1,"R")
        
binaryprint(firstNode)



        

        