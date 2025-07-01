import random

# List of choices: index 0 = Rock, index 1 = Paper, index 2 = Scissors
choices = ["✊ Rock", "✋ Paper", "✌️ Scissors"]

# Get user input
player = int(input("Choose: 1 is for '✊' (Rock), 2 is for '✋' (Paper), 3 is for '✌️' (Scissors): "))

# Convert to 0-based index
player_index = player -1
computer_index = random.randint(0,2)

print(f"\nYou chose {choices[player_index]}, Computer chose {choices[computer_index]}")

# Determine result
if player_index == computer_index:
    print("It's a tie!")
elif (player_index == 0 and computer_index == 2) or \
     (player_index == 1 and computer_index == 0) or \
     (player_index == 2 and computer_index == 1):
    print("You win! 🎉")
else:
    print("Computer wins! 😢")
