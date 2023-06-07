#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '42'

c = Compiler('expression_start')
c.realize(source, Phase.SYNTACTIC_ANALYSIS)
print(c.parse_tree_str)
print(c.wat_code)
print(c.result)
