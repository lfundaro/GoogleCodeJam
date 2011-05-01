#! /usr/bin/python

import sys

def translate(line, test_num):
    parts = line.split(' ')
    for i in range(len(parts)):
        parts[i] = parts[i].strip('\n')

    alien_value = value(parts[0], parts[1])
    target_base = len(parts[2])
    stack = []
    stack.append(alien_value % target_base)
    div = alien_value / target_base
    while div != 0:
        stack.append(div % target_base)
        div = div / target_base

    result = ''
    while stack:
        result = result + parts[2][stack.pop()]

    print 'Case #' + str(test_num)  + ':' + ' ' + result
        
    
def value(digits, source):
    dig_len = len(digits)
    base = len(source)
    val = 0
    for i in reversed(range(dig_len)):
        val = val + source.find(digits[dig_len - i - 1]) * (base ** i)

    return val
        
    
f = file(sys.argv[1], 'r')
cases = int(f.readline())

for times in range(cases):
    translate(f.readline(), times + 1)


