from random import randint, choice

RULES = 'What is the result of the expression?'


def play_round():
    x = randint(0, 101)
    y = randint(0, 101)
    math_actions = ['+', '-', '*']
    task_generation = [str(x), choice(math_actions), str(y)]
    task = " ".join(task_generation)
    correct_answer = str(eval(task))
    return task, correct_answer
