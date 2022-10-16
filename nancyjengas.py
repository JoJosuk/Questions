class Solution:
    def push(d):
        buffer='0'
        res=''
        temp=''
        for i in range(len(d)) :
            if d[i]=='.':
                temp=temp+'.'
            else:
                if d[i]==buffer:
                    res+=(d[i]*len(temp))+d[i]
                elif buffer=='0':
                    if d[i]=='L':
                        res+=('L'*len(temp))+'L'
                        buffer='L'
                    elif d[i]=='R':
                        res+=temp+'R'
                        buffer='R'
                elif d[i]=="L" and buffer=='R':
                    if(len(temp)%2==0):
                        res+=('R'*(len(temp)//2))+('L'*(len(temp)//2))+'L'
                    else:
                        res+=('R'*(len(temp)//2))+"."+('L'*(len(temp)//2))+'L'
                    buffer='L'
                
                elif d[i]=="R" and buffer=='L':
                    res+=temp+'R'
                    buffer='R'
                temp=''
        if buffer=='R' and temp:
            res=res+'R'*len(temp)
        elif temp:
            res=res+temp
        print(res)
        
    d=input()
    push(d)