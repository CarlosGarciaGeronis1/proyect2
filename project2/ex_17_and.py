#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '10 && 20 && 30'

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)