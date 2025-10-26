from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message


def get_user_info():
    """Collects and validates user input for name and age."""
    while True:
        name = input("Enter your name: ")
        if not validate_input(name):
            print("Invalid name! Please try again.")
            continue

        age = input("Enter your age: ")
        if not age.isdigit():
            print("Invalid age! Please enter a number.")
            continue

        return name, age


if __name__ == "__main__":
    show_intro()

    name, age = get_user_info()

    # Convert to binary
    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)

    # Create personalized message
    message = create_message(name, age, name_binary, age_binary)

    # Display and save message
    print(message)
    save_message(message)

    # Read back from file
    read_message()

    # Exit message
    show_exit_message()
