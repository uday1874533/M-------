# cook your dish here
# PARLOUR 2 0 1 5  TODAY 2023
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    c=b-a
    print(math.ceil(c/8))
