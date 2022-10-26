keyno=5
f=open("words.txt","r")

dic={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
words=f.read().split()
rewrite=[]
lister=[0,0,0,0,0,0,0,0]
for i in words:
    for j in range(keyno+1,9):
        if len(i)==j:
            lister[j-1]+=1
            rewrite.append(i)
            if i[keyno] in dic.keys():
                dic[i[keyno]]+=1
print(lister)
rewrite.sort()
f2=open("wordsunder9.txt","w")
for i in rewrite:
    f2.write(i+"\n")
sortdics = sorted(dic.items(), key=lambda x:x[1])
lister=[]
for i in sortdics:
    lister.append(i[0])
    string=''
for i in lister[26::-1]:
    string+=i
print(string[0:10])    
