#! /usr/bin/python

import sys

def prepare_string(string):
    string = string.split(' ')
    for i in range(len(string)):
        string[i] = string[i].strip('\n')
        string[i] = int(string[i])
    return string

def init_list(N):
    map = []
    for i in range(N):
        map.append([0,[]])
    return map

def order_map(map):
    for i in map:
        i[1].sort(reverse = True)
        
def to_work(map, T, N):
    result = []
    for i in range(N):
        result.append(0)

    before = map[:T]
    after = map[T+1:]

    b = 0
    for elem in before:
        while elem[0] > 0:
            if elem[1] == [] or elem[1][0] == 0:
                return 'IMPOSSIBLE'            

            if elem[0] > elem[1][0]:
                elem[0] = elem[0] - elem[1][0]
                elem[1] = elem[1][1:]
                result[b] += 1
            elif elem[0] <= elem[1][0]:
                elem[0] = 0
                result[b] += 1 
                
        b += 1

    a = T + 1
    for elem in after:
        while elem[0] > 0:
            if elem[1] == [] or elem[1][0] == 0:
                return 'IMPOSSIBLE'            

            if elem[0] > elem[1][0]:
                elem[0] = elem[0] - elem[1][0]
                elem[1] = elem[1][1:]
                result[a] += 1
            elif elem[0] <= elem[1][0]:
                elem[0] = 0
                result[a] += 1

        a += 1
        
    min_cars = ''
    for cars in result:
        min_cars = min_cars + str(cars) + ' '

    return min_cars

f = file(sys.argv[1], 'r')
cases = int(f.readline())

for times in range(cases):
    towns = prepare_string(f.readline())
    T = towns[1]
    N = towns[0]
    map = init_list(N)
    employees = prepare_string(f.readline())
    for i in range(employees[0]):
        ins = prepare_string(f.readline())
        map[ins[0]-1][0] += 1
        map[ins[0]-1][1].append(ins[1])
    order_map(map)
    answer = to_work(map, T - 1, N)
    print 'Case #' + str(times + 1) + ': ' + answer.strip(' ')
