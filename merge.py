a=[1,2,3]
b=[1,3,4]


def merge(x,y):
    a=sorted(x)
    b=sorted(y)
    c=[]
    i,j=0,0
    while i <len(a) and j<len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])


    return c

if __name__=="__main__":
    a=[1,2,3]
    b=[1,3,4]
    print(merge(a,b))


            
       


                   
    
    
            

            


