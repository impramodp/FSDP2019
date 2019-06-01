""" Code challenge to create a command to copy a file

file_name - 'copy_file.py'

"""

# copy 'words.txt' into 'abc.txt'

copy_file = open('abc.txt','wt')
with open('words.txt','rt') as file:
    for text in file.readlines():
        copy_file.write(text)
copy_file.close()