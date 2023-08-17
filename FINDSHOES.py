 #LAPTOP RESET
# cook your dish here
shoes = int(input())
for s in range(shoes):
  f,l = map(int,input().split())
  print (f) if f-l<=0 else print((2*f)-l)
