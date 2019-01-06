""" 
"""


def generate_alphabet(uppercase=False):
    letters=[]
    if uppercase:
        letters = alphabet_uppercase()
    else:
        letters = alphabet_lowercase()
    return letters

def alphabet_lowercase():
    letters = []
    for letter in range(97,123):
        letters.append(chr(letter))
    return letters

def alphabet_uppercase():
    letters = []
    for letter in range(65,91):
        letters.append(chr(letter))
    return letters


def letter_position(letter):
    pass


def cyphered_letter_position(letter):
    pass


def rotate_alphabet(alphabet, direction, n):
    pass
