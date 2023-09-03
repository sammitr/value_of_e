
deci_limit = int(input("How many digits do you want to calculate(upto 16) = ")) #user input for the amount of decimal places to calculate

e = 1 #Initializing variables
n = 1

def factorial(n):  #function to calculate factorial
    if n == 0 or n == 1: 
        return 1
    else:
        range_lim = n 
        for i2 in range(1, range_lim):
            n = n * i2
        return n   
            
 
 
for i in range(1, (deci_limit + 15) + 1):
    e = e + 1/factorial(i) #formula to calculate e
    
    
print(round(e, deci_limit)) #rounding off value of e to number requested by user and final print

