#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '''
var x, y;
x = 2;
y = (x + 1) * 3;
var z;
z = y - 1;
x + y + z    
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