class Solution:
    def longestPalindrome(s):
        # [b][][bad]
        # a b c
        flag=0
        if len(s) <=1:
            # for empty string and single char
            print (s)
            flag=1
        elif len(s) == 2:
            print (s) if s[0] == s[1] else s[0]
            flag=1
        
        a = [s[0]]
        b = '' # empty for even sizes
        c = list(s[-1:0:-1])
        # c reversed in order to allow for pop() instead of pop(0) which is in O(n) time
        
        maxPalin = ''
        while len(c) > 0:
            palinC = b
            
            for j in range(0, min(len(a), len(c))):
                char = c[-1-j]
                if a[-1-j] == char:
                    palinC = char + palinC + char #O(1)
                else:
                    break

            if b != '':
                a.append(b) #O(1)
                b = ''
            else:
                b = c.pop() #O(1)
            
            if len(palinC) > len(maxPalin):
                maxPalin = palinC
        if flag!=1:
            print (maxPalin)        
    longestPalindrome(input())