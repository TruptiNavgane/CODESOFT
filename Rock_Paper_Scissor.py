import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! you can try again"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win! you have good luck."
    else:
        return "Computer wins! you can try again"

def main():
    user_score = 0
    computer_score = 0

    choices = ['rock', 'paper', 'scissors']

    print("Welcome to Rock, Paper, Scissors Game! enjoy while playing")

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.\n please choose from below options")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! Final scores - You: {}, Computer: {}".format(user_score, computer_score))

if __name__ == "__main__":
    main()
