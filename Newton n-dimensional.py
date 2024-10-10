import numpy as np

# Define the function
def f(x, y):
    return np.exp(x) + np.exp(y) + 2*x**2 + 3*y**2 -5*x -4*y

# Define the gradient
def grad_f(x, y):
    df_dx = np.exp(x) + 4*x - 5
    df_dy = np.exp(y) + 6*y - 4
    return np.array([df_dx, df_dy])

# Define the Hessian
def hessian_f(x,y):
    return np.array([[np.exp(x) + 4, 0], [0, np.exp(y) + 6]])

# Newton's method
def newtons_method(x0, y0, tol=1e-6, max_iter=100):
    point = np.array([x0, y0])
    for i in range(max_iter):
        grad = grad_f(point[0], point[1])
        hessian = hessian_f(point[0], point[1])
        
        # Solve H * delta_x = -grad for delta_x
        delta_x = np.linalg.solve(hessian, -grad)
        
        # Update point
        new_point = point + delta_x
        
        # Compute function value and error
        func_val = f(new_point[0], new_point[1])
        error = np.linalg.norm(delta_x)
        
        # Print the point, function value, and error for each iteration
        print(i+1, new_point, {func_val}, error)
        #print(f"Iteration {i+1}: Point = {new_point}, f(Point) = {func_val}, Error = {error}")
        
        # Check if error is below tolerance
        if error < tol:
            break
        
        # Update the point for the next iteration
        point = new_point

# Initial guess
newtons_method(0,0)
