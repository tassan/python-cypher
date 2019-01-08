""" 
Implement test for cypher.py

How to Cypher a alphabet?

    Rotate the alphabet right or left for N positions
"""
# -*- coding: utf-8 -*-

from .context import caesar_cypher as cypher

import unittest


rotated_alphabet = []


class BasicTestSuite(unittest.TestCase):
    """Basic Test cases."""

    def test_alphabet_lowercase(self):
        assert cypher.alphabet_lowercase() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    def test_alphabet_uppercase(self):
        assert cypher.alphabet_uppercase() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    def test_letter_position(self):
        alphabet = cypher.alphabet_uppercase()
        assert cypher.letter_position('A', alphabet) == 0

    
    def test_move_letter(self):
        """ 
            Mover uma letra N posiçoes na lista e retornar a nova posicao
        """
        letter = 'A'
        direction = 'left'
        n = 3
        alphabet = []
        assert cypher.move_letter(letter, direction, n, alphabet) == 3

    def test_rotate_letter(self):
        letter = 'A'
        direction = 'left'
        n = 3
        alphabet = cypher.alphabet_uppercase()
        letter_rotate = cypher.rotate_letter(letter, direction, n, alphabet)
        assert cypher.letter_position(letter, letter_rotate) == n

    def test_rotate_alphabet(self):
        alphabet = []
        direction = 'left'
        n = 3
        assert cypher.rotate_alphabet(alphabet, direction, n) == rotated_alphabet

    def test_cyphered_letter_position(self):
        assert cypher.cyphered_letter_position('A', rotated_alphabet) == 2


    def test_replace_special_character(self):
        letter= 'Á'
        assert cypher.replace_special_character(letter) == 'A'
