cases=int(input())
for i in range(cases):
    cut=list(map(int,input().split()))
    nocut=0;
    lister=[]
    for j in range(1,cut[0]+1):
        negflag=0
        angle=cut[j]
        if angle<0:
            angle=360-(abs(angle)%360)
        elif angle>360:
            angle=angle%360
        '''while(negflag==1):
            if angle<0:
                angle+=360
                if angle>0:
                    negflag=0
        if angle>360:
            angle=angle%360
        counterangle=(angle+180)%360'''
        if angle not in lister:
            lister.append(angle)
            lister.append(counterangle)
            nocut+=2
        
    if(len(lister)==0):
        nocut=1
    print(nocut)
        
                    