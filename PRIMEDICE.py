# cook your dish here
prime=[1,2,3,5,7,11,13,17,19,23]
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    sum=a+b
    if sum in prime:
        print("Alice")
    else:
        print("Bob")
