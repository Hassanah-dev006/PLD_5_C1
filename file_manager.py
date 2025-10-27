def save_message(message):
    """Saves the message to a text file with error handling."""
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"Error saving the message: {e}")


def read_message():
    """Reads the saved message and displays it."""
    try:
        print("Reading saved message...")
        with open("user_message.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: No saved message found.")
    except Exception as e:
        print(f"Error reading the message: {e}")
