#!/usr/bin/env python3
# Author ID: Vaidehi Patel - 166249219

def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        sum = int(number1) + int(number2)
        return sum
    except (TypeError, ValueError):  
        #print('error: could not add numbers')
        #raise
        return('error: could not add numbers')

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        data = f.readlines()
        f.close()
        return data
    except FileNotFoundError:
        #print('error: could not read file')
        return('error: could not read file')

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception



