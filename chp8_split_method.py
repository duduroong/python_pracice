fname = input("Enter file name: ")
fh = open(fname)
lst = list()  #blank list

for line in fh:
    lines = line.rstrip()  #erase the /n(new line character)
    words = lines.split()  #split the sentence by words, so that store them in the list[]
    for word in words : #for any string in the list[words]
        if word not in lst :
            lst.append(word)   #store the words in list without overlap
lst.sort() #sort words
print(lst)
