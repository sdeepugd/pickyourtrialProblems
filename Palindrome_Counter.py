import sys

def ispalindrome(str):
    n=len(str)
    for i in range(n/2):
        if str[i]!=str[n-i-1]:
            return False
    return True

def countPalindromes(s)
    palin_set=set()
    strng=s
    
    def genpalin(start,stop,n):
        if start>stop or stop is n or start is n:
            return
        else:
            indices=(start,stop)
            palin_set.add(indices)
        genpalin(start+1,stop,n)
        genpalin(start,stop+1,n)
    
    genpalin(0,0,n=len(strng))
    count=0
    for indices in palin_set:
        start=indices[0]
        stop=indices[1]
        substrng=strng[start:stop+1]
        if ispalindrome(substrng):
            count=count+1
    return count
