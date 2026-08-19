a=[10,20,30,40,0,0,0,0,0,0]
n=4


def ib(x):
    global n
    i=n
    while i>0:
        a[i]=a[i-1]
        i=i-1
    a[0]=x
    n=n+1


def ie(x):
    global n
    a[n]=x
    n=n+1


def ip(p,x):
    global n
    i=n
    while i>p:
        a[i]=a[i-1]
        i=i-1
    a[p]=x
    n=n+1


def db():
    global n
    i=0
    while i<n-1:
        a[i]=a[i+1]
        i=i+1
    n=n-1


def de():
    global n
    n=n-1


def dp(p):
    global n
    i=p
    while i<n-1:
        a[i]=a[i+1]
        i=i+1
    n=n-1


ib(5)
ie(50)
ip(2,15)

print("After insertion:",a[:n])

db()
de()
dp(1)

print("After deletion:",a[:n])