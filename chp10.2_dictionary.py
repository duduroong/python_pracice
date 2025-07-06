name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d= dict()
for line in handle :
    line = line.rstrip()
    if line.startswith("From ") :
        words = line.split()
        time = words[5] #find the time
        #print(time)
        time = time.split(":") #split by ":" and store them in format of list[]
        hour = time[0]  
        #print(hour)
        d[hour]=d.get(hour,0)+1  #d[hour] = store hour in a dictionary() as a key, d.get(hour,0)+1 = count how many times the key 'hour' appears
#print(d)

for hour in sorted(d): #sort a dictionary by key
    print(hour,d[hour]) #d[hour] = key
