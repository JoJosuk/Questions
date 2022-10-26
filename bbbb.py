def ceel(k):
    if(k-int(k)>0):
        return int(k)+1
    else:
        return k
    
p=int(input())
n=int(input())
r,c=map(int,input().split(","))
posc=input()
lis=[]
fin=[]
for i in range(p):
    a=input()
    lis.append(a)
for i in range(n):
    a=input()
    fin.append(a)
x=[n-1,n-2,1,0]
for i in x:
    fin.pop(i)
for i in range(n-4):
    String=fin[i]
    fin[i]=String[3:(len(fin[i])-4):1]
finstring=""
for i in fin:
    finstring+=i
finalstr=finstring.replace(" ","_")
if(posc=="S"):
    for i in lis:
        count=len(i)
        for j in i:
            flag=0
            for k in range(len(finalstr)):
                if(j==finalstr[k]):
                    print(ceel((k+1)/c),((k+1)%c),end='',sep=',')
                    flag=1
                    break;
                 
            if count>1:
                print(',',end='') 
            count-=1
        print()
            
    print()      
       # if(finalstr[i]==""):
        #    finalstr[i]=" "
elif(posc=="L"):
    for i in lis:
        count=len(i)
        flag1=0
        for j in i:
            flag=0
           
            for k in range(len(finalstr)):
                if(j==finalstr[k]):
                    temp=k
            print(ceel((temp+1)/c),((temp+1)%c),end='',sep=',')
           # if flag1==0:
            #    print(',',ceel((temp+1)/c),((temp+1)%c),end='',sep=',')
             
            if count>1:
                print(',',end='') 
            count-=1   
        print()      
       # if(finalstr[i]==""):
        #    finalstr[i]=" "



