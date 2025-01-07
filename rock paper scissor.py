import random

# Initialize scores for the user and computer
user_wins = 0
computer_wins = 0

# Define the available options for the game
options = ["rock", "paper", "scissors"]

# Start the game loop
while True:
    # Prompt the user for input and convert it to lowercase
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    # Check if the user wants to quit the game
    if user_input == "q":
        break

    # Validate user input
    if user_input not in options:
        # Skip the rest of the loop if input is invalid
        continue

    # Randomly select the computer's choice
    random_number = random.randint(0, 2)  # Generate a number between 0 and 2
    computer_pick = options[random_number]  # Maps the number to an option
    print("Computer picked", computer_pick + ".")

    # Determine the winner based on the game's rules
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1  # Increments user score

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1  # Increments user score

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1  # Increments user score

    else:
        print("You lost!")
        computer_wins += 1  # Increments computer score

# Display the final scores after the user quits
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")