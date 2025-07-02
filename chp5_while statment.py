largest = None #no values yet
smallest = None #no values yet
while True: #indefinite loop
    num = input("Enter a number: ")
    if num == "done":
        break #exit the loop
    try :
        numb = int(num) #convert string to integer
    except :
        print('Invalid input')
        continue  #Error handling for non-numeric input
        
    if largest is None :
        largest = numb
    elif largest < numb :
        largest = numb

    if smallest is None :
        smallest = numb
    elif smallest > numb :
        smallest = numb

print("Maximum is", largest)
print('Minimum is', smallest) 
