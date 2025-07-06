# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)   #open the file
for line in fh :
    line = line.rstrip()  #erase \n (newline character)
    print(line.upper())   
