def get_non_empty_input(answer):
    """Prompt user for input until a non-empty string is entered."""
    while True:
        value = input(answer).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def get_valid_age(answer):
    """Prompt user for age input until a valid integer is entered."""
    while True:
        value = input(answer).strip()
        try:
            return int(value)
        except ValueError:
            print("Invalid input! Please enter a valid number for age.")

while True:
    # Get validated inputs
    name = get_non_empty_input("Please enter your name: ")
    age = get_valid_age("What is your age? ")
    location = get_non_empty_input("Where are you located? ")

    # Print user information
    print(f"Hello {name.title()}, you are {age} years old and currently residing in {location}.")

    # Ask if the user wants to continue
    play_again = input("Do you want to do this again? (yes/no): ").strip().lower()
    if play_again.startswith("n"):
        print("Goodbye!")
        break
