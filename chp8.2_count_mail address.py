fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh : 
    line = line.rstrip()  #erase /n (newline character)
    if line.startswith('From '):  #find the line including a mail address
        words = line.split()   #split the line by words
        address = words[1] #find the mail address
        print(address)
        count += 1   #count the mail addresses

print("There were", count, "lines in the file with From as the first word")
