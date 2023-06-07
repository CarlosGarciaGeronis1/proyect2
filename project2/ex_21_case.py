#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '''
var x, y;
x = 3;
y = 0;
case x {
    when 1 {
        y = 10;
    }
    when 2 {
        y = 20;
    }
    when 3 {
        y = 30;
    }
    else {
        y = 40;
    }
}
y
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