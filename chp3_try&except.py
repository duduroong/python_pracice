score = input("Enter Score: ")
try:
    scr = float(score)
except:       #if errors occur in try statement, proceed this code
    print("Error, plz input numeric value")
    quit()
if scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
else:
    print("F")
