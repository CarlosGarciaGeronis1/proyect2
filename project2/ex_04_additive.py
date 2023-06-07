#Author: A01748393 Carlos Garcia Geronis
from delta import Compiler, Phase 

source = '12 + 34 - 56'

c = Compiler('expression_start')
c.realize(source, Phase.SYNTACTIC_ANALYSIS)
print(c.parse_tree_str)
print()
