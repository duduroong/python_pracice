hrs = input("Enter Hours:") #input of working hours
h = float(hrs)  #convert from string to floating nums
rate = input("Enter pay rates:")  #input of pay rates
pr = float(rate) #convert from string to floating nums

if h <40:
    pay = h*pr
else :
    pay = 40*pr+(h-40)*pr*1.5   #calculate overtime pay
    
print(pay) 
