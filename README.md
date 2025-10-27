# PLD_5_C1
📌 Overview

This program is a simple Python application that collects a user’s name and age, validates the input, converts both values into binary format, creates a personalized message, and saves it to a text file. It then reads the saved message back to the user.

The project is divided into four separate files to demonstrate the use of modular programming and file handling in Python.

🗂️ Project Structure
UserInfoProgram/
│
├── helper_functions.py   # Contains validation, conversion, and message creation logic
├── file_manager.py       # Handles saving and reading messages from a text file
├── greetings.py          # Displays welcome and exit messages
├── main_program.py       # Controls the overall flow of the program
└── README.md             # Project documentation

⚙️ How It Works

The user is greeted with an introduction message.

The program asks for the user's name and age.

Inputs are validated:

The name must not be empty.

The age must be a valid number.

The name and age are converted into binary format.

A personalized message is created and displayed.

The message is saved to a file called user_message.txt.

The saved message is read and printed again.

A goodbye message is displayed.

🧩 Functions Summary
File: helper_functions.py

validate_input(user_input): Checks if input is non-empty and a string.

convert_to_binary(text): Converts text or numbers to binary.

create_message(name, age, name_binary, age_binary): Builds a personalized message.

File: file_manager.py

save_message(message): Saves the message to user_message.txt.

read_message(): Reads and prints the saved message with error handling.

File: greetings.py

show_intro(): Displays a welcome banner.

show_exit_message(): Displays a goodbye message.

File: main_program.py

get_user_info(): Collects and validates user input in a loop.

Main flow:

Displays intro message

Gets and validates user input

Converts inputs to binary

Creates and displays the personalized message

Saves and reads the message file

Displays exit message

▶️ How to Run the Program

Make sure all four Python files are in the same folder.

Open a terminal or command prompt in that folder.

Run the main program with:

python main_program.py


Follow the on-screen prompts.

💡 Example Output
==============================
Welcome to the User Info Program
==============================
Enter your name: 
Invalid name! Please try again.
Enter your name: Herve
Enter your age: hi
Invalid age! Please enter a number.
Enter your age: 23
Hello Herve, you are 23 years old!
Name in binary: 01001000 01100101 01110010 01110110 01100101
Age in binary: 0b10111
Message saved successfully.
Reading saved message...
Hello Herve, you are 23 years old!
Name in binary: 01001000 01100101 01110010 01110110 01100101
Age in binary: 0b10111
Thank you for using the program. Goodbye!

🧠 Concepts Demonstrated

Input validation

String and integer binary conversion

File handling (open, write, read)

Error handling using try and except

Modular programming and code organization