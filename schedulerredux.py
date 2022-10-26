n,m=map(int,input().split())
l=list(map(int,input().split()))
list2=[]
sumer=0
for i,j in enumerate(l):
    l[i]=2**j
if(m==1):
    print(sum(l)%1000000007)
rem=n%m
div=n//m
enum=0
while(enum<len(l)):
    if(rem>0):
        i=rem+div
        temp=[]
        for j in range(i):
            temp.append(l[enum])
            enum+=1
        list2.append(temp)
        rem-=1
    else:
        i=div
        temp=[]
        for j in range(i):
            temp.append(l[enum])
            enum+=1
        list2.append(temp)
list3=[]
for i in list2:
    list3.append(sum(i))
print(max(list3)%1000000007)

        