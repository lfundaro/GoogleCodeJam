#! /usr/bin/python

import sys

def prepare_string(string):
    string = string.split(' ')
    for i in range(len(string)):
        string[i] = string[i].strip('\n')
        string[i] = int(string[i])
    return string



def min_scalar(v1, v2, vector_size):
    # Ordering
    v1.sort()
    v2.sort(reverse = True)

    min = 0
    for i in range(vector_size):
        min = min + v1[i]*v2[i]
        
    return min


f = file(sys.argv[1], 'r')
cases = int(f.readline())

for times in range(cases):
    vector_size = prepare_string(f.readline())  
    v1 = prepare_string(f.readline())
    v2 = prepare_string(f.readline())
    answer = min_scalar(v1, v2, vector_size[0])
    print 'Case #' + str(times + 1) + ': ' + str(answer)

