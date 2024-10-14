a=int(input())
b=int(input())
l=int(input())
N=int(input())
def f(a,b,l,N):
    t=2*a*N    #вертикаль
    m=b*(N-1)  #горизонталь
    v=t+m+l    #общая 
    return v
print(f(a,b,l,N))
