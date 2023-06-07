#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '31 & 42 | 5 ^ 7'

c = Compiler('expression_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)