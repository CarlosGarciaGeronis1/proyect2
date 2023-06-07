# File: tests/test_21_case.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestCaseWhen(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('case {}')

    def test_semantic_mistake(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var case; 0')

    def test_case1(self):
        self.assertEqual(0,
                         self.c.realize('''
                         var x;
                         case 0 { }
                         x
                         '''))

    def test_case2(self):
        self.assertEqual(0,
                         self.c.realize('''
                         var x;
                         case 0 {
                            when 0 { }
                            when 1 { }
                            when 2 { }
                            when 3 { }
                            when 4 { }
                            when 5 { }
                            else { }
                         }
                         x
                         '''))

    def test_case3(self):
        self.assertEqual(1,
                         self.c.realize('''
                         var x;
                         case true {
                            when true {
                                x = 1;
                            }
                            when false {
                                x = 2;
                            }
                         }
                         x
                         '''))

    def test_case4(self):
        self.assertEqual(2,
                         self.c.realize('''
                         var x;
                         case false {
                            when true {
                                x = 1;
                            }
                            when false {
                                x = 2;
                            }
                         }
                         x
                         '''))

    def test_case5(self):
        self.assertEqual(40,
                         self.c.realize('''
                         var x, y;
                         x = 0;
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
                         '''))

    def test_case6(self):
        self.assertEqual(0,
                         self.c.realize('''
                         var x, y;
                         x = 0;
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
                         }
                         y
                         '''))

    def test_case7(self):
        self.assertEqual(30,
                         self.c.realize('''
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
                         '''))

    def test_case8(self):
        self.assertEqual(333,
                         self.c.realize('''
                         var x, y, z;
                         x = 2;
                         y = 4;
                         z = 0;
                         case x + y * z {
                             when 3 - 2 {
                                 z = 100;
                             }
                             when 5 - 2 {
                                 z = 200;
                             }
                             when 1 + 1 {
                                 z = 300;
                                 case y - 1 {
                                     when x {
                                        y = y + 0;
                                        z = z + 10;
                                     }
                                     when x + 1 {
                                        y = y + 1;
                                        z = z + 10;
                                     }
                                     when x + 2 {
                                        y = y + 2;
                                        z = z + 20;
                                     }
                                     when x + 3 {
                                        y = y + 3;
                                        z = z + 30;
                                     }
                                     else {
                                        y = y + 4;
                                        z = z + 40;
                                     }
                                 }
                                 z = z + 18;
                             }
                             else {
                                 z = 400;
                             }
                         }
                         y + z
                         '''))