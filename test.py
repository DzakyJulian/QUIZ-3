from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
x = symbols("x")
f = "6x^2"
print(parse_expr(f, transformations="all"))