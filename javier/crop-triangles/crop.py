# Google code jam - Online round 1B
# Crop triangles - Small
# Javier Fernandez: javierfdr@gmail.com

import sys
out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

# sort and add to set
def ord_set(set,list):
    element.sort()
    set.add(element)

for c in range(1,num_cases+1):
    n,A,B,C,D,x0,y0,M = map(int,in_file.readline().split())
    points =[]    
    # google snippet
    X = x0
    Y = y0
    points.append((X,Y))
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        points.append((X,Y))

    # kinda ugly multiple iteration , maybe possible to make
    # it more beautiful with map and comprehension list

    # the multiple cicle is inevitable. Optimized with
    # progressive checking in the same array [ci:] and [cj:]
    triangles = []
    count = 0
    ci=0
    cj=0
    for i in points:        
        cj=ci+1
        for j in points[ci:]:#Avoid previous tuples
            for k in points[cj:]:                
                if (((i[0]+j[0]+k[0])%3 ==0) and ((i[1]+j[1]+k[1])%3 ==0)):
                        t = [i,j,k]                        
                        triangles.append(t)
                        count+=1
            cj+=1
        ci+=1
    
    out_file.write('Case #'+str(c)+': '+str(count)+'\n')
    
