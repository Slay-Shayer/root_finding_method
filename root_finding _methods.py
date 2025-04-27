import numpy as np



def f(x):
    return (np.exp(x)* (np.sin(x) + np.cos(x)))

# The derivative may change with the function which must be calculated manually
# The return of derivative of the given function cannot be 0 (Which will lead error for the Newton-Rhapson Method)

def ddx_f(x):
    return (2 * np.exp(x) * np.cos(x))  # The deriative of the function of function f

################## Root Finding Method #######################


# Setting the tolerance and max interation values for each root finding method

max_iterations = 100
tolerance = 1e-10

# Bisection Method

def bisection(f, a, b):
    c = 5 # The initial value of c, which means nothing
    iterations = 0
    if f(a) * f(b) < 0:
        while c!= 0 and iterations < max_iterations and abs(f(c)) > tolerance:
            c = (a+b)/2 # The midpoint for finding the value of c
            if f(c) * f(a) < 0:
                b = c
            else:
                a = c
            iterations += 1
        return c, iterations
    else:
        print("ValueError")
        return None, None
    


c, iterations = bisection(f, 2, 3) # Must add the c and iterations to assign the retuerned value


# Regula-Falsi Method

def falsi(f, a, b):
    c1 = 5 # The initial value of c, which means nothing
    iterations1 = 0
    if f(a) * f(b) < 0:
        while c1!= 0 and iterations1 < max_iterations and abs(f(c1)) > tolerance:
            c1 = (a*f(b) - b*f(a))/(f(b) - f(a)) # Using the different approach for c
            if f(c1) * f(a) < 0:
                b = c1
            else:
                a = c1
            iterations1 += 1
        return c1, iterations1
    else:
        print("ValueError")
        return None, None
    
c1, iterations1 = falsi(f, 2, 3) # Must assign the c1 and iterations1 to assign the retuerned value



# Newton Rhapson in Code  

def newton_rhapson(f, ddx_f, x):
    interations2 = 0
    for i in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x, i+1 # If the iteration meets this given condition for tolerance then the loop will break and return its results
        dfx = ddx_f(x)
        if dfx == 0:
            raise ValueError("Zero derivative. No solution Found") # Just in case if the derivative is equal to zero the code will output by error
        x = x - fx/dfx  # The formula of newton Rhapson has been shown here
        i =+1
    return x, max_iterations


x, iterations2 = newton_rhapson(f, ddx_f, 2) 

# Displaying the Final Result   

if iterations > iterations1:
    
    print(f"Bisection Method - {str(f)} is: {c:.10f} (iterations: {iterations})\n")
    
    print(f"Regula-Falsi - {str(f)} is: {c1:.10f} (iterations: {iterations1})\n")
  
    print(f"Newton Rhapason - {str(f)} is: {x:.10f} (iterations: {iterations2})\n")
    
    print(f"Bisection Method took {iterations - iterations1} more iterations in order to find the root than the Regula-Falsi Method.\n")
    
    print(f"Regula-Falsi Method took {iterations1 - iterations2} more iterations in order to find the root than the Newton-Rhapson Method.\n")
    
    
