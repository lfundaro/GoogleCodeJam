# Google code jam 2008 Round 1A - warming up
# Script that parses the input file and executes milkshakes executable
# generated from 'milkshakes.cpp', and formats the output

import sys
import os
import commands

os.system('make') #compile milkshakes
out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

for c in range(1,num_cases+1):

    params = [] #problem parameters
    params.append(in_file.readline().strip('\n'))
    params.append(in_file.readline().strip('\n'))

    for i in range(int(params[1])):
        likes = (in_file.readline().strip('\n')).split(' ')
        params+=likes
        
    sol = commands.getoutput('./milkshakes '+' '.join(params)).split('\n')
    if(sol[1]==''):
        result = 'IMPOSSIBLE'
    else:
        result = ''.join((sol[1].strip('{')).strip('}').split(','))

    out_file.write('Case #'+str(c)+': '+result+'\n')
    
