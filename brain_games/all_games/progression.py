from random import randint

RULES = "What number is missing in the progression?"


def play_round():
    d = randint(1, 11)
    start_num = str(randint(0, 30))
    progres = [start_num]
    next_num = int(start_num)
    for n in range(9):
        next_num += d
        progres.append(str(next_num))
    hidden_num = randint(1, 10)
    correct_answer = progres[hidden_num]
    progres[hidden_num] = '..'
    task = ' '.join(progres)
    return task, correct_answer
