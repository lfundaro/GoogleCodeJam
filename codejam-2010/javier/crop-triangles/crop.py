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
    
    lp = len(points)
    while(ci<lp):#while's used to avoid list cutting        
        cj=ci+1
        while(cj<lp):
            ck=cj+1
            while(ck<lp):
                pi=points[ci]
                pj=points[cj]
                pk=points[ck]                
                if ((pi[0]+pj[0]+pk[0])%3 ==0):
                    if ((pi[1]+pj[1]+pk[1])%3 ==0):
                        t = [pi,pj,pk]                        
                        count+=1
                ck+=1
            cj+=1
        ci+=1
    
    out_file.write('Case #'+str(c)+': '+str(count)+'\n')
    
