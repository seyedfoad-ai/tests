import json
import os
import random

HISTORY_FILE = "history.json"


def load_history():
    """Load game history from file, or return default history."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                pass
    return {"scores": [], "high_score": 0}


def save_history(history):
    """Save game history to file."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2)


def roll_dice():
    """Simulate rolling two dice and return their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll_sum = die1 + die2
    print(f"You rolled {die1} and {die2}. Sum: {roll_sum}")
    return roll_sum


def play_round():
    """Play a round consisting of five rolls."""
    total = 0
    rolls = []
    for _ in range(5):
        input("Press Enter to roll the dice...")
        roll_sum = roll_dice()
        rolls.append(roll_sum)
        total += roll_sum
    print(f"Roll sums: {rolls}")
    print(f"Total score this round: {total}")
    return total


def main():
    history = load_history()
    while True:
        total = play_round()
        if total > history["high_score"]:
            print("Congratulations! New high score!")
            history["high_score"] = total
        else:
            print(f"Current high score: {history['high_score']}")
        history["scores"].append(total)
        save_history(history)
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
