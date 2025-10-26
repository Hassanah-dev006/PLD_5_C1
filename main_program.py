from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, 
show_exit_message


def get_user_info():
  while True:
        name = input("Enter your name: ").strip()
        if validate_input(name):
            break
        print("Invalid name! Please try again.")
    
    while True:
        age = input("Enter your age: ").strip()
        if validate_input(age) and age.isdigit():
            break
        print("Invalid age! Please enter a number.")
    
    return name, age


if __name__ == "__main__":
    show_intro()

    name, age = get_user_info()

    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)

    message = create_message(name, age, name_binary, age_binary)

    print(message)
    save_message(message)

    read_message()
    show_exit_message()
