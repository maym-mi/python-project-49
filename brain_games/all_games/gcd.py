from random import randint
from math import gcd

RULES = "Find the greatest common divisor of given numbers."


def play_round():
    a = randint(0, 100)
    b = randint(0, 100)
    while gcd(a, b) == 1:
        a = randint(0, 100)
        b = randint(0, 100)
    task = f"{a} and {b}"
    correct_answer = str(gcd(a, b))
    return task, correct_answer
