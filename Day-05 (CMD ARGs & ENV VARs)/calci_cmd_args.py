#   Command-line arguments in Python allow you to pass input to a script when executing it from the command line.
#   This is useful for dynamically controlling the behavior of a script, such as specifying file names, options, or other parameters.
#   Sys package, consists of lot of inbuild modules & most commonly used functions in python.

import sys                  

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

num1 = float(sys.argv[1])   # HERE BY USING CMD ARGS, WE ARE RUNNING CODE WITH OUT OPENING FILE
operation = sys.argv[2]     # WE CAN CALL THE OPERATION IN THE COMMAND LINE
num2 = float(sys.argv[3])   # HERE WE ARE USING CALCULATOR, SO WE NEED TO CONVERT INTO INT OR FLOAT, OR ELSE PYTHON WILL TAKE IT AS STRINGS

if operation == "add":
    print(add(num1, num2))
if operation == "sub":
    print(sub(num1, num2))
if operation == "mul":
    print(mul(num1, num2))
if operation == "div":
    print(div(num1, num2))

#   To run this file --> python filename arg1(value1) operation arg2(value2)
#                 ex --> python calci_cmd_args.py 2 add 3