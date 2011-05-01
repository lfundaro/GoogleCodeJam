#! /usr/bin/python

def prepare_string(string):
    string = string.split(' ')
    for i in range(len(string)):
        string[i] = string[i].strip('\n')
        string[i] = int(string[i])
    return string
