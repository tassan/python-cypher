""" 
Implement test for cypher.py

How to Cypher a alphabet?

    Rotate the alphabet right or left for N positions
"""
# -*- coding: utf-8 -*-

from .context import caesar_cypher as cypher

import unittest

alphabet = []
rotated_alphabet = []
direction = 'left'
n = 3

class BasicTestSuite(unittest.TestCase):
    """Basic Test cases."""

    def test_alphabet_lowercase(self):
        assert cypher.alphabet_lowercase() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def test_alphabet_uppercase(self):
        assert cypher.alphabet_uppercase() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def test_letter_position(self):
        assert cypher.letter_position('A') == 0

    def test_cyphered_letter_position(self):
        assert cypher.cyphered_letter_position('A') == 2

    def test_rotate_alphabet(self):
        assert cypher.rotate_alphabet(alphabet, direction, n) == rotated_alphabet



