#!/usr/bin/env python3

def read_file_string(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    # Return list of lines without the trailing '\n'
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    #return data
    lines = data.split('\n') 
    if len(lines) > 0 and lines[-1] == '': 
        lines.pop()
    return lines

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(str(string_of_lines))
    f.close()
    

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    #f.write(str(list_of_lines) + '\n')
    for items in list_of_lines:
        f.write(str(items) + '\n')
    f.close()
    
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    readfile = open(file_name_read, 'r')
    writefile = open(file_name_write, 'w')

    readdata = readfile.read()
    #f.close()
    
    for lines_of_readfile in readdata:
        lines_of_readfile = readdata.split('\n')
        if len(lines_of_readfile) > 0 and lines_of_readfile[-1] == "":
            lines_of_readfile.pop()
        #return lines

    #f = open(file_name_write, 'w')
    i = 1
    
    for data in lines_of_readfile:
        writefile.write(str(i) + ":"  + str(data) + '\n')
        i += 1
    #writefile.close()
    #return file_name_write

    readfile.close()
    writefile.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
