def validate_input(user_input):
    """Checks if the input is not empty and is a string."""
    if user_input and isinstance(user_input, str):
        return True
    return False


def convert_to_binary(text):
    """Converts a string or number into its binary representation."""
    if text.isdigit():
        return bin(int(text))
    else:
        return ' '.join(format(ord(char), '08b') for char in text)


def create_message(name, age, name_binary, age_binary):
    """Creates a personalized message with name and age in binary."""
    message = (
        f"Hello {name}, you are {age} years old!\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
    return message
