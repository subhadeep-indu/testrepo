from sympy import symbols, solve
str = "12 = 8 + x/2"
str = str.split("=")
x = symbols('x')
if (str[0].find("x")) >= 0 :
   str = str[0] + "-" + str[1]
else:
   str = str[1] + "-" + str[0]
str = solve(str)
print(type(str))
print(str)