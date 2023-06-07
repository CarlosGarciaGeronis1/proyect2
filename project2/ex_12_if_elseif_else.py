#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '''
var x, y;
x = 5;
if x - 5 {
    y = 1;
} else if x * 0 {
    y = 2;
} else if x - 1 {
    y = 3;
} else {
    y = 4;
}
y
'''

c = Compiler('program_start')
c.realize(source, Phase.CODE_GENERATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)