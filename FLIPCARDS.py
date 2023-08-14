# TMRW INDEPENDENCE DAY
h = int(input())
for i in range(h):
    n,x = map(int,input().split())
    print(min(x,n-x))
