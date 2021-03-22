#first function is fuctorial function:
def fuctorial (num:int):
    factorial_sum = num
    while num-1 > 0:
        factorial_sum = factorial_sum * (num-1)
        num -= 1
    return factorial_sum


#abs funcion
def absolut_value (x:float):
    if x < 0:
        return -x
    else: 
        return x

#second function is pow for the expodent:
def pow (x:float, y:int):
        sum = x
        for i in range(1,y):
            sum = sum * x
        return sum



#third function is expodnent:
def exponent (x:float):
    i = 1
    sum = 1
    while (absolut_value((x)/fuctorial(i)) > 0.00000000000000000000000000000000000000000001) & (i <= 5000000000):
        sum += (pow(x, i))/(fuctorial(i))
        i += 1
    return sum


#forth function is Ln:
def Ln (x:float):
    if x > 0:
        y_0 = x - 1.0
        y_2 = 0
        while True:
            y_2 = y_0 + 2 * (x - exponent(y_0))/(x + exponent(y_0))
            if absolut_value(y_0 - y_2) <= 0.001:
                return y_0
            y_0 = y_2
    else:
        return 0
        
#ln_value = float('%0.6f' % Ln(5.0))
#print(ln_value)



#the FIRST MAIN function XtimesY:
def XtimesY(x:float, y:float):
        if x >= 0:
            return (exponent(y * Ln(x)))
        else:
            return 0        
        



#sqrt function:
def sqrt (x:float, y:float):
    return XtimesY(y, 1/x)



#final function calculate formula:
def calculate (x:float):
    if x>=0:
        return (exponent(x) * XtimesY(7.0, x) * XtimesY(x, -1.0) * sqrt(x, x))
    else:
        return 0.0
    
