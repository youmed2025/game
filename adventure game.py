import time
import random

# State variables are raised to the global level
total_score = 0
game_over = False
round_count = 0


def display_intro():
    """Shows game introduction and player directions."""
    print("Welcome to the adventure game!")
    print("You will make decisions that affect your outcome.")
    print("good luck!\n")
    time.sleep(2)


def get_player_choice(options):
    """
    You ask the player to choose from the options provided.
You repeat the correct choice.
    """
    choice = ""
    while choice not in options:
        choice = input(f"Choose one of the options {options}: ").lower()
        if choice not in options:
            print("Incorrect choice, try again.")
    return choice


def encounter_enemy():
    """Interact with an enemy, and you update points according to the result."""
    global total_score
    print("\nI found an enemy!")
    # Probability of winning or losing the encounter
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        print("I have defeated the enemy!")
        total_score += 10
    else:
        print("I lost the face-off with the enemy.")
        total_score -= 5
    time.sleep(1)


def find_treasure():
    """Update points when you find a treasure."""
    global total_score
    print("\nI found a treasure!")
    treasure_value = random.randint(5, 15)
    print(f"You have earned {treasure_value} points!")
    total_score += treasure_value
    time.sleep(1)


def player_action():
    """Determines the player's decision each turn."""
    print("\nWhat do you want to do?")
    print("1. Moving forward")
    print("2. break")
    print("3. Explore the area")
    options = ["1", "2", "3"]
    choice = get_player_choice(options)
    if choice == "1":
        # Possibility of meeting an opponent or finding treasure
        event = random.choice(["enemy", "treasure", "nothing"])
        if event == "enemy":
            encounter_enemy()
        elif event == "treasure":
            find_treasure()
        else:
            print("Nothing happens this time.")
    elif choice == "2":
        print("Take a break and rethink.")
        time.sleep(1)
    elif choice == "3":
        # Exploration may lead to random results.
        explore_event = random.choice(["Natural point", "Unexpected situation"])
        if explore_event == "Natural point":
            print("I found a source of drinkable water.")
            global total_score
            total_score += 2
        else:
            print("I encountered an unexpected situation. Nothing happens.")
    time.sleep(1)


def check_end_game():
    """Determines if the game ends based on points or turns."""
    global game_over
    if total_score >= 50:
        print("\nCongratulations! You've reached your goal and won!")
        game_over = True
    elif total_score <= -10:
        print("\nFell into tough circumstances, try again.")
        game_over = True
    elif round_count >= 10:
        print("\nThe number of specified roles has expired.")
        game_over = True


def main():
    """Main function of running the game."""
    global round_count
    display_intro()
    while not game_over:
        round_count += 1
        print(f"\n--- Round {round_count} ---")
        print(f"Your current points: {total_score}")
        player_action()
        check_end_game()
        time.sleep(1)


if __name__ == "__main__":
    main()
