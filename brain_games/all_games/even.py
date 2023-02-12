from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_round():
    num = randint(1, 1001)
    task = f'{num}'
    if num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return task, correct_answer
