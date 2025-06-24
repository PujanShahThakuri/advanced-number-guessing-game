import random
import datetime

def play_game():
    """
    Runs one session of the guessing game.
    Generates secret number and lets the user guess with hints.
    Saves the result to a file.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    won = False

    print("\n🎯 I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess (1-100): "))
            if not 1 <= guess <= 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue  # Don't count invalid input as an attempt

            attempts += 1

            if guess < secret_number:
                print("📉 Too low!")
            elif guess > secret_number:
                print("📈 Too high!")
            else:
                print(f"🎉 You guessed it in {attempts} attempts!")
                won = True
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

    if not won:
        print(f"\n❌ Game over! The number was {secret_number}.")

    # Save result to history file with timestamp
    with open("game_history.txt", "a") as file:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "WIN" if won else "LOSE"
        file.write(f"[{time}] Result: {result}, Attempts: {attempts}, Number: {secret_number}\n")

def main():
    """
    Main function to run the guessing game repeatedly
    until the user decides to quit.
    """
    print("=== 🧠 Advanced Number Guessing Game ===")
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
