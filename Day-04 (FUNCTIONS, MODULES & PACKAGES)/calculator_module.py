# In calculator_funtions, we have hard-coded values. that is not recommended
# Instead of that we use modularized approach for reusability
# Here we define values in where we invoking function in prev example
# Instead of print in function, we use return here 

def add(x, y):
    a = x + y
    return a
def sub(x, y):
    s = x - y
    return s
def mul(x, y):
    m = x * y
    return m
def div(x, y):
    d = x / y
    return d

print(add (10, 2))
print(sub(20, 10))
print(mul(2, 5))
print(div(8, 4))