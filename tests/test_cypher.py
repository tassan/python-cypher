""" 
Implement test for cypher.py

How to Cypher a alphabet?

    Rotate the alphabet right or left for N positions
"""
import pytest
from cypher import cypher as cyp

alphabet = []
rotated_alphabet = []
direction = 'left'
n = 3

# def test_generate_alphabet():
#     assert generate_alphabet() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_letter_position():
    assert cyp.letter_position('A') == 0

def test_cyphered_letter_position():
    assert cyp.cyphered_letter_position('A') == 2

def test_rotate_alphabet():
    assert cyp.rotate_alphabet(alphabet, direction, n) == rotated_alphabet



