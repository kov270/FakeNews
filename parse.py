from histogram import Dictogram
import random
from collections import deque
import re


def generate_random_start(model):
    if '.' in model:
        seed_word = '.'
        while seed_word == '.':
            seed_word = model['.'].return_weighted_random_word()
            print(seed_word)
        return seed_word


def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return sentence