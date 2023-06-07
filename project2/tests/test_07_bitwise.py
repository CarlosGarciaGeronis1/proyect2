# File: tests/test_07_bitwise.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestBitwise(TestCase):

    def setUp(self):
        self.c = Compiler('expression_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('1 &')

    def test_and1(self):
        self.assertEqual(0,
                         self.c.realize('10 & 5'))

    def test_and2(self):
        self.assertEqual(7,
                         self.c.realize('7 & 15'))

    def test_or1(self):
        self.assertEqual(15,
                         self.c.realize('10 | 5'))

    def test_or2(self):
        self.assertEqual(15,
                         self.c.realize('7 | 15'))

    def test_xor1(self):
        self.assertEqual(15,
                         self.c.realize('10 ^ 5'))

    def test_xor2(self):
        self.assertEqual(8,
                         self.c.realize('7 ^ 15'))

    def test_mix1(self):
        self.assertEqual(8,
                         self.c.realize('31 & 42 | 5 ^ 7'))

    def test_mix2(self):
        self.assertEqual(8,
                         self.c.realize('15 + 16 & 6 * 7 '
                                        '| 5 * 1 ^ 1 * 7'))