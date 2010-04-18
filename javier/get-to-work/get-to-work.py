# get to work - google code jam 2010 Warming up
# Javier Fernandez

# Implementation notes:
# Does not matter the path taken by any car, thus the main idea
# is to fill the cars with the biggest capacity until no more
# worker is stucked or there is no space left.
# Workers can only have a ride from people in the same town(crucial)

def get_to_work(nt,office,ne,town_cars):
    #town_cars must be [[(capacity1,town1),(capacityN,town1)] reverse sort
    best_dist= [0 for t in range(nt)]

    for tc in town_cars:        
        town_emp = len(tc)
        if (town_emp == 0):
            continue
        for c in tc:
            # in office do not travel
            if (c[1]==office):
                town_emp = 0
                break

            # no car
            capacity = c[0]
            if(capacity==0):                
                continue

            # got car ride all town mates
            town_emp-= capacity
            best_dist[c[1]-1] += 1
            if (town_emp<=0):
                break
        if(town_emp>0):
            return []
        ne-=len(tc)
        
    if (ne>0):
        return []
    else:
        return best_dist
        
import sys

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

for c in range(1,num_cases+1):
    nt,office = map(int,in_file.readline().split())
    ne = int(in_file.readline())
    
    #set town cars
    town_cars = [[] for t in range(nt+1)]
    for i in range(ne):
        ht,p = map(int,in_file.readline().split())        
        town_cars[ht].append((p,ht))
    for tc in town_cars:
        tc.sort(reverse=True)
    town_cars=town_cars[1:]    

    gtw = get_to_work(nt,office,ne,town_cars)
    out_string = 'Case #'+str(c)+': '
    if (not gtw):
        out_file.write(out_string+'IMPOSSIBLE'+'\n')        
    else:
        out_file.write(out_string + ' '.join((map(str,[x for x in gtw])))+'\n')        
