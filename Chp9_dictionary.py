name = input("Enter file:")
if len(name) < 1:     
    name = "mbox-short.txt"     #if users don't input a file, initial value would be "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle :
    line = line.rstrip()
    if line.startswith("From ") :
        words = line.split()
        address = words[1]   #get email address 
        d[address] = d.get(address,0)+1. #address is stored in dict() as a key, and then count it
        
max_a = 0
max_c = 0

for address, count in d.items() :   #in dict(), address is a key and count is a value
    if count > max_c :
        max_c = count
        max_a = address  #find the maximum of count value and that of key address
        
print(max_a, max_c)
