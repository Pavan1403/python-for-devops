## Task 1: Arithmetic Operators
##  Create two variables `a` and `b` with numeric values.
##  Calculate the sum, difference, product, and quotient of `a` and `b`.
##  Print the results.
a = 5
b = 15
print(a + b)
print(a - b)
print(a * b)
print(a / b)
## Task 2: Comparison Operators
##  Compare the values of `a` and `b` using the following comparison operators: `<`, `>`, `<=`, `>=`, `==`, and `!=`.
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
##  Task 3: Logical Operators
##  Create two boolean variables, `x` and `y`.
##  Use logical operators (`and`, `or`, `not`) to perform various logical operations on `x` and `y`.
x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)
##  Task 4: Assignment Operators
##  Create a variable `total` and initialize it to 10.
##  Use assignment operators (`+=`, `-=`, `*=`, `/=`) to update the value of `total`.
total = 10
total += 5
print(total)
total *= 2
print(total)
total -= 10
print(total)
total /= 5
print(total)
##  Task 6: Identity and Membership Operators
##  Create a list `my_list` containing a few elements.
##  Use identity operators (`is` and `is not`) to check if two variables are the same object.
##  Use membership operators (`in` and `not in`) to check if an element is present in `my_list`.
##  It will only print boolean data types , True or False
my_list = [1, 2, 3, 4, 5]
numbers = my_list

is_operator = my_list is numbers
is_not_operator = my_list is not numbers
print (is_operator)
print (is_not_operator)

in_operator = 5 in my_list
not_in_oprator = 6 not in my_list
print(in_operator)
print(not_in_oprator)
