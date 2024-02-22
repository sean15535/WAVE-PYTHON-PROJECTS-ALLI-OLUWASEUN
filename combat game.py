game_over = False
while not game_over:
    
    player_action = input("Enter your move (e.g., 'attack', 'defend'): ")
    
    
    if player_action == 'attack':
            print("Congratulations! You win!")
            game_over = True
    elif player_action == 'defend':
         print("You defended successfully!")
    else:
            print("Game over! You lose!")
            break
