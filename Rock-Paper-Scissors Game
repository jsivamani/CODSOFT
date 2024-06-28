import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        print("\nEnter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_input = input("Choose (1/2/3): ")

        if user_input not in ['1', '2', '3']:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        user_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}[user_input]
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScores: You - {user_score}, Computer - {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing! Final scores:")
    print(f"You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
