from random import randint

RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def play_round():
    task = randint(1, 200)
    for d in range(2, int(task**0.5) + 1):
        if task % d == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return task, correct_answer
