class solution(object):
    
 def twosum(nums1,nums2):
    self=[]
    d=[]
    s=0
    p=0
    y,w=0,0
    for i in range(0,len(nums1)):
       s=s*10+nums1[i]
    while s>0:
        n=s%10
        y=y*10+n
        s=s//10



    for j in range(0,len(nums2)):
        p=p*10+nums2[j]
    while p>0:
       q=p%10
       w=w*10+q
       p=p//10

    total = w+y
    while total >0:
        self.append(total%10)
        total = total //10
    d=self[::-1]

    return d
 if __name__=="__main__":
    nu =[1,4,5]
    num =[3,4,6]
    print(twosum(nu,num))





    

    


   