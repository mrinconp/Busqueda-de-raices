import math

def secante(x0, x1, Df, tol, tope):
    f = lambda x: math.exp(4*x)+math.exp(3*x)+59*x**2-32*x
    for i in range(tope):
        x2 = x1 - (x1 - x0)*Df(x1)/(Df(x1) - Df(x0))
        
        if abs(Df(x2)-Df(x1)) < tol:
            print(i+1, x0, x1, x2,f(x2), abs(x2-x1))
            return 


        print(i+1, x0, x1, x2,f(x2), abs(x2-x1))

        x0 = x1
        x1 = x2

        
        

print(secante(x0= 0, x1 = 1, Df = lambda x: 4*math.exp(4*x)+3*math.exp(3*x)+118*x-32, tol = 0.00001, tope= 100))