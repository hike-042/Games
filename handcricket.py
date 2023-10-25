import random

def play_handcricket():
    print("Welcome to Handcricket Game!")
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")

    while True:
        player1_number = int(input(f"{player1_name}, enter a number from 1 to 6: "))
        player2_number = random.randint(1, 6)
        print(f"{player2_name}, your number is: {player2_number}")
        
        toss_sum = player1_number + player2_number
        
        if toss_sum % 2 == 0:
            toss_result = "even"
        else:
            toss_result = "odd"
        
        if toss_result == "even":
            print(f"{player1_name} wins the toss!")
            player1_decision = input(f"{player1_name}, choose batting or bowling: ").lower()
            player2_decision = "bowling" if player1_decision == "batting" else "batting"
            break
        elif toss_result == "odd":
            print(f"{player2_name} wins the toss!")
            player2_decision = input(f"{player2_name}, choose batting or bowling: ").lower()
            player1_decision = "bowling" if player2_decision == "batting" else "batting"
            break
        else:
            print("Toss result doesn't match. Please try again.")
    
    print("Start the Game")
    
    if player1_decision == "batting":
        batting_player = player1_name
        bowling_player = player2_name
    else:
        batting_player = player2_name
        bowling_player = player1_name
    
    print(f"{batting_player} is batting.")
    
    batting_score = 0
    batting_runs = []
    
    # Start the game
    while True:
        player_runs = int(input(f"{batting_player}, enter your runs (1-6): "))
        
        if player_runs < 1 or player_runs > 6:
            print("Invalid run. Please choose a number between 1 and 6.")
            continue
        
        computer_runs = random.randint(1, 6)
        
        print(f"{bowling_player} plays {computer_runs}.")
        
        if player_runs == computer_runs:
            print(f"{batting_player} is out!")
            break
        
        batting_score += player_runs
        batting_runs.append(player_runs)
    
    print(f"{batting_player} scored {batting_score} runs.")
    
    if player1_decision == "batting":
        target = batting_score
        chasing_player = player2_name
        bowling_player = player1_name
    else:
        target = batting_score
        chasing_player = player1_name
        bowling_player = player2_name
    
    print(f"{chasing_player} needs to chase {target+1} runs.")
    
    chasing_score = 0
    
    # Start the chase
    while True:
        player_runs = int(input(f"{chasing_player}, enter your runs (1-6): "))
        
        if player_runs < 1 or player_runs > 6:
            print("Invalid run. Please choose a number between 1 and 6.")
            continue
        
        computer_runs = random.randint(1, 6)
        
        print(f"{bowling_player} plays {computer_runs}.")
        
        if player_runs == computer_runs:
            print(f"{chasing_player} is out!")
            print(f"{bowling_player} is win!")
            break
        
        chasing_score += player_runs
        
        if chasing_score > target:
            print(f"{chasing_player} wins!")
            break
    
    # print(f"{_player} wins!")
    
play_handcricket()
