def computepay(h, r):  #define new function
    if h < 40 :
        return h*r
    else :      #if working hours >40, calculate the overtime pay
        return 40*r + (h-40)*r*1.5

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rates:")
r = float(rate)

p = computepay(h,r)
print("Pay", p)
