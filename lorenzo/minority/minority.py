#! /usr/bin/python

import sys

def minority(T, length):
    if length <= 1:
        return T
    mid = length / 2
    left = minority(T[:mid], mid)
    right = minority(T[mid:], length - mid)
    
    if left == []:
        return right
    elif right == []:
        return left
    if left[-1] >= right[0]:
        return eliminate(left, right)
    else:
        left.extend(right)
        return left


def eliminate(left, right):
    r_len = len(right)
    l_len = len(left)
    result = []

    while r_len > 0 and l_len > 0:
        if left[0] == right[0]:
            left = left[1:]
            right = right[1:]
            l_len -= 1
            r_len -= 1
        elif left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
            l_len -= 1
        else:
            result.append(right[0])
            right = right[1:]
            r_len -= 1
        
    if l_len == 0:
        result.extend(right)
        return result
    else:
        result.extend(left)
        return result


f = file(sys.argv[1], 'r')
cases = int(f.readline())

for times in range(cases):
    length = f.readline() # reading number of elements 
    str_list = f.readline() # reading list as string 
    str_list = str_list.split(' ')
    for i in range(len(str_list)):
        str_list[i] = str_list[i].strip('\n')
    T = []
    for i in str_list:
        T.append(int(i))
    answer = minority(T, int(length))
    print 'Case #' + str(times + 1) + ': ' +  str(answer[0])

