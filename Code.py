import random
Player_1 = 0
Player_2 = 0
actions = {'rock': 3, 'paper': 1, 'scissor': 2}
actions_1 = {3: 'rock', 1: 'paper', 2: 'scissor'}
cnt = 3
valid_options = ('rock', 'paper', 'scissor')
while cnt:
    computer_value = random.choice([1, 2, 3])
    while True:
        human_option = input("Enter the option from (rock, paper, scissor): ").lower()
        if human_option in valid_options:
            break
        else:
            print("Invalid input. Please choose from rock, paper, or scissor.")
    print("Computer Selected Option:", actions_1[computer_value])
    human_value = actions[human_option]
    result = {(1, 1): 0,  (1, 2): 2,  (1, 3): 1,  (2, 1): 1,  (2, 2): 0,  (2, 3): 2,  (3, 1): 2, (3, 2): 1,  (3, 3): 0, }
    winner = result[(computer_value, human_value)]

    if winner == 1:
        Player_1 += 1
    elif winner == 2:
        Player_2 += 1

    cnt -= 1

if Player_1 > Player_2:
    print("Computer Wins")
elif Player_1 < Player_2:
    print("Human Wins")
else:
    print("Tie")
