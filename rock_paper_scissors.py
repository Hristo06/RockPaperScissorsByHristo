import random
options = ["Rock", "Paper", "Scissors"]
wins_of_comp = 0
wins_of_player = 0
draws = 0
print(f"Welcome to Rock, Paper, Scissors game!")
while True:
    comp_pick = random.choice(options)
    player_pick = input("Please type one of the following options: Rock, Paper, Scissors\n")
    if player_pick == "Rock" or player_pick == "rock":
        print(f"I chose {comp_pick}")
        if comp_pick == "Paper":
            wins_of_comp += 1
            if wins_of_comp != 3:
                print("GG, EZ I WON THIS ONE YOU BAD!")
        elif comp_pick == "Rock":
            draws += 1
            print("Again!")
        else:
            wins_of_player += 1
            if wins_of_player != 3:
                print("My bad, I will win the next one!")
    elif player_pick == "Paper" or player_pick == "paper":
        print(f"I chose {comp_pick}")
        if comp_pick == "Scissors":
            wins_of_comp += 1
            if wins_of_comp != 3:
                print("GG, EZ I WON THIS ONE YOU BAD!")
        elif comp_pick == "Paper":
            draws += 1
            print("Again!")
        else:
            wins_of_player += 1
            if wins_of_player != 3:
                print("My bad, I will win the next one!")
    elif player_pick == "Scissors" or player_pick == "scissors":
        print(f"I chose {comp_pick}")
        if comp_pick == "Rock":
            wins_of_comp += 1
            if wins_of_comp != 3:
                print("GG, EZ I WON THIS ONE YOU BAD!")
        elif comp_pick == "Scissors":
            draws += 1
            print("Again!")
        else:
            wins_of_player += 1
            if wins_of_player != 3:
                print("My bad, I will win the next one!")
    else:
        print(f"Please type valid option")
        continue
    if wins_of_comp == 3 or wins_of_player == 3:
        if wins_of_comp == 3:
            print(f"You bad, go to sleep!")
            print(f"Your:\n"
                  f"Wins - {wins_of_player}\n"
                  f"Draws - {draws}\n"
                  f"Loses - {wins_of_comp}\n")
            quit()
        if wins_of_player == 3:
            print(f"JG diff!")
            print(f"Your:\n"
                  f"Wins - {wins_of_player}\n"
                  f"Draws - {draws}\n"
                  f"Loses - {wins_of_comp}\n")
            quit()