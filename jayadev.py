temp1,temp2=input().split()
n=int(temp1)
p=int(temp2)
list2=[]
list=input.split()
for i in range(n):
    list[i]=int(list[i])
for i in range(n):
    list2.append(2**list[i])
print(max(list2))