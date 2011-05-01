
# get key with value 1
def get_odd(odd_dic):
    return [k for k, v in odd_dic.iteritems() if v == 1][0]

def process_odd_input(input_f,output_f):
    f=open(input_f)
    o=open(output_f,'w+')
    l=f.readlines()

    cases = int(l[0])
    l_count=1
    c_count=1
    
    while(c_count<=cases):

        guests = l[l_count]
        codes = l[l_count+1].split(' ')
        codes[len(codes)-1]= codes[len(codes)-1].strip('\n')
        
        odd_dic={}
        for c in codes:
            if c in odd_dic:
                odd_dic[c]=2
            else:
                odd_dic[c]=1
                
        o.write('Case #'+str(c_count)+': '+get_odd(odd_dic)+'\n')
        l_count+=2
        c_count+=1
    
    
