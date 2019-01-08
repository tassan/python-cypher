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
    letters = list(map(chr, range(97, 123)))
    return letters

def alphabet_uppercase():
    letters = list(map(chr, range(65, 91)))
    return letters


def letter_position(letter, alphabet):
    return alphabet.index(letter)


def move_letter(letter, direction, n, alphabet):
    pass

def cyphered_letter_position(letter, rotated_alphabet):
    pass

def rotate_letter(letter, direction, n, alphabet):
    return ['a']

def rotate_alphabet(alphabet, direction, n):
    pass

def replace_special_character(letter):
    pass