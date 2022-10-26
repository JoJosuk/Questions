'''
lister[rhand,lhand,rleg,lleg]

'''

dicta={"left hand to head":1,"left hand to hip":2,"left hand to start":3,"left leg in":4,"left leg out":5,"right hand to head":6,"right hand to hip":7,"right hand to start":8,"right leg in":9,"right leg out":10,"turn":11}
def printdance(lister):
    if (lister[0]==2) :
        print("(",end="")
    else:
        print(" ",end="")
    print("o",end="")
    if (lister[1]==2) :
        print(")")
    else:
        print("")
    if (lister[0]==1) :
        print("<",end="")
    elif (lister[0]==2) :
        print(" ",end="")
    elif lister[0]==0  :
        print("/",end="")
    print("|",end="")
    if (lister[1]==1) :
        print(">")
    elif (lister[1]==2) :
        print(" ")
    elif lister[1]==0 :
        print("\\")
    if (lister[2]==0) :
        print("/",end=" ")
    if lister[2]==1:
        print("<",end=" ")
    if lister[3]==0:
        print("\\")
    if lister[3]==1:
        print(">")
printdance([0,0,0,1])