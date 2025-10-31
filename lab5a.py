#!/usr/bin/env python3
# Author ID: Vaidehi Patel - 166249219

def read_file_string(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    lines = data.split('\n')
    if len(lines) > 0 and lines[-1] == '':
        lines.pop()
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))


