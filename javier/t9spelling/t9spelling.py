

#Translate the given word 'word' using the letters dictionary
#letters-to-numbers given in dict
def trans_word(word,dic):
    word.lower()
    last ='none'
    res=[]
    for l in word:
        if (dic[last][0]==dic[l][0]):
            res.append(' '+dic[l])
        else:
            res.append(dic[l])
        last = l

    return ''.join(res)
            

import sys

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

ldic = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999',' ':'0','none':'-1'}

for c in range(1,num_cases+1):
    word = in_file.readline().strip('\n')
    case = 'Case #'+str(c)+': '
    out_file.write(case+trans_word(word,ldic)+'\n')
    
