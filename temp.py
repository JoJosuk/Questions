class Solution:
    def convert(s, numRows) :
        b=[''] * numRows
        i=0
        for j in s:
            b[i]+=j
            if i==0 and i==(numRows-1):
                return s
            elif i==0:
                swap=0
            elif i==(numRows-1):
                swap=1
            if swap==0:
                i+=1
            elif swap==1:
                i-=1 
        sol=''
        for i in b:
            for j in i:
                sol+=j

        return sol
r=int(input())
s=input()
print(Solution.convert(s,r))