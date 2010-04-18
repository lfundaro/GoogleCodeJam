
import sys
#sort max X and min Y and compute
def min_scalar(x,y):
    x.sort(reverse=True)
    y.sort()
    
    l = len(x)
    scalar = 0
    while(l>0):
        l-=1
        scalar += x.pop()*y.pop()
    return scalar

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

for c in range(1,num_cases+1):
    in_file.readline() #ignore num elements
    x = map(int,in_file.readline().split())
    y = map(int,in_file.readline().split())
    scalar = min_scalar(x,y)
    out_file.write('Case #'+str(c)+': '+str(scalar)+'\n')
    
