import math

def biseccion(a, b, f, tol):
    if f(a)*f(b) > 0:
        return "Escoja otro intervalo o función que cumpla las condiciones"
    
    while abs(b-a) > tol:
        p = a + (b-a)/2
        fp = f(p)
        f2 = f(b)
        if fp*f2 > 0:
            b = p
        elif fp*f2 < 0:
            a = p
        else: 
            return p
    return p

print(biseccion(0,1, f = lambda x: 4*math.exp(4*x)+3*math.exp(3*x)+118*x-32, tol = 0.00001))

        

        
