#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '''
var x;
x = 3;
{ x - 2, x + x, x * x } + 1
'''

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
print()
print(c.symbol_table)
print()
print(c.wat_code)
print()
print(c.result)