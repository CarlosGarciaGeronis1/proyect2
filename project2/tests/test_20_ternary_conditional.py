# File: tests/test_20_ternary_conditional.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from wasmtime._trap import Trap


class TestTernaryConditional(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('{1, 2}')

    def test_ternary1(self):
        self.assertEqual(1,
                         self.c.realize('{true, 1, 2}'))

    def test_ternary2(self):
        self.assertEqual(2,
                         self.c.realize('{false, 1, 2}'))

    def test_ternary3(self):
        self.assertEqual(1,
                         self.c.realize('''
                         var a;
                         a = true;
                         a = {a, 1, 2};
                         a'''))

    def test_ternary4(self):
        self.assertEqual(2,
                         self.c.realize('''
                         var a;
                         a = false;
                         a = {a, 1, 2};
                         a'''))

    def test_ternary5(self):
        self.assertEqual(7,
                         self.c.realize('''
                         var x;
                         x = 3;
                         { x - 2, x + x, x * x } + 1
                         '''))

    def test_ternary6(self):
        self.assertEqual(10,
                         self.c.realize('''
                         var x;
                         x = 3;
                         { x - 3, x + x, x * x } + 1
                         '''))

    def test_ternary7(self):
        self.assertEqual(4,
                         self.c.realize('''
                         var x;
                         x = 3;
                         if {x - 3, false, true} {
                            x = x + 1;
                         } else {
                            x = x - 1;
                         }
                         x
                         '''))

    def test_ternary8(self):
        self.assertEqual(2,
                         self.c.realize('''
                         var x;
                         x = 3;
                         if !{x - 3, false, true} {
                            x = x + 1;
                         } else {
                            x = x - 1;
                         }
                         x
                         '''))

    def test_ternary9(self):
        self.assertEqual(8,
                         self.c.realize('''
                         var x, y, z;
                         x = 2;
                         y = x * 2 - 1;
                         z = x + y;
                         { {!z, false, true},
                           {x, {!y, x + z, z + y}, z},
                           {y, z, x}
                         }
                         '''))

    def test_ternary10(self):
        self.assertEqual(1,
                         self.c.realize('''
                         var t, u;
                         t = false;
                         u = true;
                         {t, u/t, u}
                         '''))

    def test_ternary11(self):
        self.assertEqual(1,
                         self.c.realize('''
                         var a, b;
                         a = 0;
                         {a, 1 / a, {!a, 1, 1 / a}}
                         '''))

    def test_ternary_runtime_error(self):
        with self.assertRaises(Trap):
            self.c.realize('''
            var t, u;
            t = false;
            u = true;
            {!t, u/t, u}
            ''')