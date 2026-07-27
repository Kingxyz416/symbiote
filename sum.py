def add(a,b):
    c=[]
    a=sorted(a)
    b=sorted(b)
    x=0
    y=0
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                x+=1
    c.append(x)
    for j in range(0,len(b)):
        for i in range(0,len(a)):
            if b[j]==a[i]:
                y+=1
    c.append(y)
    return c 
if __name__=="__main__":
    a=[1,1,2,5,4]
    b=[2,1,5,9,3]
    print(add(a,b))
    
        
        
    
    
                      
              

            
    

    
    