a = ("Pavan")
b = ("Kalluri")
ab = a + " " + b
text = "    need to remove extra spaces using strip"
substring = "to"
print(ab)
print(len(ab))
print(ab.lower())
print(ab.upper())
print(ab.split())
print(text.strip())
if substring in text : print (substring)
#################################
x = 10
y = 20
print (x + y)
print (x - y)
print (x * y)
print (x % y) # Reminder will come as output
print (x / y)
print (y // x)
#################################
import re

text = "Welcome to the python for devops course"
pattern = r"python"
replace = "PowerShell"
search = re.search(pattern, text) # Perform the search
if search: print("Python Found:", search.group()) 
else: print("Python not Found")

match = re.match(pattern, text) # Perform the match
if match: print("Python match:", match.group())
else: print ("Python not match")

replace = re.sub(pattern, replace, text) # Perform the replacement
if replace: print ("Replaced:", replace)
else: print ("Not Replcaed")

text2 = "apple, banana, carrot, orange"
pattern2 = r","
split_text = re.split(pattern2, text2) # Perform the split operation
print ("Pattern:", split_text)

#################################
import re
sub = "I will miss you definately"
pattern = r"you"
repl = "me"
rep = re.sub(pattern, repl, sub)
if rep: print ("replaced:", rep)
else: print ("Not replaced")