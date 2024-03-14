def acker(x,y):
    if x==0: return y+1
    elif y==0: return acker(x-1,1)
    else: return acker(x-1,acker(x,y-1))

def acker2(m,n):
    if m==0: return n+1
    elif m>0 and n==0: return acker2(m-1,1)
    elif m>0 and n>0: return acker2(m-1,acker2(m,n-1))