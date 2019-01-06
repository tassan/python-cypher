def __init__(self):
    self.alphabet = generate_alphabet()


def generate_alphabet():
    letters = []
    for letter in range(97,123):
        letters.append(chr(letter))
    return letters