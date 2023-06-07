#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '''
1 <= 2 == 1 != 0 > 0 < 0 <= 1
'''

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)