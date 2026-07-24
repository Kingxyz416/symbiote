def post(exp):
    pre = {
         '+':1,
         '-':1,
         '*':2,
         '/':2,
         '^':3
         }
    stack=[]
    postfix=""
    for i in exp:
        if i.isalnum():
            postfix += i

        elif i =='(':
            stack.append(i)
        elif i ==")":
            while stack and stack[-1] !="(":
                postfix+=stack.pop()
            stack.pop()
        else :
            while (stack and stack[-1]!='('and pre.get(i,0) <= pre.get(stack[-1],0)):
                postfix+=stack.pop()
            stack.append(i)

    while stack:
        postfix += stack.pop()
            

    return postfix


x="6+5*(9-7)"
print(post(x))
y=post(x)

def sol(expp):
    new=[]
    for i in expp:
        if i.isdigit():
            new.append(int(i))
        else:
            b=new.pop()
            a=new.pop()
            if i =='+':
                new.append(a+b)
            elif i=='-':
                new.append(a-b)
            elif i=='*':
                new.append(a*b)
            elif i=='/':
                new.append(a/b)
    return new.pop()


print(sol(y))

    

                
                










 
    
        
       



  



    