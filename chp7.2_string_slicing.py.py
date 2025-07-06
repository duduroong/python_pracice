# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
ttl = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        value = line[len("X-DSPAM-Confidence:"):].rstrip() #slicing to find the floating number
        num = float(value)
        ttl = ttl+num
average = ttl/count
print("Average spam confidence:", average)
