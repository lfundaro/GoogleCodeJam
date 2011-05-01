#
# Backpropagation
#
# Comienzo de modificacion para
# proyecto final -> hot or not <-

import random
from math import exp
import Gnuplot

#Producto punto de entradas y pesos para una unidad
def test_sum(ex,weights):
    parcial_sum=0
    for w in range(len(weights)):
        parcial_sum=(weights[w]*ex[w])+parcial_sum        

    return parcial_sum

#Producto punto de entradas y pesos para una unidad
def test_sum_init(ex,weights,w0):
    parcial_sum=w0
    for w in range(len(weights)):
        parcial_sum=(weights[w]*ex[w])+parcial_sum        

    return parcial_sum


# Funcion de sigmoid o de logistica
def sigmoid(parcial_sum):
    return (1/(1+(exp(-1*parcial_sum))))

# backpropagation: Implementacion del algoritmo de backpropagation
# con un numero de neuronas de entrada 'input_units', un numero de
# neuronas escondidas de la primera capa 'hidden_units_first',
# el numero de neuronas escondidas de la segunda capa 'hidden_units_second'
# un numero de neuronas de salida 'output_units' y una cota bound de iteracion

def backpropagation_training(examples,input_units,hidden_units_first,hidden_units_second,output_units,n,bound):

    # Se calculan pesos aleatorios entre -0.05 y 0.05 para las
    # unidades escondidas y las unidades de salida
    hidden_weights_first=init_hidden_weights(hidden_units_first,input_units)
    hidden_weights_second=init_hidden_weights(hidden_units_second,hidden_units_first)
    output_weights=init_output_weights(hidden_units_second)
    w0=init_output_weights(hidden_units_first)

    h_outputs_first=[0 for i in range(hidden_units_first)]
    h_outputs_second=[0 for i in range(hidden_units_second)]
    o_output=0
    
    num_it=0
    while(num_it<bound):
        num_it+=1
          
        for e in examples:
            # Propagacion de las entradas a traves
            # de la red
            
            # Valor esperado del ejemplo
            example_target=e[len(e)-1]
            
            # Calculo de valor sigmoid por cada
            # unidad de entrada.
            # Primera capa de hidden units            
            for hw1 in range(hidden_units_first):
                h_outputs_first[hw1]=sigmoid(test_sum_init(e,hidden_weights_first[hw1],w0[hw1]))
                
            # Segunda capa de hidden units
            for hw2 in range(hidden_units_second):
                h_outputs_second[hw2]=sigmoid(test_sum(h_outputs_first,hidden_weights_second[hw2]))

            # Unidad de salida
            output_sum=sigmoid(test_sum(h_outputs_second,output_weights))

            ##--->>> Propagacion hacia atras <<<---###

            # Error para una unica unidad de salida
            output_error=output_sum*(1-output_sum)*(example_target-output_sum)

            # Error para los hidden units
            # Segunda capa
            hidden_errors_second=[0 for i in range(hidden_units_second)]
            for hd_2 in range(hidden_units_second):
                hidden_errors_second[hd_2]=h_outputs_second[hd_2]*(1-h_outputs_second[hd_2])*(output_weights[hd_2]*output_error)

            # Primera capa
            hidden_errors_first=[0 for i in range(hidden_units_first)]
            for hd_1 in range(hidden_units_first):
                acum_error=0
                for k in range(hidden_units_second):
                    acum_error+=hidden_weights_second[k][hd_1]*hidden_errors_second[k]                    
                
                hidden_errors_first[hd_1]=h_outputs_first[hd_1]*(1-h_outputs_first[hd_1])*acum_error        

            # Actualizacion de los pesos de la red

            # Pesos hidden<->output
            for ow in range(hidden_units_second):
                output_weights[ow]+=(n*output_error*h_outputs_second[ow])

            # Pesos inputs<->hidden
            # Segunda capa
            
            for hw_2 in range(hidden_units_second):
                for hw_1 in range(hidden_units_first):
                    hidden_weights_second[hw_2][hw_1]+=n*(hidden_errors_second[hw_2]*h_outputs_first[hw_1])

            # Primera capa
            for hw_1 in range(hidden_units_first):
                for inp in range(input_units):
                    hidden_weights_first[hw_1][inp]+=n*(hidden_errors_first[hw_1]*e[inp])
                w0[hw_1]+=n*hidden_errors_first[hw_1]
          
    total_weights=[hidden_weights_first,hidden_weights_second,output_weights,w0]
    return total_weights


def backpropagation_running(examples,input_units,hidden_units_first,hidden_units_second,output_units,hidden_weights_first,hidden_weights_second,output_weights,w0):

    h_outputs_first=[0 for i in range(hidden_units_first)]
    h_outputs_second=[0 for i in range(hidden_units_second)]
    o_output=0

    for e in examples:
        # Propagacion de las entradas a traves
        # de la red
            
        # Calculo de valor sigmoid por cada
        # unidad de entrada
        # Primera capa de hidden units            
        for hw1 in range(hidden_units_first):
            h_outputs_first[hw1]=sigmoid(test_sum_init(e,hidden_weights_first[hw1],w0[hw1]))
                
        # Segunda capa de hidden units
        for hw2 in range(hidden_units_second):
            h_outputs_second[hw2]=sigmoid(test_sum(h_outputs_first,hidden_weights_second[hw2]))

        # Unidad de salida
        output_sum=sigmoid(test_sum(h_outputs_second,output_weights))

        print output_sum


# Genera una lista de num_units elementos.
# Cada elemento es una lista de num_weights
# valores reales entre -0.05 y 0.05
 
def init_hidden_weights(num_units,num_weights):
    hidden_weights=[]
    for i in range(0,num_units):
        weights=[]
        for j in range(0,num_weights):
            weights.append(random.uniform(-0.05,0.05))
        hidden_weights.append(weights)
        
    return hidden_weights

# Genera una lista de num_weights elementos.
# de valores reales entre -0.05 y 0.05
 
def init_output_weights(num_weights):
    output_weights=[]
    for j in range(0,num_weights):
        output_weights.append(random.uniform(-0.05,0.05))
        
    return output_weights

# Ejemplos de entrenamiento
examples=[]
for i in range(200):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    examples.append((x,y,(x+y)/2))

run_ex=[]
for i in range(10):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    run_ex.append((x,y,(x+y)/2))

for i in run_ex:
    print i

o=backpropagation_training(examples,2,5,5,1,1,350)
backpropagation_running(run_ex,2,5,5,1,o[0],o[1],o[2],o[3])
