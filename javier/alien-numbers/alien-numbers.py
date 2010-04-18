#Alien numbers - Google code jam warming up
#Javier Fernandez

import math

    
def from_10_to_base(number,base):
    div = number
    convert =''
    while(div !=0):
        convert= str(div%base)+convert
        div = div/base

    return convert

# Receives number as string
def from_base_to_10(number,base):
    count = 1
    n=0
    for i in range(len(number)-1,-1,-1):
        n+=int(number[i])*count
        count*=base
    return str(n)

def alien_to_pos(alien,language):
    pos_array=''
    for a in alien:
        pos_array+=str(language.find(a))
        
    return pos_array

def pos_to_alien(pos,language):
    alien=''
    for p in pos:
        alien+=language[int(p)]
    return alien
    
def alien_compute(alien,source,target):    
    pos = alien_to_pos(alien,source)
    base10 = from_base_to_10(pos,len(source))
    convert = from_10_to_base(int(base10),len(target))
    return pos_to_alien(convert,target)
    
def execute_alien(input,output):
    f=open(input)
    o=open(output,'w+')
    in_file = f.readlines()
    cases = int((in_file[0].split(' '))[0])
    #for c in range(1,cases+1):
    for c in range(5,6):
        line = in_file[c].split(' ')
        line[2] = line[2].strip('\n')
        output = 'Case #'+str(c)+': '
        output += alien_compute(line[0],line[1],line[2])+'\n'
        o.write(output)
