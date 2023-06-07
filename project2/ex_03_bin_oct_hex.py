#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '#x0FF1ce'

c = Compiler('expression_start')
c.realize(source, Phase.CODE_GENERATION)
print(c.parse_tree_str)
print()
print(c.wat_code)