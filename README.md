# Self-Learning Console Chatbot (AI)
Vityarthi AI-ML Project


Overview of the Project

This project implements a simple, console-based chatbot with a self-learning capability. The chatbot utilizes a local SQLite database to store a growing knowledge base of user inputs and learned responses. When a user enters a query, the system first checks its memory (the database). If the query is unknown, the system enters a teaching mode, allowing the user to provide a correct response, which is then permanently stored for future use.

The project demonstrates key concepts of database integration, simple data retrieval logic, and conditional execution flow in Python.

Features

Basic Authentication: Access to the chat functionality is gated by a simple name check (Abhi).

Knowledge Retrieval: Uses the SQLite database to retrieve learned responses (outvalue) based on user input (inkey).

Self-Learning (Teaching Mode): If a query is unknown, the system prompts the user to input the correct reply, effectively updating its knowledge base in real-time.

Persistent Memory: All learned input-response pairs are saved in the BRAINDATA table within the local CHATBOT.db file.

Graceful Exit: Supports the case-insensitive command 'bye' to safely close the database connection and terminate.

Technologies/Tools Used

Core Language Python 3.x

Database SQLite 3

Library sqlite3

Version Control Git

Steps to Install & Run the Project

Clone the Repository:

git clone [Your_Repository_URL]

Navigate to the Project Directory:

cd [your-project-folder]

Run the Application:

The system uses Python's standard libraries, so no extra installations are needed.

Execute the main script (e.g., chatbot_sqlite.py):

python chatbot_sqlite.py

The system will automatically create the CHATBOT.db file upon first execution.

Instructions for Testing

Authentication Test:

When prompted "What is your name:", enter Abhi. (Verify successful login).

Restart the script and enter any other name. (Verify access denial).

Learning Test (First Run):

Enter a new question, e.g., "What is your favorite color?".

The chatbot will reply: "Sorry, I didn't understand...".

Enter a teaching response, e.g., "I like blue".

Verify the system prints: "I got what you said. Thanks for teaching!"

Retrieval Test (Second Run):

Enter the exact same question: "What is your favorite color?".

Verify the system replies with the stored response: "I like blue".

Exit Test:

Type bye (or Bye, BYE). Verify the system prints "Good bye! Talk to you later." and terminates.
