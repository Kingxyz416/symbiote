class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        
        self.items.append(item)
    
    def pop(self):
        
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
     
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        
        return len(self.items)



if __name__ == "__main__":
    stack = Stack()
    
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Stack after pushes:", stack.items)
    
   
    print("Popped:", stack.pop())
    print("Stack after pop:", stack.items)
    
    print("Top item:", stack.peek())
    
    print("Stack size:", stack.size())
