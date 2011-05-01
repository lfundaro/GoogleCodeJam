#################################
#                               # 
#      ALGORITMOS GENETICOS     #
#            GABIL              #
#                               #
#                               #
#        Javier Fernandez       #
#       Gabriela Martinez       #
#                               #
#   Universidad Simon Bolivar   #
#                               #
#################################

# El siguiente programa 'gabil_classify.py' corresponde a
# la implementacion de un algoritmo de clasifacion genetico
# basado en los lineamientos de GABIL, en donde el numero de
# reglas de los cromosomas es variable.
# 
# Se presentan tres metodos de seleccion: Roulette Selection,
# Tournament Selection y  SUS Selection
#
# El presente programa esta orientado a la clasificacion de
# cromosomas con reglas de tama\~no 23 que representan
# la eleccion de compra de un automovil en base a sus
# caracteristicas, entrenado con la base de datos
# creada por Marko Bohanec y disponible en:
# ftp://ftp.ics.uci.edu/pub/machine-learning-databases/car
# 

import random

# Clase de excepcion para longitud
# incorrecta de cromosoma
class CromLength(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

      
# Constante de comienzo de una regla
conj_end=[0,4,8,12,15,18,21,23]

# Arreglo de atributos de las reglas
attributes=[['vhigh','high','med','low'],
            ['vhigh','high','med','low'],
            ['2','3','4','5more'],
            ['2','4','more'],
            ['small','med','big'],
            ['low','med','high']]

# Funcion que devuelve la configuracion
# en dos bits de la clasificacion obtenida

def classificate(x,y):
    if (x=='0' and y =='0'):
        return 'unacc'
    elif (x=='0' and y=='1'):
        return 'acc'
    elif (x=='1' and y=='0'):
        return 'good'
    elif (x=='1' and y=='1'):
        return 'v-good'


# Lista de separadores de conjunciones en un cromosoma
def separators_gen(cromosome):
    num_reglas=len(cromosome)//23
    sep_list=[]
    for rule in range(0,num_reglas+1):
        sep_list.append((23*rule))

    return sep_list

# Despliega las reglas del cromosoma y las devuelve
# en una lista
def split_rules(cromosome):
    num_reglas=len(cromosome)/23
    rule_list=[]
    rule_list.append(cromosome[0:23]) # no incluye el ultimo elemento
    for i in range(1,num_reglas):
        rule=cromosome[23*i:23*i+23]
        rule_list.append(rule)

    return rule_list

# print_cromo() imprime un cromosoma divido en los
# atributos del cromosoma:
# 'buying' 'maint' 'doors' 'persons' log_boor' 'safety' 'clas'

def print_rule(rule):
    if len(rule)!=23:
        print "Longitud de cromosoma incorrecto"
        return

    tot_str=''
    for i in [0,4,8]:
        tot_str=tot_str+ rule[i]+rule[i+1]+rule[i+2]+rule[i+3]+" "

    for i in [12,15,18]:
        tot_str=tot_str+ rule[i]+rule[i+1]+rule[i+2]+" "

    tot_str=tot_str+rule[21]+rule[22]+" "        
    print tot_str

# Obtencion de las distancias d1 y d2 que determinaran
# los pares permitidos para la eleccion de puntos en
# el segundo cromosoma de cruce

def cromosome_distance(cromosome,conj_pos_list):
    r1=random.randint(0,len(cromosome))
    r2=random.randint(0,len(cromosome))
    d1=0
    d2=0

    while(r2==r1):
        r2=random.randint(0,len(cromosome))

    if r1>r2:
        aux=r1
        r1=r2
        r2=aux                
        
    d1=0
    r1_bkp=r1
    while(r1 not in conj_pos_list):
        r1-=1
        d1+=1

    d2=0
    r2_bkp=r2
    while(r2 not in conj_pos_list):
        r2-=1
        d2+=1

    r1=r1_bkp
    r2=r2_bkp
    return ((r1,d1),(r2,d2))

# Obteniene una lista de pares posibles (r1,r2) para el segundo cromosoma
# del crossover

def get_cromo_pos(cromosome,d1,d2):

    separators=separators_gen(cromosome)
    pos_list=[]
    for d1_cont in range(0,len(cromosome)):
        pos1=d1_cont-d1
        if pos1 in separators:
            for d2_cont in range(d1_cont,len(cromosome)):
                pos2=d2_cont-d2
                if (pos2 in separators):
                    pos_list.append((d1_cont,d2_cont))
                        
    return pos_list
    
# Obtener los fragmentos del cromosoma en base a
# a los puntos separados
def get_fragments(cromosome,pos_points):
    
    left_fr=cromosome[0:pos_points[0]]
    right_fr=cromosome[pos_points[1]:]
    center_fr=cromosome[pos_points[0]:pos_points[1]]

    l_total=len(left_fr)+len(right_fr)+len(center_fr)
    return (left_fr,center_fr,right_fr)

# Cruce de fragmentos de cromosomas
def cross_fragments(frag1,frag2):
    cross1=frag1[0]+frag2[1]+frag1[2]
    cross2=frag2[0]+frag1[1]+frag2[2]

    return (cross1,cross2)

# Determina los fragmentos a cruzar entre
# los cromosomas y devuelve el resultado
# del cruce

def crossover_gabil(c,c2):


    s=separators_gen(c)
    p=cromosome_distance(c,s)
    cp=get_cromo_pos(c2,p[0][1],p[1][1])

    r=random.randint(0,len(cp)-1)
    crom1=get_fragments(c2,cp[r])
    crom2=get_fragments(c,(p[0][0],p[1][0]))

    cross_result=cross_fragments(crom1,crom2)
    return cross_result

# Clasifica un atributo o valor del cromosoma
# de acuerdo a los valores de entrada
# Devuelve True si alguno concuerda, sino devuelve
# False

def classify_value(ind,crom_pos,rule):
    correct=False
        
    try:
        
        if (rule[ind+crom_pos]=='1'):            
            correct=True
    except IndexError:
        print "Error"
        print rule
        print ind+crom_pos
        raise
        


    return correct


# Determina si una regla clasifica correctamente
# un ejemplo y de ser asi devuelve el tipo
# de configuracion binaria correspondiente
# a la clasificacion
def classify(rule,example):
    
    num_example=range(0,6)
    cont=0
    for crom_pos in [0,4,8,12,15,18]:
        v=attributes[cont]
        ind=v.index(example[cont])
        cl_v=classify_value(ind,crom_pos,rule)

        if not cl_v:
            return 'not_classified'
        cont+=1

    final_class=rule[21:]
    fc=example[cont]

    if final_class=='00':
        if fc=='unacc':
            return 'ok'
    if final_class== '01':
        if fc=='acc':
            return 'ok'
    if final_class== '10':
        if fc=='good':
            return 'ok'
    if final_class== '11':
        if fc=='v-good':
            return 'ok'
        
    return 'not_classified'


# Por cada regla del cromosoma se encuentra
# el porcentaje de ejemplos calificados correctamente
# El fitness corresponde al promedio de estos porcentajes

def fitness(cromosome,examples):
    rules=split_rules(cromosome)        
    rules_class=[]

    for r in rules:
        rules_class.append(0)

    for e in examples:
        cont=0
        for r in rules:
            c=classify(r,e)
            if (c=='ok'):
                rules_class[cont]+=1
                
            cont+=1

    num_examples=len(examples)
    cont=0
    for r in rules_class:
        percentage=r*100/float(num_examples)
        rules_class[cont]=percentage
        cont+=1
        
    l=len(rules_class)
    acum=0
    cont=0
    for r in rules_class:
        acum+=rules_class[cont]
        cont+=1

    final_fit=acum/float(l)
    return final_fit

# Obtener una lista de listas de ejemplos
def get_examples(file_name):
    f=open(file_name)
    examples=f.readlines()
    split_list=[]

    for e in examples:
        split_list.append(e.replace('\n','').split(','))

    return split_list

# Metodo de seleccion de la ruleta
# Busca escoger una serie de cromosomas de acuerdo
# a su fitness

# Escoge (1-r)p cromosomas, donde p corresponde al numero
# de hipotesis a pasar para la siguiente generaci\'on
# y r la fraccion que sera cruzada en cada paso

def roulette_select(bound,crom_pool,examples,crom_fitness):

    # Lista de pares (fitness,cromosome) ordenados
    # inversamenta por fitness
    crom_fitness.sort(reverse=True)

    fit_sum=0
    for pair in crom_fitness:
        fit_sum+=pair[0]

    roulette_prob=[]
    w_prev=(crom_fitness[0][0])/float(fit_sum)
    roulette_prob.append((w_prev,crom_fitness[0][1]))

    # Construccion de arreglo de pares (probabilidad,cromosoma)
    for c in range(1,len(crom_fitness)):
        w_prev=w_prev+(crom_fitness[c][0]/float(fit_sum))
        roulette_prob.append((w_prev,crom_fitness[c][1])) 
        
    # Se escoge un numero aleatorio entre 0 y 1
    # del arreglo de pares
    # Se escoge el mas cercano en probabilidad

    # (1-cross_fraction)next_n deciden el numero de miembros a elegir

    #Lista de la nueva generacion
    next_generation=[]
    cont=0
    # Agregar bound numero de cromosomas
    while (cont<bound):

        pos_rnd=random.random()
        added=False
        for rpos in range(0,len(roulette_prob)-1):
            if pos_rnd >= roulette_prob[rpos][0] and not added and roulette_prob[rpos+1][0]>=pos_rnd:

                try:
                    if (next_generation.index((roulette_prob[rpos][1]))>=0):
                        cont=cont
                except ValueError:
                    next_generation.append(roulette_prob[rpos][1])
                    added=True                    
                
        if not added:
            rnd_pos=random.randint(0,len(roulette_prob)-1)
            next_generation.append(roulette_prob[rnd_pos][1])

        cont+=1
    return next_generation

# Metodo de seleccion por torneo. Escoge aleatoriamente pares
# de cromosomas del pool y pasa a la generacion el mas apto
# en el torneo entre pares

def tournament_select(bound,crom_pool,examples,crom_fitness):
    next_generation=[]
    fit_sum=0
    for pair in crom_fitness:
        fit_sum+=pair[0]

    for i in range(0,int(bound)):
        if len(crom_fitness)==0:
            break
    
        # Se eligen dos elementos para hacer torneo
        r1=random.randint(0,len(crom_fitness)-1)
        t1=crom_fitness[r1]
        
        r2=random.randint(0,len(crom_fitness)-1)
        t2=crom_fitness[r2]
        
        p1=t1[0]
        p2=t2[0]

        if (p1>=p2):
            next_generation.append(t1[1])
            del(crom_fitness[r1])
        else:
            next_generation.append(t2[1])
            del(crom_fitness[r2])

    return next_generation

# Metodo de seleccion de la SUS:stochastic universal
# sampling. Elige fraccionalmente de acuerdo a un
# ordenamiento probabilistico

def sus_select(bound,crom_pool,examples,crom_fitness):

    # Lista de pares (fitness,cromosome) ordenados
    # inversamenta por fitness
    crom_fitness.sort(reverse=True)

    fit_sum=0
    for pair in crom_fitness:
        fit_sum+=pair[0]

    roulette_prob=[]
    w_prev=(crom_fitness[0][0])/float(fit_sum)
    roulette_prob.append((w_prev,crom_fitness[0][1]))

    # Construccion de arreglo de pares (probabilidad,cromosoma)
    for c in range(1,len(crom_fitness)):
        w_prev=w_prev+(crom_fitness[c][0]/float(fit_sum))
        roulette_prob.append((w_prev,crom_fitness[c][1])) 
        
    #Lista de la nueva generacion
    next_generation=[]
    cont=0
    salto=0.16
    actual_pos=random.random()*salto
    
    # A partir de un elemento random entre 0-F/N
    # se escogen elementos de la ruleta con un
    # salto de F/N, donde F: suma total de los fitness
    # y N: numero de elementos
    
    while (cont<bound):

        added=False
        for rpos in range(0,len(roulette_prob)-1):
            if actual_pos >= roulette_prob[rpos][0] and not added and roulette_prob[rpos+1][0]>=actual_pos:
                try:
                    if (next_generation.index((roulette_prob[rpos][1]))>=0):
                        cont=cont
                except ValueError:
                    next_generation.append(roulette_prob[rpos][1])
                    added=True
        
        actual_pos+=salto
        # Dar la vuelta a la ruleta
        if (actual_pos>1):
            actual_pos-=1

        if not added:
            rnd_pos=random.randint(0,len(roulette_prob)-1)
            next_generation.append(roulette_prob[rnd_pos][1])

        cont+=1

    return next_generation


# Se genera una lista de num_crom cromosomas
# aleatorios con un numero variable de reglas
# 2-11

def rnd_cromosomes_gen(num_crom):

    crom_pool=[]
    for i in range(0,num_crom):
        num_rules=random.randint(2,8)
        new_rule=''
        for i in range(0,num_rules):
            for i in range(0,23):
                new_rule+=str(random.randint(0,1))
        crom_pool.append(new_rule)

    return crom_pool


# Formar pares de cromosomas para el crossover
def make_cromosomes_pair(cromosome_list):
    pair_list=[]
    rango=range(0,len(cromosome_list),2)
    for i in rango:
        if not (i+1>=len(cromosome_list)):
            pair_list.append((cromosome_list[i],cromosome_list[i+1]))

    return pair_list

# Escoge num_mutate cromosomas de la lista
# para mutarlos: cambiar aleatoriamente un bit
def mutate(num_mutate,cromosome_list):
    for i in range(0,num_mutate):
        chose=random.randint(0,len(cromosome_list)-1)
        cromosome=cromosome_list[chose]
        mutate_bit=random.randint(0,len(cromosome)-1)
        change='1'
        if (cromosome[mutate_bit]=='0'):
            change='1'
        else:
            change='0'

        new_crom=''
        for i in range(0,len(cromosome)):
            if i==mutate_bit:                
                new_crom+=change
            else:
                new_crom+=cromosome[i]

        cromosome_list[chose]=new_crom
                
    return cromosome_list

# Calcula el fitness de cada elemento del pool
# y devuelve una lista de pares (fitness,cromosoma)
def calculate_fitness(pool,examples):
    crom_fitness=[]
    for cromosome in pool:
        crom_fitness.append((fitness(cromosome,examples),cromosome))                    

    return crom_fitness

# Extension de gabil
def add_alternative(cromosome):
    new_crom=''
    for i in range(0,len(cromosome)):
        if cromosome[i]=='0':            
            r=random.randint(0,100)
            if r==33:
                new_crom+='1'
            else:
                new_crom+=cromosome[i]
        else:
            new_crom+='1'
    return new_crom

# Algoritmo genetico GABIL
# Encuentra el cromosoma mas apto para la clasificacion de un conjunto de ejemplos.

# Parametros:
#
# fitness_treshold: Cota para detener las iteraciones
# num_cromosomes: Numero de cromosomas a pasar a la siguiente generacion
# cross_frac: Fraccion de cromosomas que seran escogidos para crossover
# mutation_rate: Fraccion de cromosomas que seran escogidos para mutacion
# file_name: nombre del archivo que contiene los ejemplos a clasificar
# selection: tipo de seleccion a utilizar -> 'roulette','sus' o 'tournament'
# extension: Extension de GABIL a utilizar: 0: Ninguna 1: addAlternative

def gabil_ga(fitness_threshold,num_cromosomes,cross_frac,mutation_rate,file_name,selection,extension):
    #Inicializacion de la poblacion
    pool=rnd_cromosomes_gen(num_cromosomes)
    #Calculo de fitness por cromosoma
    examples=get_examples(file_name)
    crom_fitness=calculate_fitness(pool,examples)
    best_cromosome=crom_fitness[0]

    while(max(crom_fitness)[0]<fitness_threshold):
        # Seleccion de los primeros (1-cross_frac)*num_cromosomes
        bound=(1-cross_frac)*num_cromosomes
        if selection=='roulette':
            select=roulette_select(bound,pool,examples,crom_fitness)
        elif selection=='sus':
            select=sus_select(bound,pool,examples,crom_fitness)
        elif selection=='tournament':
            select=tournament_select(bound,pool,examples,crom_fitness)
  
        #Crossover
        bound=(cross_frac*num_cromosomes)

        if selection=='roulette':
            cross_select=roulette_select(bound,pool,examples,crom_fitness)
        elif selection=='sus':
            cross_select=sus_select(bound,pool,examples,crom_fitness)
        elif selection=='tournament':
            cross_select=tournament_select(bound,pool,examples,crom_fitness)
        
        cross_select=make_cromosomes_pair(cross_select)
        new_pool=[]
        # Se agregan los pares cruzados al new_pool
        for cpair in cross_select:
            c=[]
            if (cpair[0]!=cpair[1]):
                c=crossover_gabil(cpair[0],cpair[1])            
            else:
                c.append(cpair[0])
                c.append(cpair[1])

            
            rango=range(46,185,23)
            if len(c[0]) not in rango:
                new_pool.append(cpair[0])
            else:
                new_pool.append(c[0])
            if len(c[1]) not in rango:
                new_pool.append(cpair[1])
            else:
                new_pool.append(c[1])
            
        # Se agregan los pares seleccionados por ruleta
        # al new_pool
        for s in select:
            new_pool.append(s)
        
        num_mutate=int(mutation_rate*num_cromosomes)
        new_pool=mutate(num_mutate,new_pool)

        if extension=='1':
            
            alternative_pool=[]
            for c in new_pool:
                rc=add_alternative(c)            
                alternative_pool.append(rc)
                
            new_pool=alternative_pool
            
        
        pool=new_pool
        crom_fitness=calculate_fitness(pool,examples)
        maxf= max(crom_fitness)[0]

        print max(crom_fitness)
        if (maxf>best_cromosome[0]):
            best_cromosome=(maxf,best_cromosome[1])

    print "\n El mejor cromosoma: "
    print best_cromosome
    return max(crom_fitness)

    
print gabil_ga(20,20,0.50,0.1,'car.data','roulette','1')
