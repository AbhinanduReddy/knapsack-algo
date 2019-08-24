def maxp(p,w,m):
    r=[v/w for v,w in zip(p,w)]
    index=list(range(len(p)))
    print(p)
    print(w)
    print(r)
    print(index)
    index.sort(key=lambda i:r[i],reverse=True)
    print(index)
    maxx=0
    f=[0]*len(p)
    for i in index:
        if w[i]<=m:
            f[i]=1
            maxx+=p[i]
            m-=w[i]
        else:
            f[i]=m/w[i]
            maxx+=p[i]*(m/w[i])
            break
    return maxx,f

p=[int(i) for i in input().split()]
w=[int(i) for i in input().split()]
m=int(input())
maxx,f=maxp(p,w,m)
print(maxx,f)
