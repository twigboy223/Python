import time
import random


def play_round(points: int) -> tuple[int, bool]:
    """Play a single round. Returns (updated_points, continue_playing).

    continue_playing is False if the player typed 'quit' during the round.
    """
    number = random.randint(1, 500)

    while True:
        answer = input("Guess a number between 1 and 500 (or type 'quit' to stop): ").strip().lower()
        if answer in ("quit", "exit", "q"):
            return points, False

        try:
            guess = int(answer)
        except ValueError:
            print("Please enter a whole number or 'quit'.")
            continue

        if guess == number:
            points += 50
            print(f"You got it! The number was {number}. Your score is now {points}.")
            return points, True
        elif guess < number:
            points -= 5
            print(f"Too low. Score: {points}")
        else:
            points -= 5
            print(f"Too high. Score: {points}")


def main():
    print("Welcome to the Number Guessing Game — first to 500 points wins!")
    time.sleep(2)
    print("Correct guess: +50 points. Wrong guess: -5 points. Type 'quit' to stop anytime.")
    time.sleep(3)

    points = 0

    while points < 500:
        points, continued = play_round(points)
        if not continued:
            print(f"You stopped playing. Final points: {points}")
            return

        if points >= 500:
            print(f"fuck you You reached {points} points and won the game!")
            return

        # Ask whether to play another round; intro message is shown only once at start
        while True:
            again = input("Play again? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                break  # start a new round without re-printing the intro
            elif again in ("no", "n"):
                print(f"Thanks for playing! Final points: {points}")
                return
            else:
                print("Please answer 'yes' or 'no'.")


if __name__ == "__main__":
    main()
