import prompt

ROUNDS = 3


def engine(name_game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string("May I have your name? ")
    print(f'Hello, {name_user}')
    print(name_game.RULES)
    for _ in range(ROUNDS):
        task, correct_answer = name_game.play_round()
        print(f'Task: {task}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name_user}!")
            return
    print(f'Congratulations, {name_user}!')
