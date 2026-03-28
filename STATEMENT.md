1. Problem Statement

The challenge is to create a simple, intelligent system capable of engaging in basic, personalized dialogue while overcoming the limitation of a fixed knowledge base. Most simple chat systems rely on hardcoded responses, which limits their utility. This project addresses the need for dynamic content generation by implementing a mechanism that allows the system to learn new input-output mappings from the user. The goal is to design a persistent memory function that enables the chatbot to gradually expand its ability to provide relevant and user-defined responses over time.

2. Scope of the Project

The scope is limited to a proof-of-concept Command-Line Interface (CLI) system focused strictly on the core learning and retrieval mechanics using a local file-based database.

In-Scope:

Database Setup: Initialization and persistence of the single knowledge table (BRAINDATA) using SQLite.

Dialogue Flow: Conditional logic for distinguishing between knowledge retrieval (found) and learning (not found).

Data CRUD: Implementing the Read (SELECT) operation for retrieval and the Create/Update (INSERT OR REPLACE) operation for learning.

Basic Access Control: Simple validation for user identity before starting the chat session.

Out-of-Scope:

Natural Language Processing (NLP), contextual awareness, or semantic understanding. The system relies on exact string matching.

Web interface, GUI, or external API integration.

Complex features like multi-user roles, concurrency control, or password hashing.

3. Target Users

The system is designed for two main user groups:

Primary User: The Creator (Abhi) who serves as the principal user, interacting with the system and actively providing and validating the knowledge base in the teaching mode.

Secondary Users: Developers and Students reviewing the code to understand the application of Python, the sqlite3 library, and the implementation of a basic database-backed knowledge system.

4. High-Level Features

Knowledge Persistence: Maintain a permanent, modifiable knowledge base saved locally within the SQLite file system.

Real-Time Learning: Ability to capture new input-response pairs (questions and answers) and commit them to the database within the live session.

Dynamic Response: The system's output is not fixed; it dynamically retrieves responses from its learned memory based on the user's input.

Guided Error Handling: When an unknown input is received, the system provides an explicit, guided path for the user to teach it a response, turning an execution failure into a core learning feature.